from pathlib import Path

# Home: turn the duplicate How I Work bento into a field-to-backend bridge.
p=Path('index.html')
t=p.read_text(encoding='utf-8')
old='''          <div class="bento-card workstyle reveal">\n            <div>\n              <div class="bento-label">How I work</div>\n              <div class="steps">\n                <div class="step"><i>01</i> 문제를 데이터 흐름으로 정리</div>\n                <div class="step"><i>02</i> API · DB · AI 기능 연결</div>\n                <div class="step"><i>03</i> 테스트 · 로그 · 수치로 검증</div>\n              </div>\n            </div>\n          </div>'''
new='''          <div class="bento-card workstyle reveal">\n            <div>\n              <div class="bento-label">Field → Backend</div>\n              <div class="steps">\n                <div class="step"><i>01</i> 재고 · 납기 → 상태 · 우선순위</div>\n                <div class="step"><i>02</i> 거래처 대응 → 사용자 흐름 · API</div>\n                <div class="step"><i>03</i> 검수 습관 → 테스트 · 로그 · 지표</div>\n              </div>\n            </div>\n          </div>'''
if t.count(old)!=1: raise SystemExit(f'home bridge mismatch: {t.count(old)}')
t=t.replace(old,new)
p.write_text(t,encoding='utf-8')

# Case studies: keep Korean headings from breaking into isolated syllables on desktop.
p=Path('assets/case-study.css')
t=p.read_text(encoding='utf-8')
patch='''\n/* v1.6b — Korean case-study heading fit */\n.section h2{word-break:keep-all}\n@media(min-width:901px){\n  .section-head{grid-template-columns:1fr 1fr}\n  .section h2{font-size:clamp(38px,4.6vw,60px);line-height:1.03}\n}\n'''
if 'v1.6b — Korean case-study heading fit' in t: raise SystemExit('v1.6b already present')
p.write_text(t+patch,encoding='utf-8')

print('BENCHMARK REFINE V1.6 PASS')
