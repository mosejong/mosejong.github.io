# mosejong.github.io

모세종 | Python · FastAPI AI Backend Developer Portfolio

- Portfolio: https://mosejong.github.io
- GitHub: https://github.com/mosejong

## Portfolio v1.2

- 프로젝트 데모 GIF 3종을 로컬 MP4 + WebP poster로 전환
- 화면 근처에 들어온 데모 영상만 재생하고 화면 밖에서는 자동 pause
- `prefers-reduced-motion` 사용자는 자동 재생하지 않도록 처리
- SchoolBridge / Procurement 프로젝트 캡처 PNG를 WebP로 전환
- 대표 미디어 6종 합산 6.26 MiB → 731.8 KiB, 약 88.6% 감소
- 숨겨진 Awards 이미지와 하단 Case Study 이미지에 lazy loading / async decoding 적용
- Case Study 첫 화면 이미지는 fetch priority를 높이고 하단 이미지는 지연 로딩
- 키보드 사용자를 위한 `:focus-visible` 포커스 표시 추가
- 외부 raw GitHub 미디어 의존 제거 및 사이트 내부 자산으로 통일

## Portfolio v1.1

- 대표 프로젝트 4개 Case Study 페이지 제공
- 프로젝트 원본 저장소 기준 역할·성과 지표 문구 재검수
- Jobiverse RAG 오염률 / 근거 포함률 지표 의미 명확화
- SchoolBridge UI 이미지를 `design_reference` 기반 시안으로 명확히 표기
- Rainbow Bridge 개인 기여와 팀원 인프라 기여 범위 구분
- Procurement Logistics AI 공모전 결과를 `대면심사 진출` 수준으로 정확히 표기
- 메인 + Case Study별 1200×630 Open Graph 이미지
- favicon, canonical, Open Graph, Twitter Card, JSON-LD, robots.txt, sitemap.xml 추가
- PC / 모바일 반응형 프로젝트 및 Case Study 레이아웃 적용

## Awards panel

오른쪽 `AWARDS` 탭에서 상장·수료증을 확인할 수 있습니다.
공개용 수료증 이미지는 생년월일 영역을 비식별 처리했습니다.

## Deployment

`main` 브랜치 변경 시 `.github/workflows/pages.yml`을 통해 GitHub Pages로 자동 배포합니다.
