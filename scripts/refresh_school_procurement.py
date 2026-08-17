from pathlib import Path

path = Path('index.html')
html = path.read_text(encoding='utf-8')

school_start = '<article class="project project-real project-school reveal tilt">'
rainbow_start = '<article class="project project-real project-rainbow reveal tilt">'
proc_start = '<article class="project project-real project-procurement reveal tilt">'
career_start = '    <section class="section" id="career">'

s1 = html.find(school_start)
s2 = html.find(rainbow_start, s1)
p1 = html.find(proc_start, s2)
c1 = html.find(career_start, p1)
if min(s1, s2, p1, c1) < 0:
    raise SystemExit(f'markers missing: school={s1}, rainbow={s2}, procurement={p1}, career={c1}')

school = '''<article class="project project-real project-school reveal tilt">
  <div class="project-copy">
    <div>
      <div class="project-meta"><span class="tag gold">🏆 BEST PROJECT</span><span class="tag">TRANSLATION · TTS PIPELINE</span></div>
      <div class="project-eyeline">MULTILINGUAL SCHOOL NOTICE AI</div>
      <h3>SchoolBridge</h3>
      <p>가정통신문의 날짜·금액·준비물처럼 놓치면 안 되는 정보를 보존하면서 8개 언어 번역과 음성 안내로 연결한 서비스입니다. 저는 <b style="color:#dfe7ef">NLLB 번역·학교 용어사전·번역 검수 루프·Edge-TTS</b>를 담당했습니다.</p>
      <div class="role-grid">
        <div class="role-box"><small>MY ROLE</small><strong>Translation · TTS Pipeline</strong></div>
        <div class="role-box"><small>STACK</small><strong>NLLB · Transformers · Edge-TTS</strong></div>
        <div class="role-box wide"><small>WHAT I OWNED</small><strong>8개 언어 번역 · 학교 용어사전 · 핵심정보 보존 · Round-trip 검수 · 음성 출력</strong></div>
      </div>
      <div class="project-metrics">
        <span class="metric">quality <b>39.0 → 89.6</b></span>
        <span class="metric">languages <b>8</b></span>
        <span class="metric">backend tests <b>27</b></span>
        <span class="metric"><b>실기기 E2E 검증</b></span>
      </div>
      <div class="featured-actions">
        <a class="project-btn primary" href="https://github.com/Maxmunzy/multicultural-ai" target="_blank" rel="noreferrer">View Project ↗</a>
        <a class="project-btn" href="https://github.com/Maxmunzy/multicultural-ai/tree/main/docs/experiments" target="_blank" rel="noreferrer">Quality Evidence ↗</a>
      </div>
    </div>
  </div>
  <div class="real-project-visual school-visual school-capture-visual">
    <div class="visual-label"><i></i> ANDROID UI FLOW · PARENT / TEACHER</div>
    <div class="school-shot-stage">
      <div class="school-shot parent-shot">
        <img src="assets/projects/schoolbridge-parent.png" alt="SchoolBridge 학부모 앱 UI 흐름" loading="lazy">
        <span class="screen-chip report">PARENT APP</span>
      </div>
      <div class="school-shot teacher-shot">
        <img src="assets/projects/schoolbridge-teacher.png" alt="SchoolBridge 선생님 앱 UI 흐름" loading="lazy">
        <span class="screen-chip sim">TEACHER APP</span>
      </div>
    </div>
    <div class="visual-caption"><span>CHECKLIST</span><span>8 LANGUAGES</span><span>TTS</span></div>
  </div>
</article>

'''

procurement = '''<article class="project project-real project-procurement reveal tilt">
  <div class="project-copy">
    <div>
      <div class="project-meta"><span class="tag">SOLO PRODUCT</span><span class="tag">PUBLIC DATA · ML</span></div>
      <div class="project-eyeline">PUBLIC DEMAND / LOGISTICS INTELLIGENCE</div>
      <h3>Procurement<br>Logistics AI</h3>
      <p>물류 현장에서 쌓은 수요·납품·거점 판단을 공공데이터 제품으로 옮긴 개인 프로젝트입니다. <b style="color:#dfe7ef">문제 정의부터 데이터 수집·분류·지표·AI 해석·대시보드</b>까지 전 과정을 구현했습니다.</p>
      <div class="role-grid">
        <div class="role-box"><small>MY ROLE</small><strong>Solo Product · Data Pipeline</strong></div>
        <div class="role-box"><small>STACK</small><strong>Python · Pandas · Scikit-learn · Streamlit</strong></div>
        <div class="role-box wide"><small>WHAT I OWNED</small><strong>6개 기관 9개 소스 · 전국 수요 분석 · TF-IDF/LogReg · Gemini 해석 · 물류 거점 지표</strong></div>
      </div>
      <div class="project-metrics">
        <span class="metric">bids <b>100,083</b></span>
        <span class="metric">aT bid/award <b>734,242</b></span>
        <span class="metric">classifier <b>98.6%</b></span>
        <span class="metric"><b>대면심사 진출</b></span>
      </div>
      <div class="featured-actions">
        <a class="project-btn primary" href="https://procurement-logistics-ai-5qian47widxpcuqefpjipy.streamlit.app" target="_blank" rel="noreferrer">Live Demo ↗</a>
        <a class="project-btn" href="https://github.com/mosejong/procurement-logistics-ai" target="_blank" rel="noreferrer">GitHub ↗</a>
      </div>
    </div>
  </div>
  <div class="real-project-visual procurement-visual procurement-capture-visual">
    <div class="visual-label"><i></i> LIVE HOMEPAGE CAPTURE · STREAMLIT</div>
    <div class="browser-capture">
      <div class="browser-capture-bar">
        <span class="browser-dots"><i></i><i></i><i></i></span>
        <span class="browser-url">procurement-logistics-ai · live</span>
      </div>
      <div class="browser-capture-body">
        <img src="assets/projects/procurement-home.png" alt="공공조달 수요 기반 입지 물류 분석 실제 홈페이지 캡처" loading="lazy">
      </div>
      <a class="capture-open" href="https://procurement-logistics-ai-5qian47widxpcuqefpjipy.streamlit.app" target="_blank" rel="noreferrer">OPEN LIVE ↗</a>
    </div>
    <div class="visual-caption"><span>6 AGENCIES</span><span>9 SOURCES</span><span>NATIONWIDE</span></div>
  </div>
</article>

'''

html = html[:s1] + school + html[s2:p1] + procurement + '''        </div>\n      </div>\n    </section>\n\n''' + html[c1:]

if '/* Captured project visuals v4 */' not in html:
    css = r'''
    /* Captured project visuals v4 */
    .school-capture-visual,.procurement-capture-visual{min-height:590px}
    .school-shot-stage{position:relative;z-index:2;width:100%;height:465px;display:flex;align-items:center;justify-content:center;perspective:1200px}
    .school-shot{position:absolute;width:min(79%,610px);aspect-ratio:1.58/1;border-radius:20px;border:1px solid rgba(255,255,255,.14);overflow:hidden;background:#eef4f4;box-shadow:0 34px 95px rgba(0,0,0,.46);transition:.38s cubic-bezier(.2,.8,.2,1)}
    .school-shot img{width:100%;height:100%;display:block;object-fit:cover;object-position:left top}
    .parent-shot{transform:translate(-42px,-24px) rotateY(6deg) rotateZ(-1deg);z-index:2}
    .teacher-shot{width:min(62%,490px);transform:translate(108px,118px) rotateY(-5deg) rotateZ(2deg);z-index:3}
    .project-school:hover .parent-shot{transform:translate(-52px,-34px) rotateY(3deg) rotateZ(-1deg)}
    .project-school:hover .teacher-shot{transform:translate(116px,106px) rotateY(-2deg) rotateZ(1deg)}
    .browser-capture{position:relative;z-index:2;width:96%;height:455px;border:1px solid rgba(255,255,255,.14);border-radius:21px;overflow:hidden;background:#0b1016;box-shadow:0 34px 95px rgba(0,0,0,.46);transition:.35s cubic-bezier(.2,.8,.2,1)}
    .project-procurement:hover .browser-capture{transform:translateY(-6px) scale(1.008)}
    .browser-capture-bar{height:42px;display:flex;align-items:center;gap:13px;padding:0 14px;border-bottom:1px solid rgba(255,255,255,.08);background:#0b1017}
    .browser-dots{display:flex;gap:6px}.browser-dots i{width:7px;height:7px;border-radius:50%;background:#44505f}.browser-dots i:first-child{background:#f27c75}.browser-dots i:nth-child(2){background:#edc469}.browser-dots i:nth-child(3){background:#6ed093}
    .browser-url{flex:1;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;color:#677487;font:650 9px ui-monospace,SFMono-Regular,Menlo,monospace}
    .browser-capture-body{height:calc(100% - 42px);overflow:hidden;background:#fff}
    .browser-capture-body img{width:100%;height:100%;display:block;object-fit:cover;object-position:top center}
    .capture-open{position:absolute;right:13px;bottom:13px;padding:8px 10px;border-radius:9px;border:1px solid rgba(255,255,255,.15);background:rgba(7,10,15,.86);backdrop-filter:blur(9px);font:800 8px ui-monospace,SFMono-Regular,Menlo,monospace;color:#e4ebf2}
    @media(max-width:980px){.school-capture-visual,.procurement-capture-visual{min-height:530px}.school-shot-stage{height:420px}.browser-capture{height:410px}}
    @media(max-width:680px){.school-capture-visual,.procurement-capture-visual{min-height:400px}.school-shot-stage{height:305px}.school-shot{width:92%}.parent-shot{transform:translate(-18px,-14px)}.teacher-shot{width:68%;transform:translate(72px,82px) rotateZ(2deg)}.browser-capture{width:100%;height:310px}.browser-capture-bar{height:36px}.browser-capture-body{height:calc(100% - 36px)}}
'''
    html = html.replace('</style>', css + '\n  </style>', 1)

path.write_text(html, encoding='utf-8')
print('SchoolBridge and procurement cards refreshed.')
