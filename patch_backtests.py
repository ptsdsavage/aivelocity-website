#!/usr/bin/env python3
"""Patch backtest pages: replace nav/footer placeholders with inline HTML."""
import re, os, glob

NAV = (
    '  <nav class="navbar" role="navigation" aria-label="Main navigation">\n'
    '    <div class="navbar-signal-line" aria-hidden="true"></div>\n'
    '    <div class="nav-container">\n'
    '      <a href="/" class="nav-brand-lockup">\n'
    '        <span class="nav-brand-name">AI VELOCITY</span>\n'
    '        <span class="nav-brand-fund">FUND</span>\n'
    '      </a>\n'
    '      <button class="nav-toggle" aria-label="Toggle navigation" aria-expanded="false">\n'
    '        <span class="nav-toggle-line"></span>\n'
    '        <span class="nav-toggle-line"></span>\n'
    '        <span class="nav-toggle-line"></span>\n'
    '      </button>\n'
    '      <div class="nav-menu">\n'
    '        <div class="nav-dropdown">\n'
    '          <button class="nav-dropdown-toggle" aria-expanded="false">\n'
    '            <span>Charts</span>\n'
    '            <svg class="nav-dropdown-icon" width="10" height="10" viewBox="0 0 12 12" fill="currentColor"><path d="M6 9L1 4h10z"/></svg>\n'
    '          </button>\n'
    '          <div class="nav-dropdown-menu">\n'
    '            <a href="/charts/d1l1s1" class="nav-dropdown-link">Delta Momentum</a>\n'
    '            <a href="/charts/d2l1s1" class="nav-dropdown-link">Delta Reversal</a>\n'
    '            <a href="/charts/n1l1s1" class="nav-dropdown-link">Neutral Alpha</a>\n'
    '          </div>\n'
    '        </div>\n'
    '        <div class="nav-dropdown">\n'
    '          <button class="nav-dropdown-toggle" aria-expanded="false">\n'
    '            <span>Strategies</span>\n'
    '            <svg class="nav-dropdown-icon" width="10" height="10" viewBox="0 0 12 12" fill="currentColor"><path d="M6 9L1 4h10z"/></svg>\n'
    '          </button>\n'
    '          <div class="nav-dropdown-menu">\n'
    '            <a href="/reports/d1l1" class="nav-dropdown-link">Delta Momentum</a>\n'
    '            <a href="/reports/d2l1" class="nav-dropdown-link">Delta Reversal</a>\n'
    '            <a href="/reports/n1l1" class="nav-dropdown-link">Neutral Alpha</a>\n'
    '          </div>\n'
    '        </div>\n'
    '        <div class="nav-dropdown">\n'
    '          <button class="nav-dropdown-toggle" aria-expanded="false">\n'
    '            <span>Backtests</span>\n'
    '            <svg class="nav-dropdown-icon" width="10" height="10" viewBox="0 0 12 12" fill="currentColor"><path d="M6 9L1 4h10z"/></svg>\n'
    '          </button>\n'
    '          <div class="nav-dropdown-menu">\n'
    '            <a href="/backtests/iron-butterfly-backtest" class="nav-dropdown-link">Iron Butterfly</a>\n'
    '            <a href="/backtests/mean-reversion-strategy" class="nav-dropdown-link">Mean Reversion</a>\n'
    '            <a href="/backtests/trade-on-daily-earnings-calls---short-only" class="nav-dropdown-link">Earnings Short</a>\n'
    '            <a href="/backtests/trade-on-earnings-calls---long-only" class="nav-dropdown-link">Earnings Long</a>\n'
    '          </div>\n'
    '        </div>\n'
    '        <a href="/about-us" class="nav-link">About</a>\n'
    '        <a href="mailto:info@aivelocityfund.com" class="nav-link">Contact</a>\n'
    '      </div>\n'
    '    </div>\n'
    '  </nav>'
)

FOOTER = (
    '  <footer class="footer">\n'
    '    <div class="footer-container">\n'
    '      <div class="footer-content">\n'
    '        <div class="footer-brand">\n'
    '          <a href="/"><img src="/images/Untitled-318-x-50-px.png" loading="lazy" alt="AI Velocity Fund" class="footer-logo"></a>\n'
    '          <p class="footer-tagline">Systematic alpha generation through algorithmic execution.</p>\n'
    '        </div>\n'
    '        <div class="footer-links">\n'
    '          <div class="footer-column">\n'
    '            <h4 class="footer-heading">Company</h4>\n'
    '            <a href="/about-us" class="footer-link">About</a>\n'
    '            <a href="mailto:info@aivelocityfund.com" class="footer-link">Contact</a>\n'
    '          </div>\n'
    '          <div class="footer-column">\n'
    '            <h4 class="footer-heading">Resources</h4>\n'
    '            <a href="/reports/d1l1" class="footer-link">Strategy</a>\n'
    '            <a href="/charts/d1l1s1" class="footer-link">Charts</a>\n'
    '          </div>\n'
    '        </div>\n'
    '      </div>\n'
    '      <div class="footer-bottom">\n'
    '        <p class="footer-copyright">&copy; 2025&ndash;2026 AI Velocity Fund, LLC. All Rights Reserved.</p>\n'
    '      </div>\n'
    '    </div>\n'
    '  </footer>'
)

CSS_INSERT = (
    '<link href="/css/normalize.css" rel="stylesheet" type="text/css">\n'
    '  <link href="/css/design-system.css" rel="stylesheet" type="text/css">\n'
    '  <link href="/css/layout.css" rel="stylesheet" type="text/css">'
)

files = glob.glob('backtests/*.html')
for fpath in files:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    content = re.sub(r'<div\s+id=["\']nav-placeholder["\']>\s*</div>', NAV, content)
    content = re.sub(r'<div\s+id=["\']footer-placeholder["\']>\s*</div>', FOOTER, content)

    if 'design-system.css' not in content:
        content = content.replace(
            '<link href="/css/normalize.css" rel="stylesheet" type="text/css">',
            CSS_INSERT
        )

    content = content.replace('G-G9L6L77LNM', 'G-QZQM3NQ9WY')

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)
    print('  Updated: ' + fpath)

print('\nDone! ' + str(len(files)) + ' backtest pages updated.')
