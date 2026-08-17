from __future__ import annotations

from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlparse
import json
import re

from PIL import Image, ImageDraw, ImageFont

ROOT = Path('.')
BASE = 'https://mosejong.github.io'

PAGES = {
    'index.html': {
        'title': '모세종 | Python · FastAPI AI Backend Developer',
        'description': '물류·운영 경험을 바탕으로 Python · FastAPI로 API, DB, AI 기능을 연결하고 테스트와 수치로 검증하는 AI 백엔드 개발자 모세종의 포트폴리오.',
        'url': f'{BASE}/',
        'image': f'{BASE}/assets/og/portfolio.png',
        'type': 'website',
    },
    'projects/jobiverse.html': {
        'title': 'Jobiverse Case Study | 모세종',
        'description': 'AI 상담 → 가상 직무 체험 → 근거 기반 리포트로 이어지는 Jobiverse. Reporting · Data Pipeline 중심 Case Study.',
        'url': f'{BASE}/projects/jobiverse.html',
        'image': f'{BASE}/assets/og/jobiverse.png',
        'type': 'article',
    },
    'projects/schoolbridge.html': {
        'title': 'SchoolBridge Case Study | 모세종',
        'description': '가정통신문 핵심 행동정보를 보존하며 8개 언어 NLLB 번역과 TTS로 연결한 SchoolBridge Case Study.',
        'url': f'{BASE}/projects/schoolbridge.html',
        'image': f'{BASE}/assets/og/schoolbridge.png',
        'type': 'article',
    },
    'projects/rainbow-bridge.html': {
        'title': 'Rainbow Bridge Case Study | 모세종',
        'description': 'AI 펫로스 애프터케어 서비스의 Team Lead · Backend Integration 경험을 정리한 Rainbow Bridge Case Study.',
        'url': f'{BASE}/projects/rainbow-bridge.html',
        'image': f'{BASE}/assets/og/rainbow-bridge.png',
        'type': 'article',
    },
    'projects/procurement-logistics-ai.html': {
        'title': 'Procurement Logistics AI Case Study | 모세종',
        'description': '공공조달 수요 데이터를 창업 입지·물류 거점 판단 제품으로 만든 개인 데이터·AI 프로젝트 Case Study.',
        'url': f'{BASE}/projects/procurement-logistics-ai.html',
        'image': f'{BASE}/assets/og/procurement-logistics-ai.png',
        'type': 'article',
    },
}


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if old not in text:
        raise RuntimeError(f'missing expected text for {label}: {old[:100]}')
    return text.replace(old, new, 1)


def factual_fixes() -> None:
    # Main page: make project-level RAG metrics precise and remove live-view row count ambiguity.
    p = ROOT / 'index.html'
    s = p.read_text(encoding='utf-8')
    s = s.replace('Job contamination rate', 'RAG job contamination')
    s = s.replace('직무 추천 데이터 오염을 추적해 0%까지 개선.', 'RAG top-1 직무 오염률을 재분류 기준으로 검증해 0%로 정정.')
    s = s.replace('contamination <b>12.5% → 0%</b>', 'RAG contamination <b>12.5% → 0%</b>')
    s = s.replace('evidence <b>100%</b>', 'RAG evidence <b>95% → 100%</b>')
    s = s.replace('<div class="dashboard-badges"><span>LIVE DATA</span><span>전국 지도</span><span>93,971 공고</span></div>', '<div class="dashboard-badges"><span>LIVE DATA</span><span>전국 지도</span><span>FILTERED VIEW</span></div>')
    p.write_text(s, encoding='utf-8')

    # Jobiverse: distinguish retrieval metrics from recommendation/report metrics.
    p = ROOT / 'projects/jobiverse.html'
    s = p.read_text(encoding='utf-8')
    s = s.replace('<small>job contamination</small><strong>12.5% → 0%</strong><p>추천 데이터 직무 오염 제거</p>', '<small>RAG job contamination</small><strong>12.5% → 0%</strong><p>top-1 직무 오염률 · 동등 청크 재분류</p>')
    s = s.replace('<small>evidence coverage</small><strong>100%</strong><p>리포트 근거 포함률</p>', '<small>RAG evidence coverage</small><strong>95% → 100%</strong><p>추천 적중 시 정답 근거 포함률</p>')
    s = s.replace('<span>직무 추천 데이터 contamination rate</span>', '<span>RAG top-1 직무 오염률</span>')
    s = s.replace('<strong>95% → <em>100%</em></strong><span>정답 근거 포함률</span>', '<strong>95% → <em>100%</em></strong><span>추천 적중 시 RAG 정답 근거 포함률</span>')
    s = s.replace('직무 추천 데이터 오염, 근거 누락, 임베딩 지연처럼 실제 서비스 품질을 떨어뜨리는 지점을 지표로 잡아 반복 검증했습니다.', 'RAG 검색의 직무 오염, 정답 근거 누락, 임베딩 지연처럼 실제 서비스 품질을 떨어뜨리는 지점을 지표로 잡아 반복 검증했습니다.')
    p.write_text(s, encoding='utf-8')

    # SchoolBridge: screenshots are browser-rendered design_reference assets, not APK captures.
    p = ROOT / 'projects/schoolbridge.html'
    s = p.read_text(encoding='utf-8')
    s = s.replace('SERVICE UI · PARENT APP', 'DESIGN REFERENCE · PARENT FLOW')
    s = s.replace('alt="SchoolBridge 학부모 앱 화면"', 'alt="SchoolBridge 학부모 UI 디자인 레퍼런스"')
    s = s.replace('<h2>선생님과 학부모의<br>실제 서비스 흐름.</h2>', '<h2>선생님과 학부모의<br>UI 흐름을 시안으로 정리했습니다.</h2>')
    s = s.replace('선생님은 통신문을 보내고, 학부모는 수신한 공지를 AI로 분석해 체크리스트·번역·음성 안내를 확인합니다.', '저장소의 android/design_reference UI 시안을 브라우저로 렌더링한 화면입니다. 실제 실기기 E2E 검증은 별도로 수행했고, 아래 이미지는 화면 구조를 보여주는 디자인 레퍼런스입니다.')
    s = s.replace('PARENT APP · TRANSLATION / CHECKLIST', 'PARENT UI REFERENCE · TRANSLATION / CHECKLIST')
    s = s.replace('TEACHER APP · NOTICE SEND', 'TEACHER UI REFERENCE · NOTICE SEND')
    s = s.replace('alt="SchoolBridge 학부모 앱"', 'alt="SchoolBridge 학부모 UI 디자인 레퍼런스"')
    s = s.replace('alt="SchoolBridge 선생님 앱"', 'alt="SchoolBridge 선생님 UI 디자인 레퍼런스"')
    p.write_text(s, encoding='utf-8')

    # Rainbow Bridge: avoid claiming another teammate's HTTPS/domain implementation as personal ownership.
    p = ROOT / 'projects/rainbow-bridge.html'
    s = p.read_text(encoding='utf-8')
    s = s.replace('NCP, nginx, HTTPS, Docker Compose, GitHub Actions 기반 시연 환경 운용', 'NCP 서버 운영 · Docker Compose · GitHub Actions 기반 시연 환경 운용')
    p.write_text(s, encoding='utf-8')

    # Procurement: use the documented outcome wording and clarify raw-vs-live counts.
    p = ROOT / 'projects/procurement-logistics-ai.html'
    s = p.read_text(encoding='utf-8')
    s = s.replace('<span class="badge gold">PUBLIC CONTEST FINALIST</span>', '<span class="badge gold">PUBLIC CONTEST · FACE-TO-FACE REVIEW</span>')
    s = s.replace('<p>최근 2년 전국 입찰공고</p>', '<p>최근 2년 전국 수집 원본 기준</p>')
    s = s.replace('<span>전국 17개 시·도 최근 2년 나라장터 입찰공고</span>', '<span>전국 17개 시·도 최근 2년 나라장터 입찰공고 · 수집 원본 기준</span>')
    p.write_text(s, encoding='utf-8')


def seo_block(meta: dict, is_index: bool) -> str:
    favicon = '/assets/favicon.svg'
    preconnect = '<link rel="preconnect" href="https://raw.githubusercontent.com" crossorigin>'
    author = '<meta name="author" content="모세종">'
    canonical = f'<link rel="canonical" href="{meta["url"]}">'
    icon = f'<link rel="icon" href="{favicon}" type="image/svg+xml">'
    social = ''.join([
        f'<meta property="og:type" content="{meta["type"]}">',
        f'<meta property="og:url" content="{meta["url"]}">',
        f'<meta property="og:image" content="{meta["image"]}">',
        '<meta property="og:image:width" content="1200">',
        '<meta property="og:image:height" content="630">',
        '<meta property="og:locale" content="ko_KR">',
        '<meta name="twitter:card" content="summary_large_image">',
        f'<meta name="twitter:title" content="{meta["title"]}">',
        f'<meta name="twitter:description" content="{meta["description"]}">',
        f'<meta name="twitter:image" content="{meta["image"]}">',
    ])
    if is_index:
        data = {
            '@context': 'https://schema.org',
            '@type': 'Person',
            'name': '모세종',
            'url': f'{BASE}/',
            'sameAs': ['https://github.com/mosejong'],
            'jobTitle': 'AI Service Backend Developer',
            'knowsAbout': ['Python', 'FastAPI', 'PostgreSQL', 'Redis', 'RAG', 'LLM Integration', 'Docker', 'pytest', 'GitHub Actions'],
        }
    else:
        data = {
            '@context': 'https://schema.org',
            '@type': 'CreativeWork',
            'name': meta['title'].split(' | ')[0],
            'author': {'@type': 'Person', 'name': '모세종', 'url': f'{BASE}/'},
            'url': meta['url'],
            'image': meta['image'],
            'description': meta['description'],
        }
    structured = '<script type="application/ld+json">' + json.dumps(data, ensure_ascii=False, separators=(',', ':')) + '</script>'
    return author + canonical + icon + preconnect + social + structured


def apply_seo() -> None:
    for rel, meta in PAGES.items():
        p = ROOT / rel
        s = p.read_text(encoding='utf-8')
        # Normalize description/title/OG text already present.
        s = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{meta["description"]}">', s, count=1)
        s = re.sub(r'<meta property="og:title" content="[^"]*">', f'<meta property="og:title" content="{meta["title"]}">', s, count=1)
        s = re.sub(r'<meta property="og:description" content="[^"]*">', f'<meta property="og:description" content="{meta["description"]}">', s, count=1)
        s = re.sub(r'<title>[^<]*</title>', f'<title>{meta["title"]}</title>', s, count=1)
        # Remove a prior v1.1 block if the script is rerun.
        s = re.sub(r'<!-- SEO_V11_START -->.*?<!-- SEO_V11_END -->', '', s, flags=re.S)
        block = '<!-- SEO_V11_START -->' + seo_block(meta, rel == 'index.html') + '<!-- SEO_V11_END -->'
        s = s.replace('</head>', block + '</head>', 1)
        p.write_text(s, encoding='utf-8')


def write_favicon() -> None:
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#f6f9fc"/><stop offset=".58" stop-color="#8cf5d2"/><stop offset="1" stop-color="#82d7ff"/></linearGradient></defs>
<rect width="64" height="64" rx="16" fill="#070a0f"/><rect x="1" y="1" width="62" height="62" rx="15" fill="none" stroke="#ffffff" stroke-opacity=".14"/>
<path d="M16 43V21h7.2l8.8 12.4L40.8 21H48v22h-7V31.5l-8.7 11.7h-.7L23 31.5V43z" fill="url(#g)"/>
</svg>'''
    (ROOT / 'assets/favicon.svg').write_text(svg, encoding='utf-8')


def font_path(bold: bool = False) -> str:
    candidates = [
        '/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc' if bold else '/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc',
        '/usr/share/fonts/truetype/noto/NotoSansCJK-Bold.ttc' if bold else '/usr/share/fonts/truetype/noto/NotoSansCJK-Regular.ttc',
        '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf' if bold else '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',
    ]
    for c in candidates:
        if Path(c).exists():
            return c
    raise FileNotFoundError('No usable font found')


def fit_font(draw: ImageDraw.ImageDraw, text: str, max_width: int, start: int, minimum: int = 42):
    size = start
    while size >= minimum:
        f = ImageFont.truetype(font_path(True), size)
        if draw.textbbox((0,0), text, font=f)[2] <= max_width:
            return f
        size -= 2
    return ImageFont.truetype(font_path(True), minimum)


def draw_og(path: Path, kicker: str, title: str, subtitle: str, metrics: list[tuple[str,str]]) -> None:
    W, H = 1200, 630
    im = Image.new('RGB', (W,H), '#070a0f')
    d = ImageDraw.Draw(im)
    # grid
    for x in range(0, W, 64): d.line((x,0,x,H), fill='#101722', width=1)
    for y in range(0, H, 64): d.line((0,y,W,y), fill='#101722', width=1)
    # glows (simple concentric rings)
    for r in range(260, 10, -10):
        a = max(0, int(28 * (1-r/260)))
        col = (10, 28 + a, 28 + a)
        d.ellipse((930-r, -40-r, 930+r, -40+r), outline=col, width=8)
    # top brand
    mono = ImageFont.truetype(font_path(True), 22)
    d.rounded_rectangle((58,54,108,104), radius=13, fill='#eef3f7')
    d.text((68,69), 'MS', font=ImageFont.truetype(font_path(True), 20), fill='#070a0f')
    d.text((126,67), 'MOSEJONG  ·  AI BACKEND DEVELOPER', font=mono, fill='#9aa6b7')
    d.text((60,145), kicker, font=ImageFont.truetype(font_path(True), 20), fill='#8cf5d2')
    title_font = fit_font(d, title, 780, 78, 54)
    d.text((58,188), title, font=title_font, fill='#f7f9fc')
    sub_font = ImageFont.truetype(font_path(False), 29)
    # wrap subtitle manually by width
    words = subtitle.split(' ')
    lines, cur = [], ''
    for w in words:
        test = (cur + ' ' + w).strip()
        if d.textbbox((0,0), test, font=sub_font)[2] > 760 and cur:
            lines.append(cur); cur = w
        else: cur = test
    if cur: lines.append(cur)
    yy = 305
    for line in lines[:2]:
        d.text((62,yy), line, font=sub_font, fill='#a1adbd'); yy += 44
    # metric cards
    card_y = 452
    card_w = 250
    gap = 14
    for i,(label,value) in enumerate(metrics[:4]):
        x = 58 + i*(card_w+gap)
        d.rounded_rectangle((x,card_y,x+card_w,570), radius=20, fill='#0d131b', outline='#28313d', width=1)
        d.text((x+18,card_y+17), label.upper(), font=ImageFont.truetype(font_path(True), 15), fill='#728094')
        vf = fit_font(d, value, card_w-36, 32, 24)
        d.text((x+18,card_y+51), value, font=vf, fill='#f3f7fb')
    d.text((60,594), 'mosejong.github.io', font=ImageFont.truetype(font_path(True), 17), fill='#667386')
    path.parent.mkdir(parents=True, exist_ok=True)
    im.save(path, 'PNG', optimize=True)


def generate_og() -> None:
    draw_og(ROOT/'assets/og/portfolio.png', 'PORTFOLIO · 2026', '운영의 감각을 백엔드의 구조로.', 'Python · FastAPI로 API, DB, AI를 연결하고 테스트와 수치로 검증합니다.', [('CAREER','8Y 9M'),('PROJECT','GRAND PRIZE'),('BACKEND','FASTAPI'),('QUALITY','TEST · CI')])
    draw_og(ROOT/'assets/og/jobiverse.png', 'CASE STUDY · JOBIVERSE', 'AI 상담에서 근거 기반 리포트까지', 'Reporting · Data Pipeline · Career Experience Platform', [('RAG CONTAM.','12.5% → 0%'),('RAG EVIDENCE','95% → 100%'),('SCENARIOS','37'),('TESTS','564')])
    draw_og(ROOT/'assets/og/schoolbridge.png', 'CASE STUDY · SCHOOLBRIDGE', '핵심정보를 보존하는 다국어 가정통신문 AI', 'NLLB · School Glossary · Edge-TTS · Real-device E2E', [('QUALITY','39.0 → 89.6'),('LANGUAGES','8'),('BACKEND TEST','27'),('AWARD','BEST PROJECT')])
    draw_og(ROOT/'assets/og/rainbow-bridge.png', 'CASE STUDY · RAINBOW BRIDGE', 'AI 펫로스 애프터케어 서비스', 'Team Lead · Backend Integration · NCP · Docker', [('SAFETY','40 / 40'),('G-EVAL','4.76–4.83'),('LIP-SYNC','0.896'),('TEAM','6 PEOPLE')])
    draw_og(ROOT/'assets/og/procurement-logistics-ai.png', 'CASE STUDY · PROCUREMENT LOGISTICS AI', '공공수요를 입지·물류 판단 데이터 제품으로', '6기관 9소스 · Public Data · ML · Gemini · Streamlit', [('G2B BIDS','100,083'),('aT BID/AWARD','734,242'),('CLASSIFIER','98.6%'),('REGIONS','220')])


def write_discovery_files() -> None:
    (ROOT/'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: https://mosejong.github.io/sitemap.xml\n', encoding='utf-8')
    urls = [v['url'] for v in PAGES.values()]
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(f'  <url><loc>{u}</loc></url>\n' for u in urls) + '</urlset>\n'
    (ROOT/'sitemap.xml').write_text(xml, encoding='utf-8')


class LocalRefParser(HTMLParser):
    def __init__(self):
        super().__init__(); self.refs=[]
    def handle_starttag(self, tag, attrs):
        a=dict(attrs)
        for key in ('href','src'):
            if key in a: self.refs.append(a[key])


def validate() -> None:
    errors=[]
    required_meta = ['canonical','og:image','twitter:card','favicon.svg']
    for rel in PAGES:
        p=ROOT/rel
        s=p.read_text(encoding='utf-8')
        for term in required_meta:
            if term not in s: errors.append(f'{rel}: missing {term}')
        parser=LocalRefParser(); parser.feed(s)
        for ref in parser.refs:
            if not ref or ref.startswith(('#','http://','https://','mailto:','data:','javascript:')):
                continue
            clean=ref.split('#',1)[0].split('?',1)[0]
            if not clean: continue
            target=(p.parent/clean).resolve()
            try: target.relative_to(ROOT.resolve())
            except ValueError: continue
            if not target.exists(): errors.append(f'{rel}: missing local target {ref}')
    for f in ['assets/favicon.svg','assets/og/portfolio.png','assets/og/jobiverse.png','assets/og/schoolbridge.png','assets/og/rainbow-bridge.png','assets/og/procurement-logistics-ai.png','robots.txt','sitemap.xml']:
        if not (ROOT/f).exists(): errors.append(f'missing generated {f}')
    # guard corrected factual wording
    idx=(ROOT/'index.html').read_text(encoding='utf-8')
    if 'RAG evidence <b>95% → 100%</b>' not in idx: errors.append('index RAG evidence correction missing')
    sb=(ROOT/'projects/schoolbridge.html').read_text(encoding='utf-8')
    if 'design_reference' not in sb: errors.append('SchoolBridge design reference disclosure missing')
    rb=(ROOT/'projects/rainbow-bridge.html').read_text(encoding='utf-8')
    if 'NCP, nginx, HTTPS, Docker Compose' in rb: errors.append('Rainbow ownership overclaim still present')
    pc=(ROOT/'projects/procurement-logistics-ai.html').read_text(encoding='utf-8')
    if 'PUBLIC CONTEST FINALIST' in pc: errors.append('Procurement finalist overstatement still present')
    if errors:
        raise SystemExit('\n'.join(errors))
    print('VALIDATION PASS')


if __name__ == '__main__':
    factual_fixes()
    write_favicon()
    generate_og()
    apply_seo()
    write_discovery_files()
    validate()
