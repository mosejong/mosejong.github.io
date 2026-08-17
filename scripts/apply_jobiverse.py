from pathlib import Path

path = Path("index.html")
html = path.read_text(encoding="utf-8")

start_marker = '<a class="project reveal tilt" href="https://github.com/neunglog-sys/job_simulator" target="_blank" rel="noreferrer">'
end_marker = '<a class="project reveal tilt" href="https://github.com/Maxmunzy/multicultural-ai" target="_blank" rel="noreferrer">'

start = html.find(start_marker)
end = html.find(end_marker, start)
if start < 0 or end < 0:
    raise SystemExit("Jobiverse project block markers not found")

card = '''<article class="project project-featured-real reveal tilt">
            <div class="project-copy">
              <div>
                <div class="project-meta"><span class="tag gold">🏆 GRAND PRIZE</span><span class="tag">REPORTING · DATA PIPELINE</span></div>
                <div class="project-eyeline">AI CAREER EXPERIENCE PLATFORM</div>
                <h3>Jobiverse</h3>
                <p>AI 상담 → 가상 직무 체험 → 근거 기반 적합도 리포트로 이어지는 진로 탐색 플랫폼. 저는 <b style="color:#dfe7ef">리포트·추천 근거·외부 데이터·검증 흐름</b>을 맡았습니다.</p>

                <div class="role-grid">
                  <div class="role-box"><small>MY ROLE</small><strong>Reporting · Data Pipeline</strong></div>
                  <div class="role-box"><small>STACK</small><strong>FastAPI · PostgreSQL · pgvector</strong></div>
                  <div class="role-box wide"><small>WHAT I OWNED</small><strong>역량 레이더 · AI 해석 · 근거 각주 · PDF · 공공 API · CI</strong></div>
                </div>

                <div class="project-metrics">
                  <span class="metric">contamination <b>12.5% → 0%</b></span>
                  <span class="metric">embedding p90 <b>1.3s → 0.4s</b></span>
                  <span class="metric">evidence <b>100%</b></span>
                  <span class="metric">project tests <b>564</b></span>
                </div>

                <div class="featured-actions">
                  <a class="project-btn primary" href="https://github.com/neunglog-sys/job_simulator#-about-the-project" target="_blank" rel="noreferrer">View Case Study ↗</a>
                  <a class="project-btn" href="https://github.com/neunglog-sys/job_simulator" target="_blank" rel="noreferrer">GitHub ↗</a>
                </div>
              </div>
            </div>
            <div class="real-visual">
              <div class="visual-label"><i></i> REAL PROJECT DEMO · REPORT + SIMULATION</div>
              <div class="screen-stack">
                <div class="product-screen main">
                  <img src="https://raw.githubusercontent.com/neunglog-sys/job_simulator/main/docs/media/gif/final_report.gif" alt="Jobiverse 실제 직무 적합도 리포트 시연" loading="lazy">
                  <span class="screen-chip report">FINAL REPORT</span>
                </div>
                <div class="product-screen secondary">
                  <img src="https://raw.githubusercontent.com/neunglog-sys/job_simulator/main/docs/media/gif/senario2.gif" alt="Jobiverse 실제 가상 직무 체험 시연" loading="lazy">
                  <span class="screen-chip sim">SIMULATION</span>
                </div>
              </div>
              <div class="visual-caption"><span>38 JOB FAMILIES</span><span>37 SCENARIOS</span><span>204 JOBS</span></div>
            </div>
          </article>

          '''

html = html[:start] + card + html[end:]

if ".project-featured-real" not in html[:html.find("</style>")]:
    css = '''
    /* Featured real-project case study */
    .project-featured-real{min-height:560px;grid-template-columns:.9fr 1.1fr;border-color:rgba(130,215,255,.16);background:linear-gradient(135deg,rgba(130,215,255,.055),rgba(255,255,255,.025) 42%,rgba(140,245,210,.025))}
    .project-featured-real .project-copy{padding:36px 34px}
    .project-eyeline{margin-top:22px;color:#6f7d90;font:800 9px ui-monospace,SFMono-Regular,Menlo,monospace;letter-spacing:.16em}
    .project-featured-real h3{font-size:clamp(45px,5vw,66px);margin:12px 0 17px}
    .role-grid{display:grid;grid-template-columns:1fr 1fr;gap:9px;margin-top:26px}
    .role-box{padding:13px 14px;border:1px solid rgba(255,255,255,.075);border-radius:13px;background:rgba(255,255,255,.026)}
    .role-box.wide{grid-column:span 2}
    .role-box small{display:block;color:#657386;font:800 8px ui-monospace,SFMono-Regular,Menlo,monospace;letter-spacing:.09em;margin-bottom:6px}
    .role-box strong{display:block;color:#dce4ed;font-size:11px;line-height:1.45}
    .featured-actions{display:flex;gap:8px;flex-wrap:wrap;margin-top:23px}
    .project-btn{display:inline-flex;align-items:center;justify-content:center;min-height:40px;padding:0 13px;border-radius:11px;border:1px solid rgba(255,255,255,.1);background:rgba(255,255,255,.035);font-size:11px;font-weight:800;color:#cbd5df;transition:.22s}
    .project-btn.primary{background:#eff5f8;color:#081016;border-color:#eff5f8}
    .project-btn:hover{transform:translateY(-2px);box-shadow:0 12px 30px rgba(0,0,0,.25)}
    .real-visual{position:relative;min-height:560px;border-left:1px solid rgba(255,255,255,.075);overflow:hidden;background:radial-gradient(620px 380px at 55% 36%,rgba(130,215,255,.13),transparent 62%),radial-gradient(420px 280px at 20% 86%,rgba(140,245,210,.08),transparent 68%),#080d14;padding:38px 30px 30px;display:flex;flex-direction:column;justify-content:center}
    .real-visual:before{content:"";position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,.025) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.025) 1px,transparent 1px);background-size:30px 30px;mask-image:linear-gradient(to bottom,#000,transparent 88%)}
    .visual-label{position:absolute;left:28px;top:22px;z-index:4;display:flex;align-items:center;gap:7px;color:#758296;font:750 8px ui-monospace,SFMono-Regular,Menlo,monospace;letter-spacing:.08em}
    .visual-label i{width:7px;height:7px;border-radius:50%;background:#8cf5d2;box-shadow:0 0 15px rgba(140,245,210,.8)}
    .screen-stack{height:430px;position:relative;z-index:2;margin-top:16px}
    .product-screen{position:absolute;overflow:hidden;border:1px solid rgba(255,255,255,.13);border-radius:18px;background:#0a0e14;box-shadow:0 30px 80px rgba(0,0,0,.44);transition:.38s cubic-bezier(.2,.8,.2,1)}
    .product-screen img{width:100%;height:100%;object-fit:cover;display:block}
    .product-screen.main{width:83%;height:76%;right:3%;top:5%;transform:rotate(1.4deg)}
    .product-screen.secondary{width:55%;height:48%;left:0;bottom:1%;transform:rotate(-2.5deg)}
    .project-featured-real:hover .product-screen.main{transform:rotate(.3deg) translateY(-6px) scale(1.012)}
    .project-featured-real:hover .product-screen.secondary{transform:rotate(-1deg) translate(-4px,-4px) scale(1.02)}
    .screen-chip{position:absolute;left:10px;top:10px;padding:6px 8px;border-radius:8px;background:rgba(7,10,15,.82);backdrop-filter:blur(8px);border:1px solid rgba(255,255,255,.09);font:800 7px ui-monospace,SFMono-Regular,Menlo,monospace;letter-spacing:.07em}
    .screen-chip.report{color:#9fe7cc}.screen-chip.sim{color:#9fcfff}
    .visual-caption{position:absolute;z-index:3;right:25px;bottom:18px;display:flex;gap:14px;color:#657386;font:750 7px ui-monospace,SFMono-Regular,Menlo,monospace;letter-spacing:.07em}
    @media(max-width:980px){.project-featured-real{grid-template-columns:1fr}.real-visual{border-left:0;border-top:1px solid rgba(255,255,255,.075);min-height:500px}}
    @media(max-width:680px){.project-featured-real .project-copy{padding:25px 22px 28px}.role-grid{grid-template-columns:1fr}.role-box.wide{grid-column:auto}.real-visual{min-height:390px;padding:28px 15px 20px}.screen-stack{height:320px}.product-screen.main{width:88%;height:73%}.product-screen.secondary{width:60%;height:46%}.visual-caption{right:15px;gap:8px}}
    '''
    html = html.replace("</style>", css + "\n  </style>", 1)

path.write_text(html, encoding="utf-8")
print("Jobiverse card upgraded")
