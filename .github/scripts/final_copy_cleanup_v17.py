from pathlib import Path

changes = {
    "index.html": [
        ('<meta property="og:title" content="모세종 | Python · FastAPI AI Backend Developer" />', '<meta property="og:title" content="모세종 | Python · FastAPI AI 서비스 백엔드 개발자" />'),
        ('<title>모세종 | Python · FastAPI AI Backend Developer</title>', '<title>모세종 | Python · FastAPI AI 서비스 백엔드 개발자</title>'),
        ('<meta name="twitter:title" content="모세종 | Python · FastAPI AI Backend Developer">', '<meta name="twitter:title" content="모세종 | Python · FastAPI AI 서비스 백엔드 개발자">'),
        ('"jobTitle":"AI Service Backend Developer"', '"jobTitle":"Python · FastAPI AI 서비스 백엔드 개발자"'),
        ('<span>Seoul · AI Service Backend</span>', '<span>Seoul · AI 서비스 백엔드 개발자</span>'),
        ('<span class="tag gold">🏆 BEST PROJECT</span>', '<span class="tag gold">🏆 최우수상</span>'),
        ('<div class="time-year">2013—2026</div><div class="time-dot"></div>\n              <div class="time-content"><strong>자동차 부품 물류 · 운영 · 누적 8년 9개월</strong>', '<div class="time-year">누적 8Y 9M</div><div class="time-dot"></div>\n              <div class="time-content"><strong>자동차 부품 물류 · 운영</strong>'),
    ],
    "projects/schoolbridge.html": [
        ('<span class="badge gold">🏆 BEST PROJECT</span>', '<span class="badge gold">🏆 최우수상</span>'),
    ],
    "projects/jobiverse.html": [
        ('<h3>직무군 ↔ 시나리오 1:1</h3><p>추천 카드에서 바로 체험으로 입장할 수 있도록 직무군과 시나리오를 직접 매핑했습니다. 38개 직무군 중 37개 시나리오를 연결했습니다.</p>', '<h3>37개 체험 시나리오 직접 매핑</h3><p>추천 카드에서 바로 체험으로 입장할 수 있도록 시나리오가 구성된 37개 직무군을 각 체험 시나리오와 1:1로 매핑했습니다. 전체 추천 체계는 38개 직무군을 유지합니다.</p>'),
    ],
}

for filename, replacements in changes.items():
    path = Path(filename)
    text = path.read_text(encoding="utf-8")
    for old, new in replacements:
        if old not in text:
            raise SystemExit(f"Missing expected text in {filename}: {old[:100]}")
        text = text.replace(old, new, 1)
    path.write_text(text, encoding="utf-8")

# Assertions: old ambiguity/stale labels must be gone from targeted places.
root = Path("index.html").read_text(encoding="utf-8")
school = Path("projects/schoolbridge.html").read_text(encoding="utf-8")
job = Path("projects/jobiverse.html").read_text(encoding="utf-8")

assert "🏆 BEST PROJECT" not in root
assert "🏆 BEST PROJECT" not in school
assert '<div class="time-year">2013—2026</div>' not in root
assert "AI Service Backend Developer" not in root
assert "Seoul · AI Service Backend</span>" not in root
assert "직무군 ↔ 시나리오 1:1" not in job
assert "37개 체험 시나리오 직접 매핑" in job
assert "전체 추천 체계는 38개 직무군" in job

print("FINAL COPY CLEANUP PASS")
