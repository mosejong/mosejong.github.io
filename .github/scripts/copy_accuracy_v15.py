from pathlib import Path

repls = {
    "index.html": [
        ("<span class=\"key\">deploy</span>: production ready", "<span class=\"key\">deploy</span>: demo ready"),
        ("실제 서비스 화면과 함께 내가 맡은 문제, 구현 범위, 검증 결과를 한 화면 안에서 확인할 수 있습니다.", "프로젝트 화면과 함께 맡은 문제, 구현 범위, 검증 결과를 한 화면에서 확인할 수 있습니다."),
        ("RAG top-1 직무 오염률을 재분류 기준으로 검증해 0%로 정정.", "재분류 기준을 적용해 RAG top-1 직무 오염률을 12.5%에서 0%로 낮췄습니다."),
        ("<div class=\"time-content\"><strong>자동차 부품 물류 · 운영</strong><p>입출고, 재고, 납기, 구매, 거래처 대응. 실무에서 병목과 우선순위를 판단.</p></div>", "<div class=\"time-content\"><strong>자동차 부품 물류 · 운영 · 누적 8년 9개월</strong><p>입출고, 재고, 납기, 구매, 거래처 대응. 실무에서 병목과 우선순위를 판단.</p></div>"),
        ("재고·납기·구매·출고를 운영하며 배운 우선순위와 검수 감각을 소프트웨어에 가져왔습니다. “왜 느리지?”, “어디서 잘못됐지?”, “근거가 있나?”를 끝까지 확인하는 개발자가 되려 합니다.", "재고·납기·구매·출고를 운영하며 배운 우선순위와 검수 감각을 소프트웨어에 가져왔습니다. “왜 느리지?”, “어디서 잘못됐지?”, “근거가 있나?”를 테스트·로그·지표로 확인합니다."),
        ("“되는 기능”에서 끝나지 않고<br><span class=\"hero-accent\">쓸 수 있는 서비스</span>를 만들겠습니다.", "기능 구현에서 끝내지 않고<br><span class=\"hero-accent\">쓸 수 있는 서비스</span>로 연결합니다."),
        ("AI를 붙이는 것보다, 그것이 사용자의 실제 흐름 안에서 안정적으로 동작하도록 만드는 백엔드 개발을 하고 싶습니다.", "AI 기능을 사용자의 실제 흐름에 연결하고, API·DB·검증까지 이어지는 백엔드를 구현합니다."),
        ("<span class=\"metric\">classifier <b>98.6%</b></span>", "<span class=\"metric\">classification accuracy <b>98.6%</b></span>"),
        ("<span class=\"metric\">safety routing <b>40/40</b></span>", "<span class=\"metric\">team safety routing <b>40/40</b></span>"),
        ("<span class=\"metric\">G-Eval <b>4.76–4.83 / 5</b></span>", "<span class=\"metric\">team G-Eval <b>4.76–4.83 / 5</b></span>"),
        ("<span class=\"metric\">lip-sync <b>0.896</b></span>", "<span class=\"metric\">team lip-sync <b>0.896</b></span>"),
    ],
    "projects/jobiverse.html": [
        ("AI와 상담하고 가상 회사에서 실제 업무를 체험한 뒤 <strong>행동 근거가 붙은 직무 적합도 리포트</strong>까지 이어지도록 만든 6인 팀 프로젝트입니다.", "AI와 상담하고 가상 회사에서 직무 과제를 수행한 뒤 <strong>행동 근거가 붙은 직무 적합도 리포트</strong>까지 이어지도록 만든 6인 팀 프로젝트입니다."),
        ("직무군·세부직업·시나리오 연결이 어긋나는 문제를 테스트와 GitHub Actions로 감시", "직무군·세부직업·시나리오 연결이 어긋나는 문제를 테스트와 GitHub Actions에서 자동 검증"),
    ],
    "projects/schoolbridge.html": [
        ("<h2>번역 품질을<br>39.0 → 89.6으로 개선했습니다.</h2>", "<h2>용어사전 적용 전후를<br>같은 기준으로 재평가했습니다.</h2>"),
    ],
    "projects/rainbow-bridge.html": [
        ("<small>safety routing</small><strong>40 / 40</strong>", "<small>team safety routing</small><strong>40 / 40</strong>"),
        ("<small>G-Eval quality</small><strong>4.76–4.83</strong>", "<small>team G-Eval quality</small><strong>4.76–4.83</strong>"),
        ("<small>lip-sync corr.</small><strong>0.896</strong>", "<small>team lip-sync corr.</small><strong>0.896</strong>"),
        ("<h2>위로 한 문장보다<br>시간에 따라 이어지는 케어가 필요했습니다.</h2>", "<h2>한 번의 위로가 아니라<br>상태 변화에 따라 이어지는 흐름으로 설계했습니다.</h2>"),
        ("<h2>시연 성공과 별도로<br>안전·윤리·대화 품질을 검증했습니다.</h2>", "<h2>프로젝트 전체 결과를<br>안전·윤리·대화 품질 지표로 확인했습니다.</h2>"),
        ("대화 품질뿐 아니라 안전 라우팅, 윤리 준수, TTS 정확도, 립싱크 성능을 별도 지표로 나눠 검증했습니다.", "팀 전체 결과에서 대화 품질, 안전 라우팅, 윤리 준수, TTS 정확도, 립싱크 성능을 별도 지표로 나눠 확인했습니다."),
    ],
    "projects/procurement-logistics-ai.html": [
        ("공공기관이 실제로 무엇을 사고 있는지", "공공기관이 무엇을 구매하려 하는지와 무엇이 실제 계약됐는지"),
        ("<h2>기획부터 수집·모델·지표·화면까지<br>혼자 끝까지 만들었습니다.</h2>", "<h2>개인 프로젝트로<br>기획부터 대시보드까지 직접 구현했습니다.</h2>"),
        ("<small>classifier</small><strong>98.6%</strong>", "<small>classification accuracy</small><strong>98.6%</strong>"),
    ],
}

for filename, pairs in repls.items():
    path = Path(filename)
    text = path.read_text(encoding="utf-8")
    for old, new in pairs:
        count = text.count(old)
        if count != 1:
            raise SystemExit(f"expected exactly 1 match in {filename}, got {count}: {old[:100]!r}")
        text = text.replace(old, new)
    path.write_text(text, encoding="utf-8")

checks = {
    "index.html": ["production ready", "개발자가 되려 합니다", "개발을 하고 싶습니다", "실제 서비스 화면과 함께"],
    "projects/jobiverse.html": ["실제 업무를 체험한 뒤", "GitHub Actions로 감시"],
    "projects/rainbow-bridge.html": ["시간에 따라 이어지는 케어가 필요했습니다"],
    "projects/procurement-logistics-ai.html": ["혼자 끝까지 만들었습니다", "실제로 무엇을 사고 있는지"],
}
for filename, banned in checks.items():
    text = Path(filename).read_text(encoding="utf-8")
    for phrase in banned:
        if phrase in text:
            raise SystemExit(f"banned phrase remains in {filename}: {phrase}")

print("COPY ACCURACY V1.5 PASS")
