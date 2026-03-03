#!/usr/bin/env python3
"""
AI Velocity Fund - Add Dark/Light Mode Toggle to all Strategy, Chart, and Backtest pages.
Run: python3 add_dark_mode_toggle.py
"""
import os, glob, re

# ── The toggle button HTML to inject into the navbar (before </div> of nav-menu) ──
TOGGLE_BTN = '''        <button class="theme-toggle" id="themeToggle" aria-label="Toggle light/dark mode" title="Toggle light/dark mode">
          <span class="theme-toggle-icon theme-icon-dark">🌙</span>
          <span class="theme-toggle-icon theme-icon-light">☀️</span>
        </button>'''

# ── CSS to inject into <head>
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-WCG69XDQ');</script> (inside a <style> block) ──
TOGGLE_CSS = '''
  <style id="theme-toggle-styles">
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

    /* ── Light Mode Overrides ── */
    body.light-mode {
      background-color: #f5f7fa !important;
      color: #1a2035 !important;
    }
    body.light-mode .navbar {
      background-color: rgba(245,247,250,0.92) !important;
      border-bottom: 1px solid #d1d5db !important;
    }
    body.light-mode .navbar-signal-line { background-color: #2A5CB3 !important; }
    body.light-mode .nav-brand-name { color: #0b1d3a !important; }
    body.light-mode .nav-brand-fund { color: #5A6A7E !important; }
    body.light-mode .nav-link,
    body.light-mode .nav-dropdown-toggle { color: #374151 !important; }
    body.light-mode .nav-link:hover,
    body.light-mode .nav-dropdown-toggle:hover { color: #0b1d3a !important; }
    body.light-mode .nav-dropdown-menu {
      background-color: #ffffff !important;
      border-color: #d1d5db !important;
    }
    body.light-mode .nav-dropdown-link { color: #374151 !important; }
    body.light-mode .nav-dropdown-link:hover {
      background-color: #f3f4f6 !important;
      color: #0b1d3a !important;
    }
    body.light-mode .nav-toggle-line { background-color: #0b1d3a !important; }
    body.light-mode .theme-toggle {
      border-color: rgba(0,0,0,0.15) !important;
      background: rgba(0,0,0,0.05) !important;
    }
    body.light-mode .theme-toggle:hover {
      background: rgba(0,0,0,0.1) !important;
    }

    /* Footer */
    body.light-mode .footer {
      background-color: #e8ecf0 !important;
      border-top-color: #d1d5db !important;
    }
    body.light-mode .footer-tagline,
    body.light-mode .footer-link,
    body.light-mode .footer-copyright { color: #5A6A7E !important; }
    body.light-mode .footer-heading { color: #0b1d3a !important; }
    body.light-mode .nav-brand-name.footer-brand-name { color: #0b1d3a !important; }

    /* ── Report pages (light-mode on already-light pages) ── */
    body.light-mode .report-hero {
      background: linear-gradient(135deg,#1b4d3e 0%,#0b1d3a 100%) !important;
    }
    body.light-mode .stat-card {
      background: #ffffff !important;
      border-color: #d1d5db !important;
    }
    body.light-mode .report-table-card {
      background: #ffffff !important;
      border-color: #d1d5db !important;
    }
    body.light-mode td { color: #374151 !important; }
    body.light-mode td:first-child { color: #111827 !important; }
    body.light-mode tbody tr:hover { background: #f9fafb !important; }
    body.light-mode .report-table-header h2 { color: #111827 !important; }
    body.light-mode .report-footer-note { color: #6B7280 !important; border-top-color: #e5e7eb !important; }

    /* ── Chart pages (light-mode on already-light pages) ── */
    body.light-mode .chart-card {
      background: #ffffff !important;
      box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1) !important;
    }
    body.light-mode .chart-card-title-block h2 { color: #111827 !important; }
    body.light-mode .chart-card-title-block p { color: #6B7280 !important; }
    body.light-mode .time-selector { background: #f9fafb !important; }
    body.light-mode .time-btn { background: #ffffff !important; color: #111827 !important; }
    body.light-mode .time-btn.active { background: #1b4d3e !important; color: #ffffff !important; }
    body.light-mode .chart-wrapper { border-color: #e5e7eb !important; background: #fafafa !important; }
    body.light-mode .chart-legend { border-top-color: #e5e7eb !important; }
    body.light-mode .chart-legend-item { background: #f9fafb !important; }
    body.light-mode .chart-legend-label { color: #6B7280 !important; }
    body.light-mode .chart-legend-value { color: #111827 !important; }
    body.light-mode .chart-hint { background: #f9fafb !important; color: #6B7280 !important; }

    /* ── Backtest pages (dark → light) ── */
    body.light-mode .backtest-hero {
      background: linear-gradient(135deg,#1b4d3e 0%,#0b1d3a 100%) !important;
    }
    body.light-mode .backtest-container { color: #1a2035 !important; }
    body.light-mode .highlight-box {
      background: #ffffff !important;
      border-color: #d1d5db !important;
    }
    body.light-mode .highlight-box h3 { color: #0b1d3a !important; }
    body.light-mode .highlight-param {
      background: #f3f4f6 !important;
      border-color: #d1d5db !important;
    }
    body.light-mode .highlight-param-label { color: #374151 !important; }
    body.light-mode .highlight-param-value { color: #2A5CB3 !important; }
    body.light-mode .stats-grid .stat-card,
    body.light-mode .stats-hero .stat-card {
      background: #ffffff !important;
      border-color: #d1d5db !important;
      box-shadow: 0 2px 8px rgba(0,0,0,0.08) !important;
    }
    body.light-mode .stat-card.highlight {
      background: linear-gradient(135deg,#059669,#10b981) !important;
      border: none !important;
    }
    body.light-mode .stat-label,
    body.light-mode .stat-card .label { color: #6B7280 !important; }
    body.light-mode .stat-value,
    body.light-mode .stat-card .value { color: #111827 !important; }
    body.light-mode .stat-card.highlight .label,
    body.light-mode .stat-card.highlight .value,
    body.light-mode .stat-card.highlight .subtext { color: #ffffff !important; }
    body.light-mode .chart-card.backtest-chart,
    body.light-mode .chart-card {
      background: #ffffff !important;
      border-color: #d1d5db !important;
    }
    body.light-mode .chart-card h3 { color: #0b1d3a !important; }
    body.light-mode .params-section {
      background: #ffffff !important;
      border-color: #d1d5db !important;
    }
    body.light-mode .params-section h3 { color: #0b1d3a !important; }
    body.light-mode .param-item {
      background: #f3f4f6 !important;
      border-color: #d1d5db !important;
    }
    body.light-mode .param-name { color: #374151 !important; }
    body.light-mode .param-value { color: #2A5CB3 !important; }
    body.light-mode .comparison-table th { background: #1b4d3e !important; color: #ffffff !important; }
    body.light-mode .comparison-table td { color: #374151 !important; }
    body.light-mode .comparison-table tr:hover td { background: rgba(27,77,62,0.05) !important; }
    body.light-mode .backtest-section {
      background: #ffffff !important;
      border-color: #d1d5db !important;
    }
    body.light-mode .backtest-section h2,
    body.light-mode .backtest-section h3 { color: #0b1d3a !important; }
    body.light-mode .backtest-section th { background: #f3f4f6 !important; color: #374151 !important; }
    body.light-mode .backtest-section td { color: #374151 !important; }
    body.light-mode .backtest-section tr:hover td { background: rgba(27,77,62,0.05) !important; }
    body.light-mode .config-box,
    body.light-mode .risk-card { background: #f3f4f6 !important; border-color: #d1d5db !important; }
    body.light-mode .config-item .label,
    body.light-mode .risk-card h4 { color: #6B7280 !important; }
    body.light-mode .config-item .value { color: #c55000 !important; }
    body.light-mode .risk-card .value { color: #111827 !important; }
    body.light-mode .progress-bar { background: #e5e7eb !important; border-color: #d1d5db !important; }
    body.light-mode .progress-label { color: #374151 !important; }
    body.light-mode .alert-success { background: rgba(16,185,129,0.08) !important; }
    body.light-mode .alert-warning { background: rgba(245,158,11,0.08) !important; }
    body.light-mode .alert-content h4 { color: #111827 !important; }
    body.light-mode .alert-content p { color: #374151 !important; }
    body.light-mode .recommendation-box {
      background: linear-gradient(135deg,rgba(27,77,62,0.06),rgba(11,29,58,0.06)) !important;
    }
    body.light-mode .recommendation-box h3 { color: #0b1d3a !important; }
    body.light-mode .recommendation-box .big-value { color: #1b4d3e !important; }
    body.light-mode .recommendation-box .subtitle-text { color: #6B7280 !important; }
    body.light-mode .backtest-footer { color: #6B7280 !important; border-top-color: #d1d5db !important; }
    body.light-mode .badge { color: #ffffff !important; }

    /* Chart container backgrounds in dark backtest pages */
    body.light-mode .chart-container { background: #f3f4f6 !important; }

    /* Dark-mode chart pages that have dark hero/card */
    body.light-mode .chart-hero {
      background: linear-gradient(135deg,#1b4d3e 0%,#0b1d3a 100%) !important;
    }

    /* Mobile nav in light mode */
    @media (max-width: 768px) {
      body.light-mode .nav-menu {
        background-color: #ffffff !important;
        border-left-color: #d1d5db !important;
      }
      body.light-mode .nav-link { border-bottom-color: #e5e7eb !important; }
      body.light-mode .nav-dropdown-toggle { border-bottom-color: #e5e7eb !important; }
      body.light-mode .nav-dropdown-menu { background-color: #f9fafb !important; }
    }
  </style>'''

# ── JS to inject before </body> ──
TOGGLE_JS = '''
  <script id="theme-toggle-script">
    (function() {
      var STORAGE_KEY = 'aiv-theme';
      var btn = document.getElementById('themeToggle');
      // Apply saved preference immediately
      var saved = localStorage.getItem(STORAGE_KEY);
      if (saved === 'light') document.body.classList.add('light-mode');

      function toggle() {
        var isLight = document.body.classList.toggle('light-mode');
        localStorage.setItem(STORAGE_KEY, isLight ? 'light' : 'dark');
      }
      if (btn) {
        btn.addEventListener('click', toggle);
      } else {
        // If btn not yet in DOM (e.g. nav loaded async), wait
        document.addEventListener('DOMContentLoaded', function() {
          var b = document.getElementById('themeToggle');
          if (b) b.addEventListener('click', toggle);
        });
      }
    })();
  </script>'''


def inject_toggle(content, filepath):
    """Inject toggle CSS, button, and JS into an HTML file."""
    changed = False

    # Skip if already patched
    if 'theme-toggle-styles' in content:
        print(f'  SKIP (already patched): {filepath}')
        return content

    # 1. Inject CSS before </head>
    if '</head>' in content:
        content = content.replace('</head>', TOGGLE_CSS + '\n</head>', 1)
        changed = True

    # 2. Inject toggle button inside nav-menu (before the closing </div> of nav-menu)
    #    We look for the last nav-link (Contact) and insert after it
    contact_pattern = r'(<a href="mailto:info@aivelocityfund\.com"[^>]*class="nav-link"[^>]*>Contact</a>)'
    if re.search(contact_pattern, content):
        content = re.sub(
            contact_pattern,
            r'\1\n' + TOGGLE_BTN,
            content,
            count=1
        )
        changed = True

    # 3. Inject JS before </body>
    if '</body>' in content:
        content = content.replace('</body>', TOGGLE_JS + '\n</body>', 1)
        changed = True

    if changed:
        print(f'  Patched: {filepath}')
    else:
        print(f'  WARNING - no changes made: {filepath}')

    return content


def process_files():
    base = '/Users/carolineyakar/Desktop/aivelocity-website'
    patterns = [
        'backtests/*.html',
        'charts/*.html',
        'reports/*.html',
    ]
    all_files = []
    for pat in patterns:
        all_files.extend(glob.glob(os.path.join(base, pat)))

    print(f'Found {len(all_files)} files to process...\n')
    patched = 0
    skipped = 0

    for fpath in sorted(all_files):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        if 'theme-toggle-styles' in content:
            print(f'  SKIP (already patched): {os.path.relpath(fpath, base)}')
            skipped += 1
            continue

        new_content = inject_toggle(content, os.path.relpath(fpath, base))
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        patched += 1

    print(f'\nDone! {patched} files patched, {skipped} already patched.')


if __name__ == '__main__':
    print('AI Velocity Fund - Dark/Light Mode Toggle Injector')
    print('=' * 50)
    process_files()
