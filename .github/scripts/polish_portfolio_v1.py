from pathlib import Path

path = Path('index.html')
s = path.read_text(encoding='utf-8')

css = r'''

    /* Portfolio v1.0 visual polish */
    .project-list{gap:24px}
    .project{box-shadow:0 18px 60px rgba(0,0,0,.16)}
    .project:hover{box-shadow:0 32px 90px rgba(0,0,0,.32)}
    .project-copy p{max-width:555px}
    .project-metrics{gap:7px}
    .metric{background:rgba(4,8,13,.34)}

    /* Jobiverse — reference card */
    .project-featured-real{grid-template-columns:.94fr 1.06fr}
    .project-featured-real .product-screen img{object-position:center top}
    .project-featured-real .product-screen.main{width:87%;height:79%;right:1%;top:3%}
    .project-featured-real .product-screen.secondary{width:54%;height:47%;left:0;bottom:0}

    /* SchoolBridge — clean dual product view */
    .school-capture-visual{padding:54px 25px 30px;min-height:575px}
    .school-shot-stage{
      position:relative;z-index:2;width:100%;height:420px;display:flex;gap:14px;
      align-items:stretch;justify-content:center;perspective:none
    }
    .school-shot{
      position:relative;inset:auto;width:auto!important;height:100%;border-radius:19px;
      border:1px solid rgba(255,255,255,.14);overflow:hidden;background:#eef4f4;
      box-shadow:0 30px 80px rgba(0,0,0,.40);transform:none!important;
      transition:.32s cubic-bezier(.2,.8,.2,1)
    }
    .parent-shot{flex:1.14;z-index:2}
    .teacher-shot{flex:.86;z-index:2}
    .school-shot img{width:100%;height:100%;display:block;object-fit:cover;object-position:left top}
    .project-school:hover .parent-shot{transform:translateY(-5px)!important}
    .project-school:hover .teacher-shot{transform:translateY(-5px)!important}
    .school-flow-pill{
      position:absolute;z-index:6;left:50%;bottom:13px;transform:translateX(-50%);
      display:flex;align-items:center;gap:8px;padding:8px 11px;border-radius:999px;
      border:1px solid rgba(140,245,210,.20);background:rgba(7,12,16,.86);backdrop-filter:blur(12px);
      box-shadow:0 12px 30px rgba(0,0,0,.28);white-space:nowrap
    }
    .school-flow-pill span{font:800 8px ui-monospace,SFMono-Regular,Menlo,monospace;color:#ccefe3;letter-spacing:.06em}
    .school-flow-pill i{font-style:normal;color:#5e7e74;font-size:9px}

    /* Rainbow Bridge — mobile demo + service flow */
    .rainbow-visual{padding:54px 24px 30px}
    .rainbow-stage{position:relative;z-index:2;width:100%;height:430px;display:flex;align-items:center;justify-content:center;gap:20px}
    .rainbow-stage .phone-demo{width:min(68%,430px);height:430px;flex:0 1 430px}
    .rainbow-flow{width:150px;display:grid;gap:9px;align-content:center}
    .rainbow-flow .flow-step{
      min-height:62px;padding:10px 11px;border-radius:13px;border:1px solid rgba(170,151,255,.14);
      background:rgba(170,151,255,.045);display:flex;align-items:center;gap:9px
    }
    .flow-step b{width:24px;height:24px;border-radius:8px;display:grid;place-items:center;background:rgba(170,151,255,.10);color:#cfc4ff;font:800 8px ui-monospace,monospace}
    .flow-step span{font:750 8px/1.35 ui-monospace,SFMono-Regular,Menlo,monospace;color:#a7a2bf;letter-spacing:.04em}
    .flow-step + .flow-step:before{content:'↓';position:absolute;color:#625b82;margin-top:-79px;margin-left:7px;font-size:9px}

    /* Procurement — live dashboard focus */
    .project-procurement{background:linear-gradient(135deg,rgba(255,214,138,.035),rgba(255,255,255,.022) 45%,rgba(255,214,138,.018))}
    .origin-note{
      margin-top:22px;padding:13px 14px;border-radius:13px;border:1px solid rgba(255,214,138,.16);
      background:linear-gradient(90deg,rgba(255,214,138,.07),rgba(255,214,138,.018))
    }
    .origin-note small{display:block;color:#9e8964;font:800 8px ui-monospace,SFMono-Regular,Menlo,monospace;letter-spacing:.12em;margin-bottom:6px}
    .origin-note strong{display:block;color:#f0dfbd;font-size:11px;line-height:1.5}
    .procurement-capture-visual{padding:54px 22px 30px;min-height:575px}
    .browser-capture{width:100%;height:470px;border-color:rgba(255,214,138,.18)}
    .browser-capture-body{position:relative;overflow:hidden}
    .browser-capture-body img{
      width:100%;height:100%;display:block;object-fit:cover;object-position:center top;
      transform:scale(1.115);transform-origin:55% 38%
    }
    .dashboard-badges{
      position:absolute;z-index:5;left:13px;bottom:13px;display:flex;gap:6px;flex-wrap:wrap;max-width:75%
    }
    .dashboard-badges span{
      padding:6px 8px;border-radius:8px;background:rgba(7,10,15,.84);border:1px solid rgba(255,255,255,.10);
      color:#dce5ed;font:800 7px ui-monospace,SFMono-Regular,Menlo,monospace;backdrop-filter:blur(8px)
    }
    .dashboard-badges span:first-child{color:#ffe0a6;border-color:rgba(255,214,138,.20)}

    @media(max-width:980px){
      .project-featured-real{grid-template-columns:1fr}
      .school-capture-visual,.procurement-capture-visual{min-height:510px}
      .rainbow-stage{height:420px}
    }
    @media(max-width:680px){
      .project-list{gap:16px}
      .school-capture-visual{padding:44px 14px 22px;min-height:420px}
      .school-shot-stage{height:330px;gap:8px}
      .teacher-shot{flex:.78}
      .school-flow-pill{bottom:9px;padding:7px 9px;gap:6px}
      .rainbow-visual{padding:44px 14px 22px}
      .rainbow-stage{height:auto;min-height:390px;gap:10px}
      .rainbow-stage .phone-demo{width:68%;height:350px;flex-basis:68%}
      .rainbow-flow{width:30%;gap:7px}
      .rainbow-flow .flow-step{min-height:50px;padding:7px;gap:6px}
      .flow-step b{width:20px;height:20px}
      .flow-step span{font-size:7px}
      .procurement-capture-visual{padding:44px 14px 22px;min-height:405px}
      .browser-capture{height:330px}
      .browser-capture-body img{transform:scale(1.16);transform-origin:58% 36%}
      .dashboard-badges{left:8px;bottom:8px;max-width:72%}
    }
'''

if '/* Portfolio v1.0 visual polish */' not in s:
    assert '</style>' in s
    s = s.replace('</style>', css + '\n  </style>', 1)

# SchoolBridge: labels and clean dual-view flow badge
s = s.replace(
    '<div class="visual-label"><i></i> ANDROID UI FLOW · PARENT / TEACHER</div>',
    '<div class="visual-label"><i></i> SERVICE UI · PARENT / TEACHER</div>',
    1,
)
s = s.replace(
    '''      <div class="school-shot teacher-shot">\n        <img src="assets/projects/schoolbridge-teacher.png" alt="SchoolBridge 선생님 앱 UI 흐름" loading="lazy">\n        <span class="screen-chip sim">TEACHER APP</span>\n      </div>\n    </div>\n    <div class="visual-caption"><span>CHECKLIST</span><span>8 LANGUAGES</span><span>TTS</span></div>''',
    '''      <div class="school-shot teacher-shot">\n        <img src="assets/projects/schoolbridge-teacher.png" alt="SchoolBridge 선생님 앱 UI 흐름" loading="lazy">\n        <span class="screen-chip sim">TEACHER APP</span>\n      </div>\n      <div class="school-flow-pill"><span>KO</span><i>→</i><span>8 LANG</span><i>→</i><span>TTS</span></div>\n    </div>\n    <div class="visual-caption"><span>KEY INFO PRESERVED</span><span>8 LANGUAGES</span><span>TTS</span></div>''',
    1,
)

# Rainbow Bridge: add service-flow rail beside real mobile demo
s = s.replace(
    '<div class="visual-label"><i></i> REAL PROJECT DEMO · MOBILE FLOW</div>\n    <div class="single-real-screen rainbow-screen phone-demo">\n      <img src="https://raw.githubusercontent.com/mosejong/mosejong/main/assets/rainbow-bridge-demo.gif" alt="Rainbow Bridge 실제 모바일 서비스 데모" loading="lazy">\n      <span class="screen-chip sim">LIVE DEMO GIF</span>\n    </div>\n    <div class="visual-caption"><span>FASTAPI</span><span>EXPO</span><span>AI CARE FLOW</span></div>',
    '<div class="visual-label"><i></i> REAL MOBILE FLOW · CHECK-IN → REPORT</div>\n    <div class="rainbow-stage">\n      <div class="single-real-screen rainbow-screen phone-demo">\n        <img src="https://raw.githubusercontent.com/mosejong/mosejong/main/assets/rainbow-bridge-demo.gif" alt="Rainbow Bridge 실제 모바일 서비스 데모" loading="lazy">\n        <span class="screen-chip sim">LIVE DEMO GIF</span>\n      </div>\n      <div class="rainbow-flow" aria-label="Rainbow Bridge service flow">\n        <div class="flow-step"><b>01</b><span>EMOTION<br>CHECK-IN</span></div>\n        <div class="flow-step"><b>02</b><span>MESSAGE<br>+ TTS</span></div>\n        <div class="flow-step"><b>03</b><span>RECOVERY<br>MISSION</span></div>\n        <div class="flow-step"><b>04</b><span>TIMELINE<br>+ REPORT</span></div>\n      </div>\n    </div>\n    <div class="visual-caption"><span>NCP</span><span>DOCKER</span><span>EXPO</span></div>',
    1,
)

# Procurement: strengthen field-to-product story and focus the live screenshot
proc_marker = '''      <div class="role-grid">\n        <div class="role-box"><small>MY ROLE</small><strong>Solo Product · Data Pipeline</strong></div>'''
if '<div class="origin-note">' not in s:
    s = s.replace(
        proc_marker,
        '''      <div class="origin-note"><small>FIELD → PRODUCT</small><strong>8년 9개월 물류·운영 경험을 공공 수요와 거점 판단 데이터 제품으로 전환</strong></div>\n      <div class="role-grid">\n        <div class="role-box"><small>MY ROLE</small><strong>Solo Product · Data Pipeline</strong></div>''',
        1,
    )
s = s.replace(
    '<div class="visual-label"><i></i> LIVE HOMEPAGE CAPTURE · STREAMLIT</div>',
    '<div class="visual-label"><i></i> LIVE DASHBOARD · NATIONWIDE DEMAND MAP</div>',
    1,
)
s = s.replace(
    '''      <div class="browser-capture-body">\n        <img src="assets/projects/procurement-home.png" alt="공공조달 수요 기반 입지 물류 분석 실제 홈페이지 캡처" loading="lazy">\n      </div>\n      <a class="capture-open"''',
    '''      <div class="browser-capture-body">\n        <img src="assets/projects/procurement-home.png" alt="공공조달 수요 기반 입지 물류 분석 실제 홈페이지 캡처" loading="lazy">\n        <div class="dashboard-badges"><span>LIVE DATA</span><span>전국 지도</span><span>93,971 공고</span></div>\n      </div>\n      <a class="capture-open"''',
    1,
)

# Make the page feel finished in the project section copy.
s = s.replace(
    '각 프로젝트에서 내가 맡은 문제, 구현 범위, 결과가 한 화면 안에서 보이도록 구성했습니다.',
    '실제 서비스 화면과 함께 내가 맡은 문제, 구현 범위, 검증 결과를 한 화면 안에서 확인할 수 있습니다.',
    1,
)

required = [
    'school-flow-pill', 'rainbow-stage', 'origin-note', 'dashboard-badges',
    'LIVE DASHBOARD · NATIONWIDE DEMAND MAP', 'Portfolio v1.0 visual polish'
]
for marker in required:
    if marker not in s:
        raise SystemExit(f'missing expected marker after patch: {marker}')

path.write_text(s, encoding='utf-8')
print('Portfolio v1.0 visual polish applied.')
