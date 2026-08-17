from __future__ import annotations

import html
import re
import shutil
import subprocess
import tempfile
from pathlib import Path
from urllib.request import urlretrieve

ROOT = Path(__file__).resolve().parents[2]
ASSETS = ROOT / "assets" / "projects"
ASSETS.mkdir(parents=True, exist_ok=True)

DEMOS = {
    "jobiverse-final-report": "https://raw.githubusercontent.com/neunglog-sys/job_simulator/main/docs/media/gif/final_report.gif",
    "jobiverse-simulation": "https://raw.githubusercontent.com/neunglog-sys/job_simulator/main/docs/media/gif/senario2.gif",
    "rainbow-bridge-demo": "https://raw.githubusercontent.com/mosejong/mosejong/main/assets/rainbow-bridge-demo.gif",
}


def run(*args: str) -> None:
    subprocess.run(args, check=True)


def human(n: int) -> str:
    return f"{n / 1024:.1f} KiB" if n < 1024 * 1024 else f"{n / 1024 / 1024:.2f} MiB"


def video_tag(prefix: str, name: str, alt: str, preload: str) -> str:
    alt_q = html.escape(alt, quote=True)
    return (
        f'<video class="media-video" data-demo-video muted loop playsinline preload="{preload}" '
        f'poster="{prefix}{name}-poster.webp" aria-label="{alt_q}">'
        f'<source src="{prefix}{name}.mp4" type="video/mp4"></video>'
    )


def replace_gif_img(text: str, url: str, prefix: str, name: str, preload: str) -> str:
    pat = re.compile(
        r'<img\s+src="' + re.escape(url) + r'"\s+alt="([^"]+)"(?:\s+loading="lazy")?\s*>'
    )
    text, n = pat.subn(lambda m: video_tag(prefix, name, m.group(1), preload), text)
    if n == 0:
        raise RuntimeError(f"GIF image tag not found: {url}")
    return text


def add_video_controller(text: str) -> str:
    marker = "<!-- PERF_V12_VIDEO -->"
    if marker in text:
        return text
    js = r'''<!-- PERF_V12_VIDEO --><script>(()=>{const q=window.matchMedia('(prefers-reduced-motion: reduce)');const v=[...document.querySelectorAll('video[data-demo-video]')];if(!v.length)return;const stop=()=>v.forEach(x=>{x.pause();try{x.currentTime=0}catch(_){}});if(q.matches){stop();return}if(!('IntersectionObserver'in window)){v.forEach(x=>x.play().catch(()=>{}));return}const o=new IntersectionObserver(e=>e.forEach(({target:t,isIntersecting:i})=>{if(i)t.play().catch(()=>{});else t.pause()}),{rootMargin:'150px 0px',threshold:.05});v.forEach(x=>o.observe(x));q.addEventListener?.('change',e=>{if(e.matches){o.disconnect();stop()}})})();</script>'''
    if "</body>" not in text:
        raise RuntimeError("body close not found")
    return text.replace("</body>", js + "</body>", 1)


def optimize_media() -> dict[str, tuple[int, int]]:
    stats: dict[str, tuple[int, int]] = {}
    with tempfile.TemporaryDirectory() as td:
        td_path = Path(td)
        for name, url in DEMOS.items():
            src = td_path / f"{name}.gif"
            urlretrieve(url, src)
            mp4 = ASSETS / f"{name}.mp4"
            poster = ASSETS / f"{name}-poster.webp"
            run(
                "ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", str(src),
                "-vf", "fps=12", "-an", "-c:v", "libx264", "-preset", "medium", "-crf", "26",
                "-pix_fmt", "yuv420p", "-movflags", "+faststart", str(mp4),
            )
            run(
                "ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", str(src),
                "-frames:v", "1", "-c:v", "libwebp", "-quality", "84", str(poster),
            )
            before, after = src.stat().st_size, mp4.stat().st_size
            if after >= before:
                raise RuntimeError(f"MP4 did not shrink: {name} {before} -> {after}")
            stats[name] = (before, after)

    for stem in ("schoolbridge-parent", "schoolbridge-teacher", "procurement-home"):
        src = ASSETS / f"{stem}.png"
        dst = ASSETS / f"{stem}.webp"
        run("cwebp", "-quiet", "-q", "90", "-m", "6", str(src), "-o", str(dst))
        if dst.stat().st_size >= src.stat().st_size:
            raise RuntimeError(f"WebP did not shrink: {stem}")
        stats[stem] = (src.stat().st_size, dst.stat().st_size)
    return stats


def patch_main() -> None:
    p = ROOT / "index.html"
    s = p.read_text(encoding="utf-8")
    s = replace_gif_img(s, DEMOS["jobiverse-final-report"], "assets/projects/", "jobiverse-final-report", "none")
    s = replace_gif_img(s, DEMOS["jobiverse-simulation"], "assets/projects/", "jobiverse-simulation", "none")
    s = replace_gif_img(s, DEMOS["rainbow-bridge-demo"], "assets/projects/", "rainbow-bridge-demo", "none")
    for stem in ("schoolbridge-parent", "schoolbridge-teacher", "procurement-home"):
        s = s.replace(f"assets/projects/{stem}.png", f"assets/projects/{stem}.webp")
    # Below-fold screenshots and hidden award thumbnails should decode off the main thread.
    s = re.sub(r'(<img src="assets/projects/[^"]+\.webp" alt="[^"]+" loading="lazy")(>)', r'\1 decoding="async"\2', s)
    s = re.sub(r'(<img src="assets/awards/[^"]+\.webp" alt="[^"]+")(>)', r'\1 loading="lazy" decoding="async"\2', s)
    s = s.replace('<link rel="preconnect" href="https://raw.githubusercontent.com" crossorigin>', '')
    css = '''\n    /* PERF_V12_START */\n    .media-video{width:100%;height:100%;display:block;object-fit:cover;object-position:center top;background:#0a0e14}\n    .single-real-screen .media-video,.phone-demo .media-video{object-fit:contain}\n    /* PERF_V12_END */\n'''
    if "PERF_V12_START" not in s:
        s = s.replace("  </style>", css + "  </style>", 1)
    s = add_video_controller(s)
    p.write_text(s, encoding="utf-8")


def patch_case(path: str, video_names: list[str] | None = None) -> None:
    p = ROOT / "projects" / path
    s = p.read_text(encoding="utf-8")
    if video_names:
        for name in video_names:
            s = replace_gif_img(s, DEMOS[name], "../assets/projects/", name, "metadata")
    for stem in ("schoolbridge-parent", "schoolbridge-teacher", "procurement-home"):
        s = s.replace(f"../assets/projects/{stem}.png", f"../assets/projects/{stem}.webp")
    # Hero images remain eager but async-decoded; gallery images are lazy.
    s = re.sub(r'(<img src="\.\./assets/projects/[^"]+\.webp" alt="[^"]+")(>)', r'\1 decoding="async"\2', s)
    s = re.sub(r'(<img src="\.\./assets/projects/[^"]+\.webp" alt="[^"]+" loading="lazy")(>)', r'\1 decoding="async"\2', s)
    s = s.replace('<link rel="preconnect" href="https://raw.githubusercontent.com" crossorigin>', '')
    if video_names:
        s = add_video_controller(s)
    p.write_text(s, encoding="utf-8")


def patch_css() -> None:
    p = ROOT / "assets" / "case-study.css"
    s = p.read_text(encoding="utf-8")
    marker = "/*PERF_V12_START*/"
    if marker not in s:
        s += (
            marker
            + ".media-video{width:100%;height:100%;display:block;object-fit:cover;object-position:top center;background:#0a0e13}"
            + ".hero-media.contain .media-video{object-fit:contain}.shot .media-video{aspect-ratio:16/10}.shot.phone .media-video{object-fit:contain;aspect-ratio:16/11}"
            + "@media(prefers-reduced-motion:reduce){.media-video{animation:none!important}}"
            + "/*PERF_V12_END*/"
        )
    p.write_text(s, encoding="utf-8")


def validate(stats: dict[str, tuple[int, int]]) -> None:
    pages = [ROOT / "index.html", *sorted((ROOT / "projects").glob("*.html"))]
    joined = "\n".join(p.read_text(encoding="utf-8") for p in pages)
    if "raw.githubusercontent.com" in joined:
        raise RuntimeError("raw.githubusercontent.com remains in HTML")
    if re.search(r'<img[^>]+\.gif', joined, re.I):
        raise RuntimeError("GIF img tag remains")
    for stem in ("schoolbridge-parent", "schoolbridge-teacher", "procurement-home"):
        if f"assets/projects/{stem}.png" in joined or f"../assets/projects/{stem}.png" in joined:
            raise RuntimeError(f"PNG reference remains: {stem}")
    if "loading=\"lazy\" decoding=\"async\"" not in (ROOT / "index.html").read_text(encoding="utf-8"):
        raise RuntimeError("lazy async decoding not installed")
    for name in DEMOS:
        for suffix in (".mp4", "-poster.webp"):
            if not (ASSETS / f"{name}{suffix}").exists():
                raise RuntimeError(f"missing generated media: {name}{suffix}")
    print("MEDIA SIZE REPORT")
    total_before = total_after = 0
    for name, (before, after) in stats.items():
        total_before += before
        total_after += after
        print(f"{name}: {human(before)} -> {human(after)} ({(1-after/before)*100:.1f}% smaller)")
    print(f"TOTAL tracked assets: {human(total_before)} -> {human(total_after)} ({(1-total_after/total_before)*100:.1f}% smaller)")
    print("VALIDATION PASS")


def main() -> None:
    stats = optimize_media()
    patch_main()
    patch_case("jobiverse.html", ["jobiverse-final-report", "jobiverse-simulation"])
    patch_case("rainbow-bridge.html", ["rainbow-bridge-demo"])
    patch_case("schoolbridge.html")
    patch_case("procurement-logistics-ai.html")
    patch_css()
    validate(stats)


if __name__ == "__main__":
    main()
