#!/usr/bin/env python3
"""Patch main top-level pages with light/dark mode toggle."""
import os, re

TARGET_PAGES = [
    '/Users/carolineyakar/Desktop/aivelocity-website/strategies.html',
    '/Users/carolineyakar/Desktop/aivelocity-website/charts.html',
    '/Users/carolineyakar/Desktop/aivelocity-website/index.html',
    '/Users/carolineyakar/Desktop/aivelocity-website/about-us.html',
]

TOGGLE_BTN = '''        <button class="theme-toggle" id="themeToggle" aria-label="Toggle light/dark mode" title="Toggle light/dark mode">
          <span class="theme-toggle-icon theme-icon-dark">\U0001f319</span>
          <span class="theme-toggle-icon theme-icon-light">\u2600\ufe0f</span>
        </button>'''

TOGGLE_CSS = '''
  <style id="theme-toggle-styles">
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
    body:not(.light-mode) .theme-icon-light { display: none; }
    body:not(.light-mode) .theme-icon-dark  { display: inline; }
    body.light-mode .theme-icon-dark  { display: none; }
    body.light-mode .theme-icon-light { display: inline; }

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
    body.light-mode .footer {
      background-color: #e8ecf0 !important;
      border-top-color: #d1d5db !important;
    }
    body.light-mode .footer-tagline,
    body.light-mode .footer-link,
    body.light-mode .footer-copyright { color: #5A6A7E !important; }
    body.light-mode .footer-heading { color: #0b1d3a !important; }
    body.light-mode .nav-brand-name.footer-brand-name { color: #0b1d3a !important; }

    /* Strategies page */
    body.light-mode .page-hero {
      background: linear-gradient(135deg,#1b4d3e 0%,#0b1d3a 100%) !important;
    }
    body.light-mode .strategy-card {
      background: #ffffff !important;
      border-color: #d1d5db !important;
      box-shadow: 0 2px 8px rgba(0,0,0,0.08) !important;
    }
    body.light-mode .strategy-card h2 { color: #111827 !important; }
    body.light-mode .strategy-card p { color: #374151 !important; }
    body.light-mode .strategy-card-label { color: #6B7280 !important; }
    body.light-mode .comparison-section {
      background: #ffffff !important;
      border-color: #d1d5db !important;
    }
    body.light-mode .comparison-section h2 { color: #111827 !important; }
    body.light-mode .comparison-section .subtitle { color: #6B7280 !important; }
    body.light-mode .legend { border-top-color: #e5e7eb !important; }
    body.light-mode .legend-label { color: #6B7280 !important; }
    body.light-mode .legend-value { color: #111827 !important; }
    body.light-mode .page-footer-note { color: #6B7280 !important; border-top-color: #e5e7eb !important; }
    body.light-mode .strategy-link-secondary {
      color: #2A5CB3 !important;
      border-color: rgba(42,92,179,0.4) !important;
    }

    /* Charts overview page */
    body.light-mode .chart-hero {
      background: linear-gradient(135deg,#1b4d3e 0%,#0b1d3a 100%) !important;
    }
    body.light-mode .chart-card {
      background: #ffffff !important;
      border-color: #d1d5db !important;
    }
    body.light-mode .chart-card h2,
    body.light-mode .chart-card h3 { color: #111827 !important; }
    body.light-mode .chart-card p { color: #6B7280 !important; }

    /* Index / home page */
    body.light-mode .hero-section {
      background: linear-gradient(135deg,#1b4d3e 0%,#0b1d3a 100%) !important;
    }
    body.light-mode .section-card,
    body.light-mode .feature-card,
    body.light-mode .metric-card {
      background: #ffffff !important;
      border-color: #d1d5db !important;
    }
    body.light-mode .section-card h2,
    body.light-mode .section-card h3,
    body.light-mode .feature-card h3,
    body.light-mode .metric-card h3 { color: #111827 !important; }
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
      background: #ffffff !important;
      border-color: #d1d5db !important;
    }
    body.light-mode .about-card h2,
    body.light-mode .about-card h3,
    body.light-mode .team-card h3,
    body.light-mode .value-card h3 { color: #111827 !important; }
    body.light-mode .about-card p,
    body.light-mode .team-card p,
    body.light-mode .value-card p { color: #374151 !important; }

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

TOGGLE_JS = '''
  <script id="theme-toggle-script">
    (function() {
      var STORAGE_KEY = 'aiv-theme';
      var btn = document.getElementById('themeToggle');
      var saved = localStorage.getItem(STORAGE_KEY);
      if (saved === 'light') document.body.classList.add('light-mode');

      function toggle() {
        var isLight = document.body.classList.toggle('light-mode');
        localStorage.setItem(STORAGE_KEY, isLight ? 'light' : 'dark');
      }
      if (btn) {
        btn.addEventListener('click', toggle);
      } else {
        document.addEventListener('DOMContentLoaded', function() {
          var b = document.getElementById('themeToggle');
          if (b) b.addEventListener('click', toggle);
        });
      }
    })();
  </script>'''

contact_pattern = r'(<a href="mailto:info@aivelocityfund\.com"[^>]*class="nav-link"[^>]*>Contact</a>)'

for fpath in TARGET_PAGES:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    if 'theme-toggle-styles' in content:
        print('SKIP (already patched): ' + os.path.basename(fpath))
        continue

    if '</head>' in content:
        content = content.replace('</head>', TOGGLE_CSS + '\n</head>', 1)

    if re.search(contact_pattern, content):
        content = re.sub(contact_pattern, r'\1\n' + TOGGLE_BTN, content, count=1)
    else:
        print('  WARNING: no Contact link found in ' + os.path.basename(fpath))

    if '</body>' in content:
        content = content.replace('</body>', TOGGLE_JS + '\n</body>', 1)

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)
    print('Patched: ' + os.path.basename(fpath))

# Also fix d1l1r1.html - has CSS/JS but missing the button
r1_path = '/Users/carolineyakar/Desktop/aivelocity-website/reports/d1l1r1.html'
with open(r1_path, 'r', encoding='utf-8') as f:
    content = f.read()

if 'id="themeToggle"' not in content:
    # This page uses a different nav structure - inject a floating button instead
    FLOATING_BTN = '''
  <button class="theme-toggle" id="themeToggle" aria-label="Toggle light/dark mode" title="Toggle light/dark mode" style="position:fixed;top:1rem;right:1rem;z-index:9999;">
    <span class="theme-toggle-icon theme-icon-dark">\U0001f319</span>
    <span class="theme-toggle-icon theme-icon-light">\u2600\ufe0f</span>
  </button>'''
    content = content.replace('<body>
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-WCG69XDQ"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>', '<body>
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-WCG69XDQ"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>' + FLOATING_BTN, 1)
    with open(r1_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print('Patched (floating btn): reports/d1l1r1.html')
else:
    print('SKIP (btn already present): reports/d1l1r1.html')

print('\nAll done!')
