from pathlib import Path

repls = {
    'index.html': [
        (
            '기술을 사용했다는 말보다 무엇이 개선됐고, 어떤 기준으로 검증했는지 보여주는 포트폴리오를 지향합니다.',
            '사용한 기술보다, 무엇을 개선했고 어떤 기준으로 검증했는지를 먼저 보여줍니다.'
        ),
        (
            '물류·운영 현장에서 <strong>8년 9개월</strong> 동안 재고·납기·구매·출고의 흐름을 다뤘습니다.\n            지금은 <strong>Python · FastAPI</strong>로 API, DB, AI 기능을 연결하고\n            <strong>테스트와 수치로 검증되는 서비스</strong>를 만듭니다.',
            '물류·운영 현장에서 <strong>8년 9개월</strong> 동안 재고·납기·구매·출고의 흐름을 다뤘습니다.\n            이 경험을 바탕으로 <strong>Python · FastAPI</strong>로 API, DB, AI 기능을 연결하고,\n            <strong>테스트와 지표로 개선 효과를 검증</strong>합니다.'
        ),
        (
            'AI 상담 → 가상 직무 체험 → 근거 기반 적합도 리포트로 이어지는 진로 탐색 플랫폼. 저는 <b style="color:#dfe7ef">리포트·추천 근거·외부 데이터·검증 흐름</b>을 맡았습니다.',
            'AI 상담 → 가상 직무 체험 → 근거 기반 적합도 리포트로 이어지는 진로 탐색 플랫폼. <b style="color:#dfe7ef">리포트·추천 근거·외부 데이터·검증 흐름</b>을 맡아 체험 결과를 설명 가능한 리포트로 연결했습니다.'
        ),
        (
            '가정통신문의 날짜·금액·준비물처럼 놓치면 안 되는 정보를 보존하면서 8개 언어 번역과 음성 안내로 연결한 서비스입니다. 저는 <b style="color:#dfe7ef">NLLB 번역·학교 용어사전·번역 검수 루프·Edge-TTS</b>를 담당했습니다.',
            '가정통신문의 날짜·금액·준비물처럼 놓치면 안 되는 정보를 보존하면서 8개 언어 번역과 음성 안내로 연결한 서비스입니다. <b style="color:#dfe7ef">NLLB 번역·학교 용어사전·번역 검수 루프·Edge-TTS</b>를 맡아 번역 품질을 39.0 → 89.6으로 개선했습니다.'
        ),
        (
            '감정 체크인 → 추모 메시지·TTS → 회복 미션 → 타임라인·리포트로 이어지는 AI 펫로스 애프터케어 서비스. 저는 <b style="color:#dfe7ef">팀 운영·API 통합·서버 배포·사용자 시연 흐름</b>을 맡았습니다.',
            '감정 체크인 → 추모 메시지·TTS → 회복 미션 → 타임라인·리포트로 이어지는 AI 펫로스 애프터케어 서비스. <b style="color:#dfe7ef">팀 운영·API 통합·서버 운영·사용자 시연 흐름</b>을 맡아 각 기능을 하나의 모바일 여정으로 연결했습니다.'
        ),
    ],
    'projects/jobiverse.html': [
        (
            '제 역할은 <strong>Reporting · Data Pipeline</strong>. 체험 결과를 사용자가 납득할 수 있는 결과물로 바꾸고, 추천과 외부 데이터를 연결하며, 데이터 정합성을 CI에서 계속 확인하는 영역을 맡았습니다.',
            '<strong>Reporting · Data Pipeline</strong>에서 체험 결과를 설명 가능한 리포트로 바꾸고, 추천·외부 데이터·CI 검증 흐름을 연결했습니다.'
        ),
        (
            '“AI가 좋다고 말해서”가 아니라, 상담에서 한 말과 체험에서 한 행동을 근거로 사용자가 자신의 결과를 이해할 수 있게 만드는 것이 목표였습니다.',
            '상담에서 한 말과 체험에서 한 행동을 근거로 연결해, 사용자가 점수의 이유를 직접 확인할 수 있게 했습니다.'
        ),
    ],
    'projects/schoolbridge.html': [
        (
            '번역만 잘해도<br>놓치면 안 되는 정보는 사라질 수 있습니다.',
            '문장이 자연스러워도<br>핵심 행동정보는 사라질 수 있습니다.'
        ),
        (
            '제 역할은 <strong>Translation · TTS Pipeline</strong>. NLLB 다국어 번역, 학교 용어사전, 번역 품질 검수 루프, Edge-TTS 음성 출력을 맡았습니다.',
            '<strong>Translation · TTS Pipeline</strong>에서 NLLB 다국어 번역, 학교 용어사전, 품질 검수 루프, Edge-TTS 음성 출력을 연결했습니다.'
        ),
        (
            '39점짜리 번역을<br>89.6점까지 끌어올렸습니다.',
            '번역 품질을<br>39.0 → 89.6으로 개선했습니다.'
        ),
    ],
    'projects/rainbow-bridge.html': [
        (
            'AI 펫로스 애프터케어 서비스의 Team Lead · Backend Integration 경험을 정리한 Rainbow Bridge Case Study.',
            '감정 체크인부터 추모 메시지·회복 미션·리포트까지 연결한 AI 펫로스 애프터케어 서비스. Team Lead · Backend Integration Case Study.'
        ),
        (
            '18일짜리 팀 프로젝트에서 중요한 것은 “할 수 있는 것”보다 <strong>발표 날 실제로 연결되어 동작하는 것</strong>을 정하는 일이었습니다.',
            '18일 안에 <strong>발표 날 실제로 연결되어 동작하는 흐름</strong>을 기준으로 기능 범위와 우선순위를 줄였습니다.'
        ),
        (
            '제 역할은 <strong>Team Lead · PM · Backend</strong>. 우선순위를 정하고 FastAPI API를 연결하며, 데이터 저장소와 회복 로직, 배포 환경, 최종 시연까지 전체 흐름을 책임졌습니다.',
            '<strong>Team Lead · PM · Backend</strong>로 우선순위를 정하고 FastAPI API, 데이터 저장소, 회복 로직, 배포 환경, 최종 시연 흐름을 연결했습니다.'
        ),
        (
            '민감한 서비스일수록<br>시연보다 평가 기준이 중요했습니다.',
            '시연 성공과 별도로<br>안전·윤리·대화 품질을 검증했습니다.'
        ),
    ],
    'projects/procurement-logistics-ai.html': [
        (
            '“어디에 수요가 있는가?”를<br>감이 아니라 데이터로 보고 싶었습니다.',
            '“어디에 수요가 있는가?”를<br>감이 아니라 데이터로 비교했습니다.'
        ),
        (
            '물류 현장에서 하던 “수요가 어디에 몰리는지, 납품은 가능한지, 거점은 어디가 유리한지”라는 질문을 코드와 공공데이터로 다시 풀어본 프로젝트입니다.',
            '물류 현장의 수요·납품·거점 판단을 공공데이터 지표와 분석 화면으로 옮겼습니다.'
        ),
        (
            '수집 스크립트부터<br>대시보드까지 재현 가능한 파이프라인.',
            '수집부터 대시보드까지<br>재현 가능한 파이프라인으로 구성했습니다.'
        ),
        (
            '데이터 규모와 모델 성능을<br>둘 다 확인했습니다.',
            '데이터 규모와 모델 성능을<br>함께 검증했습니다.'
        ),
    ],
}

for filename, pairs in repls.items():
    path = Path(filename)
    text = path.read_text(encoding='utf-8')
    for old, new in pairs:
        count = text.count(old)
        if count < 1:
            raise SystemExit(f'missing copy in {filename}: {old[:80]!r}')
        text = text.replace(old, new)
    path.write_text(text, encoding='utf-8')

joined = '\n'.join(Path(p).read_text(encoding='utf-8') for p in repls)
assert '포트폴리오를 지향합니다' not in joined
assert '보고 싶었습니다' not in Path('projects/procurement-logistics-ai.html').read_text(encoding='utf-8')
assert '경험을 정리한 Rainbow Bridge Case Study' not in Path('projects/rainbow-bridge.html').read_text(encoding='utf-8')
print('COPY POLISH V1.4 PASS')
