import os

files = []
for d in ['backtests', 'reports']:
    for f in os.listdir(d):
        if f.endswith('.html'):
            files.append(os.path.join(d, f))
files.append('strategies.html')

for filepath in files:
    with open(filepath) as f:
        content = f.read()
    lines = content.split('\n')
    matches = []
    for i, line in enumerate(lines):
        if 'borderColor' in line or 'backgroundColor' in line:
            matches.append((i+1, line.strip()[:100]))
    if matches:
        print(f'=== {filepath} ===')
        for ln, line in matches[:5]:
            print(f'  {ln}: {line}')
