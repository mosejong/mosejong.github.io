from pathlib import Path

path = Path('index.html')
s = path.read_text(encoding='utf-8')

marker = '/* HERO_TITLE_CLIP_FIX_V13 */'
block = '''
    /* HERO_TITLE_CLIP_FIX_V13 */
    .hero h1{
      font-size:clamp(50px,6.7vw,96px);
      line-height:1.045;
      letter-spacing:-.055em;
      max-width:none;
      white-space:nowrap;
      overflow:visible;
      padding-block:.04em .08em;
    }
    .hero,.hero-grid,.hero-grid>div{overflow:visible}
    @media(max-width:980px){
      .hero h1{font-size:clamp(46px,9vw,82px);line-height:1.06;letter-spacing:-.05em}
    }
    @media(max-width:680px){
      .hero h1{font-size:clamp(33px,9.1vw,54px);line-height:1.09;letter-spacing:-.038em}
    }
'''

if marker in s:
    start = s.index(marker)
    start = s.rfind('\n', 0, start) + 1
    end = s.find('    /* Awards side dock */', start)
    if end == -1:
        raise SystemExit('could not locate end of existing hero fix')
    s = s[:start] + block + '\n' + s[end:]
else:
    anchor = '    /* Awards side dock */'
    if anchor not in s:
        raise SystemExit('CSS anchor not found')
    s = s.replace(anchor, block + '\n' + anchor, 1)

assert marker in s
assert 'white-space:nowrap' in s
assert 'line-height:1.045' in s
path.write_text(s, encoding='utf-8')
print('hero title clip fix applied')
