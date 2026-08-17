from pathlib import Path
import re

index_path = Path('index.html')
text = index_path.read_text(encoding='utf-8')

# 1) Add How I Work scan strip before the existing impact bento.
needle = '''          <p class="section-note">사용한 기술보다, 무엇을 개선했고 어떤 기준으로 검증했는지를 먼저 보여줍니다.</p>\n        </div>\n\n        <div class="bento">'''
replacement = '''          <p class="section-note">사용한 기술보다, 무엇을 개선했고 어떤 기준으로 검증했는지를 먼저 보여줍니다.</p>\n        </div>\n\n        <div class="work-principles reveal" aria-label="개발 방식 요약">\n          <div class="work-principle"><small>01 · STRUCTURE</small><strong>문제를 구조화합니다.</strong><span>운영에서 흐름과 병목을 보던 방식으로 API·DB·데이터 흐름을 정리합니다.</span></div>\n          <div class="work-principle"><small>02 · VERIFY</small><strong>수치로 확인합니다.</strong><span>성능·품질·안전·회귀 조건을 테스트와 지표로 확인합니다.</span></div>\n          <div class="work-principle"><small>03 · CONNECT</small><strong>끝까지 연결합니다.</strong><span>AI 기능을 단독 데모로 두지 않고 실제 사용자 흐름과 서비스 동작으로 연결합니다.</span></div>\n        </div>\n\n        <div class="bento">'''
if text.count(needle) != 1:
    raise SystemExit(f'impact insertion point mismatch: {text.count(needle)}')
text = text.replace(needle, replacement)

# 2) Add large background numbering to the four project cards.
pattern = re.compile(r'<article class="(project[^\"]*)">')
matches = list(pattern.finditer(text))
if len(matches) != 4:
    raise SystemExit(f'expected 4 project articles, got {len(matches)}')
idx = 0
def add_index(m):
    global idx
    idx += 1
    return f'<article class="{m.group(1)}" data-index="{idx:02d}">'
text = pattern.sub(add_index, text)

# 3) Replace dense role/detail blocks with 3-second scan summaries.
blocks = [
('''                <div class="role-grid">\n                  <div class="role-box"><small>MY ROLE</small><strong>Reporting · Data Pipeline</strong></div>\n                  <div class="role-box"><small>STACK</small><strong>FastAPI · PostgreSQL · pgvector</strong></div>\n                  <div class="role-box wide"><small>WHAT I OWNED</small><strong>역량 레이더 · AI 해석 · 근거 각주 · PDF · 공공 API · CI</strong></div>\n                </div>\n\n                <div class="project-metrics">\n                  <span class="metric">RAG contamination <b>12.5% → 0%</b></span>\n                  <span class="metric">embedding p90 <b>1.3s → 0.4s</b></span>\n                  <span class="metric">RAG evidence <b>95% → 100%</b></span>\n                  <span class="metric">project tests <b>564</b></span>\n                </div>''',
'''                <div class="role-grid scan-grid">\n                  <div class="role-box"><small>MY ROLE</small><strong>Reporting · Data Pipeline</strong></div>\n                  <div class="role-box signal"><small>KEY RESULT</small><strong>RAG top-1 오염률 12.5% → 0%</strong></div>\n                  <div class="role-box proof"><small>VALIDATION</small><strong>564 project backend tests</strong></div>\n                </div>\n\n                <div class="project-metrics supporting-metrics">\n                  <span class="metric">embedding p90 <b>1.3s → 0.4s</b></span>\n                  <span class="metric">RAG evidence <b>95% → 100%</b></span>\n                  <span class="metric">stack <b>FastAPI · PostgreSQL · pgvector</b></span>\n                </div>'''),
('''      <div class="role-grid">\n        <div class="role-box"><small>MY ROLE</small><strong>Translation · TTS Pipeline</strong></div>\n        <div class="role-box"><small>STACK</small><strong>NLLB · Transformers · Edge-TTS</strong></div>\n        <div class="role-box wide"><small>WHAT I OWNED</small><strong>8개 언어 번역 · 학교 용어사전 · 핵심정보 보존 · Round-trip 검수 · 음성 출력</strong></div>\n      </div>\n      <div class="project-metrics">\n        <span class="metric">quality <b>39.0 → 89.6</b></span>\n        <span class="metric">languages <b>8</b></span>\n        <span class="metric">backend tests <b>27</b></span>\n        <span class="metric"><b>실기기 E2E 검증</b></span>\n      </div>''',
'''      <div class="role-grid scan-grid">\n        <div class="role-box"><small>MY ROLE</small><strong>Translation · TTS Pipeline</strong></div>\n        <div class="role-box signal"><small>KEY RESULT</small><strong>번역 품질 39.0 → 89.6</strong></div>\n        <div class="role-box proof"><small>VALIDATION</small><strong>Android 실기기 E2E</strong></div>\n      </div>\n      <div class="project-metrics supporting-metrics">\n        <span class="metric">languages <b>8</b></span>\n        <span class="metric">project backend tests <b>27</b></span>\n        <span class="metric">stack <b>NLLB · Transformers · Edge-TTS</b></span>\n      </div>'''),
('''      <div class="role-grid">\n        <div class="role-box"><small>MY ROLE</small><strong>Team Lead · Backend Integration</strong></div>\n        <div class="role-box"><small>STACK</small><strong>FastAPI · NCP · Docker · nginx</strong></div>\n        <div class="role-box wide"><small>WHAT I OWNED</small><strong>우선순위 조율 · API 흐름 통합 · 서버 운영 · CI/CD · Expo 모바일 시연</strong></div>\n      </div>\n      <div class="project-metrics">\n        <span class="metric">team safety routing <b>40/40</b></span>\n        <span class="metric">team G-Eval <b>4.76–4.83 / 5</b></span>\n        <span class="metric">team lip-sync <b>0.896</b></span>\n        <span class="metric"><b>6-person team</b></span>\n      </div>''',
'''      <div class="role-grid scan-grid">\n        <div class="role-box"><small>MY ROLE</small><strong>Team Lead · Backend Integration</strong></div>\n        <div class="role-box signal"><small>KEY RESULT</small><strong>핵심 API · 회복 흐름 통합</strong></div>\n        <div class="role-box proof"><small>TEAM VALIDATION</small><strong>Safety routing 40 / 40</strong></div>\n      </div>\n      <div class="project-metrics supporting-metrics">\n        <span class="metric">team G-Eval <b>4.76–4.83 / 5</b></span>\n        <span class="metric">team lip-sync <b>0.896</b></span>\n        <span class="metric">stack <b>FastAPI · NCP · Docker · nginx</b></span>\n      </div>'''),
('''      <div class="role-grid">\n        <div class="role-box"><small>MY ROLE</small><strong>Solo Product · Data Pipeline</strong></div>\n        <div class="role-box"><small>STACK</small><strong>Python · Pandas · Scikit-learn · Streamlit</strong></div>\n        <div class="role-box wide"><small>WHAT I OWNED</small><strong>6개 기관 9개 소스 · 전국 수요 분석 · TF-IDF/LogReg · Gemini 해석 · 물류 거점 지표</strong></div>\n      </div>\n      <div class="project-metrics">\n        <span class="metric">bids <b>100,083</b></span>\n        <span class="metric">aT bid/award <b>734,242</b></span>\n        <span class="metric">classification accuracy <b>98.6%</b></span>\n        <span class="metric"><b>대면심사 진출</b></span>\n      </div>''',
'''      <div class="role-grid scan-grid">\n        <div class="role-box"><small>MY ROLE</small><strong>Solo Product · Data Pipeline</strong></div>\n        <div class="role-box signal"><small>KEY RESULT</small><strong>Classification accuracy 98.6%</strong></div>\n        <div class="role-box proof"><small>VALIDATION</small><strong>100,083 G2B bid records</strong></div>\n      </div>\n      <div class="project-metrics supporting-metrics">\n        <span class="metric">aT bid + award <b>734,242</b></span>\n        <span class="metric">data sources <b>6 agencies / 9 sources</b></span>\n        <span class="metric">stack <b>Python · Pandas · Scikit-learn · Streamlit</b></span>\n      </div>''')]

for old, new in blocks:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f'project summary block mismatch: {count} | {old[:80]!r}')
    text = text.replace(old, new)

# 4) Append scanability CSS to the home page.
css = r'''

    /* v1.6 — recruiter scanability */
    .work-principles{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin:-2px 0 22px}
    .work-principle{min-height:150px;padding:19px 20px;border:1px solid rgba(255,255,255,.09);border-radius:20px;background:linear-gradient(145deg,rgba(255,255,255,.045),rgba(255,255,255,.022));position:relative;overflow:hidden}
    .work-principle:after{content:"";position:absolute;width:150px;height:150px;right:-72px;bottom:-88px;border-radius:50%;background:radial-gradient(circle,rgba(130,215,255,.10),transparent 67%)}
    .work-principle small{display:block;color:var(--mint);font:800 9px ui-monospace,SFMono-Regular,Menlo,monospace;letter-spacing:.11em;margin-bottom:18px}
    .work-principle strong{display:block;font-size:17px;letter-spacing:-.035em;margin-bottom:8px}
    .work-principle span{display:block;color:#8794a5;font-size:12px;line-height:1.65;max-width:290px}
    .project:before{content:attr(data-index);position:absolute;z-index:1;right:52%;top:13px;font:900 86px/1 Inter,Pretendard,"Noto Sans KR",sans-serif;letter-spacing:-.08em;color:rgba(255,255,255,.035);pointer-events:none;user-select:none}
    .scan-grid{grid-template-columns:repeat(3,minmax(0,1fr));gap:8px}
    .scan-grid .role-box{min-height:86px;padding:13px 12px;display:flex;flex-direction:column;justify-content:space-between}
    .scan-grid .role-box.wide{grid-column:auto}
    .scan-grid .role-box small{margin-bottom:10px}
    .scan-grid .role-box strong{font-size:11px;line-height:1.45}
    .scan-grid .role-box.signal{border-color:rgba(140,245,210,.16);background:rgba(140,245,210,.035)}
    .scan-grid .role-box.signal small,.scan-grid .role-box.signal strong{color:#b9f7e3}
    .scan-grid .role-box.proof{border-color:rgba(130,215,255,.16);background:rgba(130,215,255,.032)}
    .scan-grid .role-box.proof small{color:#79a8c3}.scan-grid .role-box.proof strong{color:#d7edf8}
    .supporting-metrics{margin-top:15px}
    @media(max-width:980px){.project:before{right:24px;top:18px}.work-principles{grid-template-columns:1fr 1fr}.work-principle:last-child{grid-column:span 2}}
    @media(max-width:680px){.work-principles{grid-template-columns:1fr}.work-principle:last-child{grid-column:auto}.work-principle{min-height:0}.scan-grid{grid-template-columns:1fr}.scan-grid .role-box{min-height:0}.project:before{font-size:68px;right:18px;top:13px}}
'''
if '/* v1.6 — recruiter scanability */' in text:
    raise SystemExit('v1.6 CSS already present')
if text.count('</style>') != 1:
    raise SystemExit('unexpected style tag count')
text = text.replace('</style>', css + '\n  </style>')
index_path.write_text(text, encoding='utf-8')

# 5) Make case-study result cards meaning-first: label before the number.
css_path = Path('assets/case-study.css')
case_css = css_path.read_text(encoding='utf-8')
case_patch = '''\n/* v1.6 — result scanability: meaning before number */\n.result{display:flex;flex-direction:column}\n.result span{order:-1;margin:0 0 11px;color:#7f8da0;font:800 10px/1.55 ui-monospace,SFMono-Regular,Menlo,monospace;letter-spacing:.045em}\n.result strong{order:0}\n'''
if 'result scanability: meaning before number' in case_css:
    raise SystemExit('case-study v1.6 CSS already present')
css_path.write_text(case_css + case_patch, encoding='utf-8')

# Sanity checks.
final = index_path.read_text(encoding='utf-8')
assert final.count('data-index=') == 4
assert final.count('KEY RESULT') == 4
assert '문제를 구조화합니다.' in final
assert '수치로 확인합니다.' in final
assert '끝까지 연결합니다.' in final
assert final.count('WHAT I OWNED') == 0
assert final.count('scan-grid') >= 5  # CSS + 4 project blocks
print('PORTFOLIO BENCHMARK SCAN V1.6 PASS')
