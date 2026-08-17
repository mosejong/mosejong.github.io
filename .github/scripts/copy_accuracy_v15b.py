from pathlib import Path

path = Path("projects/schoolbridge.html")
text = path.read_text(encoding="utf-8")
repls = [
    ("<small>backend quality</small><strong>27 tests</strong>", "<small>project backend tests</small><strong>27 tests</strong>"),
    ("평가 기준을 단순 BLEU류 점수가 아니라 실제 사용자 관점의 학교 문맥·정보 보존·상용 표현까지 넓혀 개선 전후를 비교했습니다.", "평가 기준을 단순 BLEU류 점수가 아니라 학교 공지 사용 맥락의 문맥·정보 보존·상용 표현까지 넓혀 개선 전후를 비교했습니다."),
]
for old, new in repls:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"expected exactly 1 match, got {count}: {old}")
    text = text.replace(old, new)
path.write_text(text, encoding="utf-8")
print("COPY ACCURACY V1.5B PASS")
