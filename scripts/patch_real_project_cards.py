from pathlib import Path

path = Path('index.html')
html = path.read_text(encoding='utf-8')

school_start = '<a class="project reveal tilt" href="https://github.com/Maxmunzy/multicultural-ai" target="_blank" rel="noreferrer">'
rainbow_start = '<a class="project reveal tilt" href="https://github.com/mosejong/Rainbow-Bridge" target="_blank" rel="noreferrer">'
procurement_start = '<a class="project reveal tilt" href="https://github.com/mosejong/procurement-logistics-ai" target="_blank" rel="noreferrer">'
career_start = '    <section class="section" id="career">'

s1 = html.find(school_start)
s2 = html.find(rainbow_start, s1)
s3 = html.find(procurement_start, s2)
s4 = html.find(career_start, s3)
if min(s1, s2, s3, s4) < 0:
    raise SystemExit(f'project markers not found: {s1}, {s2}, {s3}, {s4}')

school = r'''<article class="project project-real project-school reveal tilt">
  <div class="project-copy">
    <div>
      <div class="project-meta"><span class="tag gold">🏆 BEST PROJECT</span><span class="tag">TRANSLATION · TTS PIPELINE</span></div>
      <div class="project-eyeline">MULTILINGUAL SCHOOL NOTICE AI</div>
      <h3>SchoolBridge</h3>
      <p>가정통신문의 날짜·금액·준비물 같은 핵심 행동정보를 보존하면서 8개 언어로 번역하고 음성으로 전달하는 서비스입니다. 저는 <b style="color:#dfe7ef">NLLB 번역·학교 용어사전·검수 루프·TTS</b>를 맡았습니다.</p>
      <div class="role-grid">
        <div class="role-box"><small>MY ROLE</small><strong>Translation · TTS Pipeline</strong></div>
        <div class="role-box"><small>STACK</small><strong>NLLB · Transformers · Edge-TTS</strong></div>
        <div class="role-box wide"><small>WHAT I OWNED</small><strong>8개 언어 번역 · 학교 용어사전 · 핵심정보 보존 · Round-trip 검수 · 음성 출력</strong></div>
      </div>
      <div class="project-metrics">
        <span class="metric">quality <b>39.0 → 89.6</b></span>
        <span class="metric">languages <b>8</b></span>
        <span class="metric">backend tests <b>27</b></span>
        <span class="metric"><b>Android E2E</b></span>
      </div>
      <div class="featured-actions">
        <a class="project-btn primary" href="https://github.com/Maxmunzy/multicultural-ai" target="_blank" rel="noreferrer">View Project ↗</a>
        <a class="project-btn" href="https://github.com/Maxmunzy/multicultural-ai/tree/main/docs/experiments" target="_blank" rel="noreferrer">Quality Evidence ↗</a>
      </div>
    </div>
  </div>
  <div class="real-project-visual school-visual">
    <div class="visual-label"><i></i> REAL PROJECT ASSET · TRANSLATION / TTS</div>
    <div class="single-real-screen school-screen">
      <img src="https://raw.githubusercontent.com/Maxmunzy/multicultural-ai/main/docs/assets/translation_tts_status.png" alt="SchoolBridge 실제 번역 TTS 프로젝트 상태 화면" loading="lazy">
      <span class="screen-chip report">TRANSLATION + TTS</span>
    </div>
    <div class="visual-caption"><span>NLLB</span><span>8 LANGUAGES</span><span>EDGE-TTS</span></div>
  </div>
</article>

'''

rainbow = r'''<article class="project project-real project-rainbow reveal tilt">
  <div class="project-copy">
    <div>
      <div class="project-meta"><span class="tag">TEAM LEAD</span><span class="tag">BACKEND INTEGRATION</span></div>
      <div class="project-eyeline">AI PET-LOSS AFTERCARE SERVICE</div>
      <h3>Rainbow Bridge</h3>
      <p>감정 체크인 → 추모 메시지·TTS → 회복 미션 → 타임라인·리포트로 이어지는 AI 펫로스 애프터케어 서비스. 저는 <b style="color:#dfe7ef">팀 운영·API 통합·서버 배포·사용자 시연 흐름</b>을 맡았습니다.</p>
      <div class="role-grid">
        <div class="role-box"><small>MY ROLE</small><strong>Team Lead · Backend Integration</strong></div>
        <div class="role-box"><small>STACK</small><strong>FastAPI · NCP · Docker · nginx</strong></div>
        <div class="role-box wide"><small>WHAT I OWNED</small><strong>우선순위 조율 · API 흐름 통합 · 서버 운영 · CI/CD · Expo 모바일 시연</strong></div>
      </div>
      <div class="project-metrics">
        <span class="metric">safety routing <b>40/40</b></span>
        <span class="metric">G-Eval <b>4.76–4.83 / 5</b></span>
        <span class="metric">lip-sync <b>0.896</b></span>
        <span class="metric"><b>6-person team</b></span>
      </div>
      <div class="featured-actions">
        <a class="project-btn primary" href="https://github.com/mosejong/Rainbow-Bridge" target="_blank" rel="noreferrer">View Project ↗</a>
        <a class="project-btn" href="https://github.com/mosejong/Rainbow-Bridge/blob/dev/CONTRIBUTION.md" target="_blank" rel="noreferrer">My Contribution ↗</a>
      </div>
    </div>
  </div>
  <div class="real-project-visual rainbow-visual">
    <div class="visual-label"><i></i> REAL PROJECT DEMO · MOBILE FLOW</div>
    <div class="single-real-screen rainbow-screen phone-demo">
      <img src="https://raw.githubusercontent.com/mosejong/mosejong/main/assets/rainbow-bridge-demo.gif" alt="Rainbow Bridge 실제 모바일 서비스 데모" loading="lazy">
      <span class="screen-chip sim">LIVE DEMO GIF</span>
    </div>
    <div class="visual-caption"><span>FASTAPI</span><span>EXPO</span><span>AI CARE FLOW</span></div>
  </div>
</article>

'''

procurement = r'''<article class="project project-real project-procurement reveal tilt">
  <div class="project-copy">
    <div>
      <div class="project-meta"><span class="tag">SOLO PRODUCT</span><span class="tag">PUBLIC DATA · ML</span></div>
      <div class="project-eyeline">PUBLIC DEMAND / LOGISTICS INTELLIGENCE</div>
      <h3>Procurement<br>Logistics AI</h3>
      <p>물류 현장에서 쌓은 수요·납품·거점 판단을 공공데이터 제품으로 옮긴 개인 프로젝트. <b style="color:#dfe7ef">문제 정의부터 데이터 수집·분류·지표·AI 해석·대시보드</b>까지 전 과정을 구현했습니다.</p>
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
  <div class="real-project-visual procurement-visual">
    <div class="visual-label"><i></i> LIVE PRODUCT · STREAMLIT DASHBOARD</div>
    <div class="live-frame-wrap">
      <iframe src="https://procurement-logistics-ai-5qian47widxpcuqefpjipy.streamlit.app/?embed=true" title="공공조달 수요 기반 입지 물류 분석 라이브 대시보드" loading="lazy"></iframe>
      <a class="frame-fallback" href="https://procurement-logistics-ai-5qian47widxpcuqefpjipy.streamlit.app" target="_blank" rel="noreferrer">Open live dashboard ↗</a>
    </div>
    <div class="visual-caption"><span>6 AGENCIES</span><span>9 SOURCES</span><span>NATIONWIDE</span></div>
  </div>
</article>

      </div>
    </div>
  </section>

'''

html = html[:s1] + school + rainbow + procurement + html[s4:]

if '/* Real project cards v2 */' not in html:
    css = r'''
    /* Real project cards v2 */
    .project-real{min-height:560px;grid-template-columns:.92fr 1.08fr;background:linear-gradient(135deg,rgba(255,255,255,.047),rgba(255,255,255,.022));}
    .project-real .project-copy{padding:35px 34px}
    .project-school{border-color:rgba(140,245,210,.14)}
    .project-rainbow{border-color:rgba(170,151,255,.15)}
    .project-procurement{border-color:rgba(255,214,138,.14)}
    .real-project-visual{position:relative;min-height:560px;border-left:1px solid rgba(255,255,255,.075);overflow:hidden;padding:42px 28px 28px;display:flex;align-items:center;justify-content:center;background:#080d14}
    .real-project-visual:before{content:"";position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,.025) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.025) 1px,transparent 1px);background-size:30px 30px;mask-image:linear-gradient(to bottom,#000,transparent 90%)}
    .school-visual{background:radial-gradient(560px 330px at 55% 42%,rgba(140,245,210,.10),transparent 65%),#080d14}
    .rainbow-visual{background:radial-gradient(560px 340px at 55% 42%,rgba(170,151,255,.12),transparent 65%),#090b14}
    .procurement-visual{background:radial-gradient(560px 340px at 55% 42%,rgba(255,214,138,.09),transparent 65%),#0b0d11}
    .single-real-screen{position:relative;z-index:2;width:min(94%,610px);max-height:430px;border:1px solid rgba(255,255,255,.13);border-radius:19px;background:#0a0e14;box-shadow:0 30px 80px rgba(0,0,0,.44);overflow:hidden;transition:.38s cubic-bezier(.2,.8,.2,1)}
    .single-real-screen img{display:block;width:100%;height:100%;max-height:430px;object-fit:contain;background:#0a0e14}
    .project-real:hover .single-real-screen{transform:translateY(-6px) scale(1.012)}
    .phone-demo{width:min(74%,470px);height:430px;background:#0a0e14}
    .phone-demo img{object-fit:contain;height:100%}
    .live-frame-wrap{position:relative;z-index:2;width:96%;height:430px;border:1px solid rgba(255,255,255,.13);border-radius:19px;overflow:hidden;background:#10141a;box-shadow:0 30px 80px rgba(0,0,0,.44)}
    .live-frame-wrap iframe{display:block;width:100%;height:100%;border:0;background:#fff}
    .frame-fallback{position:absolute;right:10px;bottom:10px;padding:8px 10px;border-radius:9px;background:rgba(7,10,15,.88);border:1px solid rgba(255,255,255,.1);font:800 8px ui-monospace,SFMono-Regular,Menlo,monospace;color:#dce5ed;backdrop-filter:blur(8px)}
    @media(max-width:980px){.project-real{grid-template-columns:1fr}.real-project-visual{border-left:0;border-top:1px solid rgba(255,255,255,.075);min-height:500px}}
    @media(max-width:680px){.project-real .project-copy{padding:25px 22px 28px}.real-project-visual{min-height:390px;padding:38px 15px 20px}.single-real-screen,.phone-demo,.live-frame-wrap{width:100%;height:320px;max-height:320px}.single-real-screen img{max-height:320px}.phone-demo img{height:100%}}
    '''
    html = html.replace('</style>', css + '\n  </style>', 1)

path.write_text(html, encoding='utf-8')
print('Patched real project cards successfully')
