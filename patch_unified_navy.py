#!/usr/bin/env python3
"""
patch_unified_navy.py
Unified Navy Light Mode: Navy background (#040911) + Pure White cards (#FFFFFF) + Navy text (#040911)
Electric Cobalt (#2A5CB3) for metric numbers in light mode.
"""

import os
import re

# ── The unified light-mode block to inject into every page ──────────────────
UNIFIED_LIGHT_MODE_CSS = """
    /* ── Light Mode Overrides ── */
    body.light-mode {
      background-color: #040911 !important;
      color: #040911 !important;
    }
    body.light-mode .navbar {
      background-color: rgba(4,9,17,0.96) !important;
      border-bottom: 1px solid rgba(42,92,179,0.3) !important;
    }
    body.light-mode .navbar-signal-line { background-color: #2A5CB3 !important; }
    body.light-mode .nav-brand-name { color: #ffffff !important; }
    body.light-mode .nav-brand-fund { color: #A0ABBE !important; }
    body.light-mode .nav-link,
    body.light-mode .nav-dropdown-toggle { color: #C8CDD8 !important; }
    body.light-mode .nav-link:hover,
    body.light-mode .nav-dropdown-toggle:hover { color: #ffffff !important; }
    body.light-mode .nav-dropdown-menu {
      background-color: #0D1525 !important;
      border-color: rgba(42,92,179,0.3) !important;
    }
    body.light-mode .nav-dropdown-link { color: #C8CDD8 !important; }
    body.light-mode .nav-dropdown-link:hover {
      background-color: rgba(42,92,179,0.1) !important;
      color: #ffffff !important;
    }
    body.light-mode .nav-toggle-line { background-color: #ffffff !important; }
    body.light-mode .theme-toggle {
      border-color: rgba(255,255,255,0.2) !important;
      background: rgba(255,255,255,0.08) !important;
    }
    body.light-mode .theme-toggle:hover {
      background: rgba(255,255,255,0.15) !important;
    }

    /* Footer */
    body.light-mode .footer {
      background-color: #0D1525 !important;
      border-top-color: rgba(42,92,179,0.2) !important;
    }
    body.light-mode .footer-tagline,
    body.light-mode .footer-link,
    body.light-mode .footer-copyright { color: #A0ABBE !important; }
    body.light-mode .footer-heading { color: #ffffff !important; }
    body.light-mode .nav-brand-name.footer-brand-name { color: #ffffff !important; }

    /* ── White Cards on Navy Background ── */
    /* Report stat cards */
    body.light-mode .stat-card {
      background: #FFFFFF !important;
      border-color: #D1D9E6 !important;
      box-shadow: 0 4px 16px rgba(0,0,0,0.25) !important;
    }
    body.light-mode .stat-card h3 { color: #6B7280 !important; }
    body.light-mode .stat-card p { color: #040911 !important; }
    body.light-mode .stat-card.positive p { color: #059669 !important; }
    body.light-mode .stat-card.negative p { color: #dc2626 !important; }

    /* Report table card */
    body.light-mode .report-table-card {
      background: #FFFFFF !important;
      border-color: #D1D9E6 !important;
      box-shadow: 0 4px 16px rgba(0,0,0,0.25) !important;
    }
    body.light-mode .report-table-header h2 { color: #040911 !important; }
    body.light-mode td { color: #374151 !important; }
    body.light-mode td:first-child { color: #040911 !important; }
    body.light-mode tbody tr:hover td { background: #f9fafb !important; }
    body.light-mode .report-footer-note { color: #6B7280 !important; border-top-color: #e5e7eb !important; }

    /* Report hero */
    body.light-mode .report-hero {
      background: linear-gradient(135deg,#1b4d3e 0%,#0b1d3a 100%) !important;
    }

    /* Chart pages */
    body.light-mode .chart-hero {
      background: #0D1525 !important;
      border-color: rgba(42,92,179,0.3) !important;
    }
    body.light-mode .chart-hero .chart-hero-title { color: #ffffff !important; }
    body.light-mode .chart-hero .chart-hero-subtitle { color: #A0ABBE !important; }
    body.light-mode .chart-card {
      background: #FFFFFF !important;
      border-color: #D1D9E6 !important;
      box-shadow: 0 4px 16px rgba(0,0,0,0.25) !important;
    }
    body.light-mode .chart-card-title-block h2 { color: #040911 !important; }
    body.light-mode .chart-card-title-block p { color: #6B7280 !important; }
    body.light-mode .time-selector { background: #f3f4f6 !important; border-color: #D1D9E6 !important; }
    body.light-mode .time-btn { background: #ffffff !important; color: #374151 !important; border-color: #D1D9E6 !important; }
    body.light-mode .time-btn.active { background: #2A5CB3 !important; color: #ffffff !important; border-color: #2A5CB3 !important; }
    body.light-mode .chart-wrapper { border-color: #D1D9E6 !important; background: #f9fafb !important; }
    body.light-mode .chart-legend { border-top-color: #D1D9E6 !important; }
    body.light-mode .chart-legend-item { background: #f3f4f6 !important; border-color: #D1D9E6 !important; }
    body.light-mode .chart-legend-label { color: #6B7280 !important; }
    body.light-mode .chart-legend-value { color: #040911 !important; }
    body.light-mode .chart-legend-value.positive { color: #059669 !important; }
    body.light-mode .chart-legend-value.negative { color: #dc2626 !important; }
    body.light-mode .chart-hint { background: #f3f4f6 !important; color: #6B7280 !important; border-color: #D1D9E6 !important; }

    /* Strategies page */
    body.light-mode .page-hero {
      background: #0D1525 !important;
      border-color: rgba(42,92,179,0.3) !important;
    }
    body.light-mode .page-hero h1 { color: #ffffff !important; }
    body.light-mode .page-hero p { color: #A0ABBE !important; }
    body.light-mode .strategy-card {
      background: #FFFFFF !important;
      border-color: #D1D9E6 !important;
      box-shadow: 0 4px 16px rgba(0,0,0,0.25) !important;
    }
    body.light-mode .strategy-card h2 { color: #040911 !important; }
    body.light-mode .strategy-card p { color: #374151 !important; }
    body.light-mode .strategy-card-label { color: #6B7280 !important; }
    body.light-mode .comparison-section {
      background: #FFFFFF !important;
      border-color: #D1D9E6 !important;
      box-shadow: 0 4px 16px rgba(0,0,0,0.25) !important;
    }
    body.light-mode .comparison-section h2 { color: #040911 !important; }
    body.light-mode .comparison-section .subtitle { color: #6B7280 !important; }
    body.light-mode .legend { border-top-color: #D1D9E6 !important; }
    body.light-mode .legend-label { color: #6B7280 !important; }
    body.light-mode .legend-value { color: #040911 !important; }
    body.light-mode .page-footer-note { color: #6B7280 !important; border-top-color: rgba(42,92,179,0.2) !important; }
    body.light-mode .strategy-link-secondary {
      color: #2A5CB3 !important;
      border-color: rgba(42,92,179,0.4) !important;
    }

    /* Index / home page */
    body.light-mode .hero-section {
      background: linear-gradient(135deg,#1b4d3e 0%,#0b1d3a 100%) !important;
    }
    body.light-mode .section-card,
    body.light-mode .feature-card,
    body.light-mode .metric-card {
      background: #FFFFFF !important;
      border-color: #D1D9E6 !important;
      box-shadow: 0 4px 16px rgba(0,0,0,0.25) !important;
    }
    body.light-mode .section-card h2,
    body.light-mode .section-card h3,
    body.light-mode .feature-card h3,
    body.light-mode .metric-card h3 { color: #040911 !important; }
    body.light-mode .section-card p,
    body.light-mode .feature-card p,
    body.light-mode .metric-card p { color: #374151 !important; }

    /* About page */
    body.light-mode .about-hero {
      background: linear-gradient(135deg,#1b4d3e 0%,#0b1d3a 100%) !important;
    }
    body.light-mode .about-card,
    body.light-mode .team-card,
    body.light-mode .value-card {
      background: #FFFFFF !important;
      border-color: #D1D9E6 !important;
      box-shadow: 0 4px 16px rgba(0,0,0,0.25) !important;
    }
    body.light-mode .about-card h2,
    body.light-mode .about-card h3,
    body.light-mode .team-card h3,
    body.light-mode .value-card h3 { color: #040911 !important; }
    body.light-mode .about-card p,
    body.light-mode .team-card p,
    body.light-mode .value-card p { color: #374151 !important; }

    /* ── Backtest pages ── */
    body.light-mode .backtest-hero {
      background: linear-gradient(135deg,#1b4d3e 0%,#0b1d3a 100%) !important;
    }
    body.light-mode .backtest-hero h1 { color: #ffffff !important; }
    body.light-mode .backtest-hero p { color: rgba(255,255,255,0.85) !important; }
    body.light-mode .backtest-container { color: #040911 !important; }
    body.light-mode .backtest-section {
      background: #FFFFFF !important;
      border-color: #D1D9E6 !important;
      box-shadow: 0 4px 16px rgba(0,0,0,0.25) !important;
    }
    body.light-mode .backtest-section h2,
    body.light-mode .backtest-section h3 { color: #040911 !important; }
    body.light-mode .backtest-section th { background: #f3f4f6 !important; color: #374151 !important; }
    body.light-mode .backtest-section td { color: #374151 !important; }
    body.light-mode .backtest-section tr:hover td { background: rgba(42,92,179,0.04) !important; }
    /* Stat cards in backtests - White with Cobalt metrics */
    body.light-mode .stats-hero .stat-card,
    body.light-mode .stats-grid .stat-card {
      background: #FFFFFF !important;
      border-color: #D1D9E6 !important;
      box-shadow: 0 4px 16px rgba(0,0,0,0.25) !important;
    }
    body.light-mode .stats-hero .stat-card .label,
    body.light-mode .stats-grid .stat-card .label { color: #6B7280 !important; }
    body.light-mode .stats-hero .stat-card .value,
    body.light-mode .stats-grid .stat-card .value { color: #2A5CB3 !important; }
    body.light-mode .stats-hero .stat-card .subtext,
    body.light-mode .stats-grid .stat-card .subtext { color: #6B7280 !important; }
    body.light-mode .stat-card.highlight {
      background: linear-gradient(135deg,#059669,#10b981) !important;
      border: none !important;
    }
    body.light-mode .stat-card.highlight .label,
    body.light-mode .stat-card.highlight .value,
    body.light-mode .stat-card.highlight .subtext { color: #ffffff !important; }
    body.light-mode .config-box,
    body.light-mode .risk-card {
      background: #f3f4f6 !important;
      border-color: #D1D9E6 !important;
    }
    body.light-mode .config-item .label,
    body.light-mode .risk-card h4 { color: #6B7280 !important; }
    body.light-mode .config-item .value { color: #2A5CB3 !important; }
    body.light-mode .risk-card .value { color: #2A5CB3 !important; }
    body.light-mode .progress-bar { background: #e5e7eb !important; border-color: #D1D9E6 !important; }
    body.light-mode .progress-label { color: #374151 !important; }
    body.light-mode .alert-success { background: rgba(16,185,129,0.08) !important; }
    body.light-mode .alert-warning { background: rgba(245,158,11,0.08) !important; }
    body.light-mode .alert-content h4 { color: #040911 !important; }
    body.light-mode .alert-content p { color: #374151 !important; }
    body.light-mode .recommendation-box {
      background: rgba(255,255,255,0.05) !important;
      border-color: rgba(42,92,179,0.3) !important;
    }
    body.light-mode .recommendation-box h3 { color: #ffffff !important; }
    body.light-mode .recommendation-box .big-value { color: #2A5CB3 !important; }
    body.light-mode .recommendation-box .subtitle-text { color: #A0ABBE !important; }
    body.light-mode .comparison-table th { background: #1b4d3e !important; color: #ffffff !important; }
    body.light-mode .comparison-table td { color: #374151 !important; }
    body.light-mode .comparison-table tr:hover td { background: rgba(42,92,179,0.04) !important; }
    body.light-mode .highlight-box {
      background: #FFFFFF !important;
      border-color: #D1D9E6 !important;
    }
    body.light-mode .highlight-box h3 { color: #040911 !important; }
    body.light-mode .highlight-param {
      background: #f3f4f6 !important;
      border-color: #D1D9E6 !important;
    }
    body.light-mode .highlight-param-label { color: #374151 !important; }
    body.light-mode .highlight-param-value { color: #2A5CB3 !important; }
    body.light-mode .params-section {
      background: #FFFFFF !important;
      border-color: #D1D9E6 !important;
    }
    body.light-mode .params-section h3 { color: #040911 !important; }
    body.light-mode .param-item {
      background: #f3f4f6 !important;
      border-color: #D1D9E6 !important;
    }
    body.light-mode .param-name { color: #374151 !important; }
    body.light-mode .param-value { color: #2A5CB3 !important; }
    body.light-mode .backtest-footer { color: #A0ABBE !important; border-top-color: rgba(42,92,179,0.2) !important; }
    body.light-mode .badge { background: rgba(42,92,179,0.15) !important; color: #2A5CB3 !important; border-color: rgba(42,92,179,0.3) !important; }
    body.light-mode .chart-container { background: #f3f4f6 !important; }

    /* Mobile nav in light mode */
    @media (max-width: 768px) {
      body.light-mode .nav-menu {
        background-color: #0D1525 !important;
        border-left-color: rgba(42,92,179,0.3) !important;
      }
      body.light-mode .nav-link { border-bottom-color: rgba(42,92,179,0.15) !important; }
      body.light-mode .nav-dropdown-toggle { border-bottom-color: rgba(42,92,179,0.15) !important; }
      body.light-mode .nav-dropdown-menu { background-color: #040911 !important; }
    }
"""

# ── Regex to find and replace the existing light-mode block ─────────────────
# Matches from the comment "/* ── Light Mode Overrides ── */" or just "body.light-mode {"
# through the closing </style> of the theme-toggle-styles block.

STYLE_BLOCK_PATTERN = re.compile(
    r'(<style[^>]*id=["\']theme-toggle-styles["\'][^>]*>)(.*?)(</style>)',
    re.DOTALL
)

# The toggle button CSS (kept unchanged)
TOGGLE_BTN_CSS = """
    /* ── Theme Toggle Button ── */
    .theme-toggle {
      display: flex;
      align-items: center;
      justify-content: center;
      width: 36px;
      height: 36px;
      border-radius: 50%;
      border: 1px solid rgba(255,255,255,0.15);
      background: rgba(255,255,255,0.06);
      cursor: pointer;
      font-size: 1rem;
      transition: background 0.2s, border-color 0.2s, transform 0.2s;
      margin-left: 0.5rem;
      flex-shrink: 0;
    }
    .theme-toggle:hover {
      background: rgba(255,255,255,0.12);
      border-color: rgba(255,255,255,0.3);
      transform: scale(1.1);
    }
    .theme-icon-dark, .theme-icon-light { line-height: 1; }
    /* Default (dark mode): show moon, hide sun */
    body:not(.light-mode) .theme-icon-light { display: none; }
    body:not(.light-mode) .theme-icon-dark  { display: inline; }
    /* Light mode: show sun, hide moon */
    body.light-mode .theme-icon-dark  { display: none; }
    body.light-mode .theme-icon-light { display: inline; }
"""

NEW_STYLE_BLOCK = '<style id="theme-toggle-styles">' + TOGGLE_BTN_CSS + UNIFIED_LIGHT_MODE_CSS + '\n  </style>'


def patch_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if 'theme-toggle-styles' not in content:
        print(f'  SKIP (no theme-toggle-styles): {filepath}')
        return False

    new_content = STYLE_BLOCK_PATTERN.sub(NEW_STYLE_BLOCK, content)

    if new_content == content:
        print(f'  UNCHANGED: {filepath}')
        return False

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f'  PATCHED: {filepath}')
    return True


def main():
    base = os.path.dirname(os.path.abspath(__file__))
    targets = []

    # Root HTML files
    for fname in os.listdir(base):
        if fname.endswith('.html'):
            targets.append(os.path.join(base, fname))

    # Subdirectories
    for subdir in ['reports', 'charts', 'backtests']:
        d = os.path.join(base, subdir)
        if os.path.isdir(d):
            for fname in os.listdir(d):
                if fname.endswith('.html'):
                    targets.append(os.path.join(d, fname))

    patched = 0
    for fp in sorted(targets):
        if patch_file(fp):
            patched += 1

    print(f'\nDone. {patched} files patched.')


if __name__ == '__main__':
    main()
