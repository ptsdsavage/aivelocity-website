import os

files = []
for d in ['backtests', 'reports']:
    for f in os.listdir(d):
        if f.endswith('.html'):
            files.append(os.path.join(d, f))
files.append('strategies.html')

for f in files:
    with open(f) as fp:
        content = fp.read()
    matches = [(i+1, line) for i, line in enumerate(content.split('\n')) if 'btn-primary' in line or 'btn-cta' in line]
    if matches:
        print(f'=== {f} ===')
        for ln, line in matches[:5]:
            print(f'  {ln}: {line.strip()[:100]}')
