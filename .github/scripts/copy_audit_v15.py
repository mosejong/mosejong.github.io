from pathlib import Path
from html.parser import HTMLParser
import re

FILES = [
    'index.html',
    'projects/jobiverse.html',
    'projects/schoolbridge.html',
    'projects/rainbow-bridge.html',
    'projects/procurement-logistics-ai.html',
]

BLOCK = {'p','h1','h2','h3','h4','div','section','article','li','span','small','strong','b','pre','br'}
SKIP = {'style','script','svg'}

class VisibleText(HTMLParser):
    def __init__(self):
        super().__init__()
        self.depth_skip = 0
        self.parts = []
    def handle_starttag(self, tag, attrs):
        if tag in SKIP:
            self.depth_skip += 1
        elif self.depth_skip == 0 and tag in BLOCK:
            self.parts.append('\n')
    def handle_endtag(self, tag):
        if tag in SKIP and self.depth_skip:
            self.depth_skip -= 1
        elif self.depth_skip == 0 and tag in BLOCK:
            self.parts.append('\n')
    def handle_data(self, data):
        if self.depth_skip == 0:
            self.parts.append(data)

PATTERNS = {
    'META_SELF': [r'지향', r'목표였', r'중요했', r'생각했', r'느꼈', r'보고 싶', r'노력했', r'경험을 정리', r'저는', r'제가', r'제 역할은'],
    'VAGUE': [r'다양한', r'여러 ', r'효율적', r'안정적', r'사용자 관점', r'품질을 높', r'최적화', r'잘 되', r'좋은 '],
    'OVERCLAIM': [r'완벽', r'유일', r'모든 ', r'전체를 책임', r'끝까지', r'혼자 끝까지', r'실시간', r'100%'],
    'JARGON': [r'정합성', r'폴백', r'PR gate', r'오염률', r'피처', r'컨텍스트', r'RAG', r'E2E', r'G-Eval', r'립싱크'],
}
VERBS = ['연결했습니다','검증했습니다','개선했습니다','구성했습니다','설계했습니다','구현했습니다','맡았습니다','만들었습니다','관리했습니다','책임졌습니다']

print('=== PORTFOLIO COPY AUDIT V1.5 ===')
all_text = ''
for fn in FILES:
    raw = Path(fn).read_text(encoding='utf-8')
    p = VisibleText(); p.feed(raw)
    text = re.sub(r'[ \t]+', ' ', ''.join(p.parts))
    text = re.sub(r'\n+', '\n', text)
    lines = [x.strip() for x in text.split('\n') if x.strip()]
    all_text += '\n' + '\n'.join(lines)
    print(f'\n## {fn}')
    for cat, pats in PATTERNS.items():
        hits = []
        for line in lines:
            if any(re.search(pat, line, re.I) for pat in pats):
                hits.append(line)
        if hits:
            print(f'[{cat}] {len(hits)}')
            for h in hits[:30]: print(' -', h)
    long_lines = [x for x in lines if len(x) >= 95 and not x.startswith(('Browser','React Native','Public APIs'))]
    if long_lines:
        print(f'[LONG] {len(long_lines)}')
        for h in long_lines[:20]: print(f' - ({len(h)}) {h}')

print('\n=== VERB COUNTS ===')
for v in VERBS:
    c = all_text.count(v)
    if c: print(f'{v}: {c}')

print('\n=== GLOBAL PHRASE COUNTS ===')
for phrase in ['연결', '검증', '개선', '실제', '사용자', '데이터', '서비스', '프로젝트', '근거']:
    print(f'{phrase}: {all_text.count(phrase)}')

print('\nAUDIT_DONE')
