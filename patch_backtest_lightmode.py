#!/usr/bin/env python3
"""Patch backtest pages with additional light-mode text color overrides."""
import os, glob

EXTRA_OVERRIDES = (
    '\n    /* -- Additional backtest text color overrides -- */\n'
    '    body.light-mode .backtest-hero h1 { color: #ffffff !important; }\n'
    '    body.light-mode .backtest-hero p { color: rgba(255,255,255,0.85) !important; }\n'
    '    body.light-mode .highlight-box h3 { color: #0b1d3a !important; }\n'
    '    body.light-mode .stat-label { color: #6B7280 !important; }\n'
    '    body.light-mode .stat-value { color: #111827 !important; }\n'
    '    body.light-mode .stat-value.positive { color: #059669 !important; }\n'
    '    body.light-mode .stat-value.negative { color: #dc2626 !important; }\n'
    '    body.light-mode .chart-card h3 { color: #0b1d3a !important; }\n'
    '    body.light-mode .params-section h3 { color: #0b1d3a !important; }\n'
    '    body.light-mode .param-name { color: #374151 !important; }\n'
    '    body.light-mode .param-value { color: #2A5CB3 !important; }\n'
    '    body.light-mode .highlight-param-label { color: #374151 !important; }\n'
    '    body.light-mode .highlight-param-value { color: #2A5CB3 !important; }\n'
    '    body.light-mode .comparison-table td { color: #374151 !important; }\n'
    '    body.light-mode .comparison-table th { color: #374151 !important; background: #f3f4f6 !important; }\n'
    '    body.light-mode .comparison-table .positive { color: #059669 !important; }\n'
    '    body.light-mode .comparison-table .negative { color: #dc2626 !important; }\n'
    '    body.light-mode .backtest-footer { color: #6B7280 !important; border-top-color: #e5e7eb !important; }\n'
    '    body.light-mode .badge { background: rgba(42,92,179,0.1) !important; color: #2A5CB3 !important; border-color: rgba(42,92,179,0.3) !important; }\n'
    '    body.light-mode .badge-success { background: rgba(5,150,105,0.1) !important; color: #059669 !important; }\n'
    '    body.light-mode .badge-danger { background: rgba(220,38,38,0.1) !important; color: #dc2626 !important; }\n'
)

base = '/Users/carolineyakar/Desktop/aivelocity-website'
files = glob.glob(os.path.join(base, 'backtests/*.html'))

patched = 0
for fpath in sorted(files):
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    if 'Additional backtest text color overrides' in content:
        print('  SKIP (already patched): ' + os.path.relpath(fpath, base))
        continue

    idx = content.find('<style id="theme-toggle-styles">')
    if idx == -1:
        print('  SKIP (no theme-toggle-styles): ' + os.path.relpath(fpath, base))
        continue

    close_idx = content.find('</style>', idx)
    if close_idx == -1:
        print('  SKIP (no closing style tag): ' + os.path.relpath(fpath, base))
        continue

    new_content = content[:close_idx] + EXTRA_OVERRIDES + content[close_idx:]

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print('  Patched: ' + os.path.relpath(fpath, base))
    patched += 1

print('\nDone! ' + str(patched) + ' backtest files updated.')
