#!/usr/bin/env python3
"""
AI Velocity Fund - Strategy Report Page Generator
Run: python3 update_reports.py
"""
import os

REPORTS = [
    {"filename":"d1l1","display_name":"Delta Momentum Live","account_name":"DanSavage1 Live","csv_file":"alpaca_portfolio_history_DanSavage1Live.csv"},
    {"filename":"d1p1","display_name":"Delta Momentum Paper 1","account_name":"DanSavage1 Paper 1","csv_file":"alpaca_portfolio_history_DanSavage1P1.csv"},
    {"filename":"d1p2","display_name":"Delta Momentum Paper 2","account_name":"DanSavage1 Paper 2","csv_file":"alpaca_portfolio_history_DanSavage1P2.csv"},
    {"filename":"d1p3","display_name":"Delta Momentum Paper 3","account_name":"DanSavage1 Paper 3","csv_file":"alpaca_portfolio_history_DanSavage1P3.csv"},
    {"filename":"d2l1","display_name":"Delta Reversal Live","account_name":"DanSavage2 Live","csv_file":"alpaca_portfolio_history_DanSavage2Live.csv"},
    {"filename":"d2p1","display_name":"Delta Reversal Paper 1","account_name":"DanSavage2 Paper 1","csv_file":"alpaca_portfolio_history_DanSavage2P1.csv"},
    {"filename":"n1l1","display_name":"Neutral Alpha Live","account_name":"Nikki Live","csv_file":"alpaca_portfolio_history_NikkiLive.csv"},
    {"filename":"n1p1","display_name":"Neutral Alpha Paper 1","account_name":"Nikki Paper 1","csv_file":"alpaca_portfolio_history_NikkiP1.csv"},
    {"filename":"n1p2","display_name":"Neutral Alpha Paper 2","account_name":"Nikki Paper 2","csv_file":"alpaca_portfolio_history_NikkiP2.csv"},
    {"filename":"n1p3","display_name":"Neutral Alpha Paper 3","account_name":"Nikki Paper 3","csv_file":"alpaca_portfolio_history_NikkiP3.csv"},
    {"filename":"aiv1P2","display_name":"AIV001 Paper 2","account_name":"AIV001 Paper 2","csv_file":"alpaca_portfolio_history_Aiv001P2.csv"},
    {"filename":"aiv1P3","display_name":"AIV001 Paper 3","account_name":"AIV001 Paper 3","csv_file":"alpaca_portfolio_history_Aiv001P3.csv"},
    {"filename":"aiv2P1","display_name":"AIV002 Paper 1","account_name":"AIV002 Paper 1","csv_file":"alpaca_portfolio_history_Aiv002P1.csv"},
    {"filename":"aiv2P2","display_name":"AIV002 Paper 2","account_name":"AIV002 Paper 2","csv_file":"alpaca_portfolio_history_Aiv002P2.csv"},
    {"filename":"aiv2P3","display_name":"AIV002 Paper 3","account_name":"AIV002 Paper 3","csv_file":"alpaca_portfolio_history_Aiv002P3.csv"},
    {"filename":"aiv3P1","display_name":"AIV003 Paper 1","account_name":"AIV003 Paper 1","csv_file":"alpaca_portfolio_history_Aiv003P1.csv"},
    {"filename":"aiv3P2","display_name":"AIV003 Paper 2","account_name":"AIV003 Paper 2","csv_file":"alpaca_portfolio_history_Aiv003P2.csv"},
    {"filename":"aiv4P1","display_name":"AIV004 Paper 1","account_name":"AIV004 Paper 1","csv_file":"alpaca_portfolio_history_Aiv004P1.csv"},
    {"filename":"aiv4P2","display_name":"AIV004 Paper 2","account_name":"AIV004 Paper 2","csv_file":"alpaca_portfolio_history_Aiv004P2.csv"},
    {"filename":"aiv5P1","display_name":"AIV005 Paper 1","account_name":"AIV005 Paper 1","csv_file":"alpaca_portfolio_history_Aiv005P1.csv"},
    {"filename":"aiv5P2","display_name":"AIV005 Paper 2","account_name":"AIV005 Paper 2","csv_file":"alpaca_portfolio_history_Aiv005P2.csv"},
]

NAV_HTML = """  <nav class="navbar" role="navigation" aria-label="Main navigation">
    <div class="navbar-signal-line" aria-hidden="true"></div>
    <div class="nav-container">
      <a href="/" class="nav-brand-lockup">
        <span class="nav-brand-name">AI VELOCITY</span>
        <span class="nav-brand-fund">FUND</span>
      </a>
      <button class="nav-toggle" aria-label="Toggle navigation" aria-expanded="false">
        <span class="nav-toggle-line"></span>
        <span class="nav-toggle-line"></span>
        <span class="nav-toggle-line"></span>
      </button>
      <div class="nav-menu">
        <div class="nav-dropdown">
          <button class="nav-dropdown-toggle" aria-expanded="false">
            <span>Charts</span>
            <svg class="nav-dropdown-icon" width="10" height="10" viewBox="0 0 12 12" fill="currentColor"><path d="M6 9L1 4h10z"/></svg>
          </button>
          <div class="nav-dropdown-menu">
            <a href="/charts/d1l1s1" class="nav-dropdown-link">Delta Momentum</a>
            <a href="/charts/d2l1s1" class="nav-dropdown-link">Delta Reversal</a>
            <a href="/charts/n1l1s1" class="nav-dropdown-link">Neutral Alpha</a>
          </div>
        </div>
        <div class="nav-dropdown">
          <button class="nav-dropdown-toggle" aria-expanded="false">
            <span>Strategies</span>
            <svg class="nav-dropdown-icon" width="10" height="10" viewBox="0 0 12 12" fill="currentColor"><path d="M6 9L1 4h10z"/></svg>
          </button>
          <div class="nav-dropdown-menu">
            <a href="/reports/d1l1" class="nav-dropdown-link">Delta Momentum</a>
            <a href="/reports/d2l1" class="nav-dropdown-link">Delta Reversal</a>
            <a href="/reports/n1l1" class="nav-dropdown-link">Neutral Alpha</a>
          </div>
        </div>
        <div class="nav-dropdown">
          <button class="nav-dropdown-toggle" aria-expanded="false">
            <span>Backtests</span>
            <svg class="nav-dropdown-icon" width="10" height="10" viewBox="0 0 12 12" fill="currentColor"><path d="M6 9L1 4h10z"/></svg>
          </button>
          <div class="nav-dropdown-menu">
            <a href="/backtests/iron-butterfly-backtest" class="nav-dropdown-link">Iron Butterfly</a>
            <a href="/backtests/mean-reversion-strategy" class="nav-dropdown-link">Mean Reversion</a>
            <a href="/backtests/trade-on-daily-earnings-calls---short-only" class="nav-dropdown-link">Earnings Short</a>
            <a href="/backtests/trade-on-earnings-calls---long-only" class="nav-dropdown-link">Earnings Long</a>
          </div>
        </div>
        <a href="/about-us" class="nav-link">About</a>
        <a href="mailto:info@aivelocityfund.com" class="nav-link">Contact</a>
      </div>
    </div>
  </nav>"""

FOOTER_HTML = """  <footer class="footer">
    <div class="footer-container">
      <div class="footer-content">
        <div class="footer-brand">
          <a href="/"><img src="/images/Untitled-318-x-50-px.png" loading="lazy" alt="AI Velocity Fund" class="footer-logo"></a>
          <p class="footer-tagline">Systematic alpha generation through algorithmic execution.</p>
        </div>
        <div class="footer-links">
          <div class="footer-column">
            <h4 class="footer-heading">Company</h4>
            <a href="/about-us" class="footer-link">About</a>
            <a href="mailto:info@aivelocityfund.com" class="footer-link">Contact</a>
          </div>
          <div class="footer-column">
            <h4 class="footer-heading">Resources</h4>
            <a href="/reports/d1l1" class="footer-link">Strategy</a>
            <a href="/charts/d1l1s1" class="footer-link">Charts</a>
          </div>
        </div>
      </div>
      <div class="footer-bottom">
        <p class="footer-copyright">&copy; 2025&ndash;2026 AI Velocity Fund, LLC. All Rights Reserved.</p>
      </div>
    </div>
  </footer>"""

def build_report_html(display_name, account_name, csv_file):
    csv_url = "https://www.machinetrader.io/csvfiles/" + csv_file
    return """<!DOCTYPE html>
<html lang="en">
<head>
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-WCG69XDQ');</script>
  <meta charset="utf-8">
  <title>""" + display_name + """ - Portfolio Report | AI Velocity Fund</title>
  <meta name="description" content="Portfolio history report for """ + account_name + """.">
  <meta property="og:title" content=\"""" + display_name + """ - Portfolio Report | AI Velocity Fund\">
  <meta property="og:description" content="Portfolio history report for """ + account_name + """.\">
  <meta property="og:type" content="website">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@300;400;500;600;700&family=IBM+Plex+Sans:wght@300;400;500;600;700&family=IBM+Plex+Serif:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link href="/css/normalize.css" rel="stylesheet" type="text/css">
  <link href="/css/design-system.css" rel="stylesheet" type="text/css">
  <link href="/css/components.css" rel="stylesheet" type="text/css">
  <link href="/css/layout.css" rel="stylesheet" type="text/css">
  <link href="/css/ai-velocity.css" rel="stylesheet" type="text/css">
  <link href="/images/favicon.jpeg" rel="shortcut icon" type="image/x-icon">
  <link href="/images/webclip.jpeg" rel="apple-touch-icon">
  
  <script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag('js',new Date());gtag('config','G-QZQM3NQ9WY');</script>
  <style>
    .report-hero{background:linear-gradient(135deg,#1b4d3e 0%,#0b1d3a 100%);padding:3rem 2rem;text-align:center;margin-bottom:2rem;border-radius:12px;box-shadow:0 10px 40px rgba(27,77,62,0.3);}
    .report-hero h1{color:#fff;font-family:var(--font-serif);font-size:2.5rem;font-weight:700;margin-bottom:0.5rem;letter-spacing:-0.025em;}
    .report-hero p{color:rgba(255,255,255,0.8);font-family:var(--font-sans);font-size:1.125rem;}
    .report-stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:1rem;margin-bottom:2rem;}
    .stat-card{background:#fff;border-radius:12px;padding:1.5rem;text-align:center;border:2px solid #e5e7eb;box-shadow:0 2px 8px rgba(0,0,0,0.06);transition:transform 0.2s,box-shadow 0.2s;}
    .stat-card:hover{transform:translateY(-3px);box-shadow:0 8px 24px rgba(0,0,0,0.12);}
    .stat-card h3{font-family:var(--font-sans);font-size:0.8125rem;color:#6B7280;font-weight:600;text-transform:uppercase;letter-spacing:0.5px;margin-bottom:0.5rem;}
    .stat-card p{font-family:var(--font-mono);font-size:1.625rem;font-weight:700;color:#111827;}
    .stat-card.positive p{color:#1b4d3e;}
    .stat-card.negative p{color:#ef4444;}
    .report-table-card{background:#fff;border-radius:12px;overflow:hidden;border:2px solid #e5e7eb;box-shadow:0 2px 8px rgba(0,0,0,0.06);margin-bottom:2rem;}
    .report-table-header{padding:1.5rem 2rem;border-bottom:2px solid #e5e7eb;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:1rem;}
    .report-table-header h2{font-family:var(--font-serif);font-size:1.5rem;font-weight:700;color:#111827;}
    .report-table-header p{font-family:var(--font-sans);font-size:0.9375rem;color:#6B7280;margin:0;}
    .table-scroll{overflow-x:auto;}
    table{width:100%;border-collapse:collapse;font-family:var(--font-sans);font-size:0.9rem;}
    thead{background:linear-gradient(135deg,#1b4d3e 0%,#0b1d3a 100%);}
    th{padding:1rem 1.25rem;text-align:right;font-weight:600;white-space:nowrap;color:#fff;font-size:0.8125rem;text-transform:uppercase;letter-spacing:0.5px;}
    th:first-child{text-align:left;}
    td{padding:0.875rem 1.25rem;text-align:right;border-bottom:1px solid #f3f4f6;color:#374151;}
    td:first-child{text-align:left;font-weight:600;color:#111827;font-family:var(--font-mono);}
    tbody tr:hover{background:#f9fafb;}
    tbody tr:nth-child(even){background:#fafbfc;}
    tbody tr:nth-child(even):hover{background:#f3f4f6;}
    .positive{color:#1b4d3e;font-weight:600;}
    .negative{color:#ef4444;font-weight:600;}
    .neutral{color:#6B7280;}
    .highlight-row{background:#fffbeb!important;}
    .report-footer-note{text-align:center;padding:1.5rem;color:#6B7280;font-family:var(--font-sans);font-size:0.875rem;border-top:2px solid #e5e7eb;}
    .loading-state{text-align:center;padding:3rem;color:#6B7280;font-family:var(--font-sans);}
    @media(max-width:768px){
      .report-hero{padding:2rem 1.5rem;}
      .report-hero h1{font-size:1.875rem;}
      .report-stats{grid-template-columns:1fr 1fr;}
      table{font-size:0.75rem;min-width:700px;}
      th,td{padding:0.625rem 0.75rem;}
    }
  </style>
</head>
<body>
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-WCG69XDQ"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>

""" + NAV_HTML + """

  <div style="max-width:1400px;margin:0 auto;padding:2rem 1.5rem;">

    <div class="report-hero">
      <h1>""" + display_name + """</h1>
      <p>Portfolio History Report</p>
    </div>

    <div class="report-stats" id="stats">
      <div class="stat-card" style="grid-column:1/-1;">
        <div class="loading-state">Loading portfolio data...</div>
      </div>
    </div>

    <div class="report-table-card">
      <div class="report-table-header">
        <div>
          <h2>Portfolio History</h2>
          <p>Daily performance data for """ + account_name + """</p>
        </div>
      </div>
      <div class="table-scroll">
        <table>
          <thead>
            <tr>
              <th>Date</th>
              <th>Equity</th>
              <th>Cash Flow</th>
              <th>Daily P/L</th>
              <th>Daily %</th>
              <th>Cumulative Profit</th>
              <th>Cumulative %</th>
              <th>Annualized %</th>
              <th>Sharpe Ratio</th>
            </tr>
          </thead>
          <tbody id="tableBody">
            <tr><td colspan="9" class="loading-state">Loading...</td></tr>
          </tbody>
        </table>
      </div>
      <div class="report-footer-note">Last updated: <span id="lastUpdate">—</span></div>
    </div>

  </div>

""" + FOOTER_HTML + """

  <script src="/js/site.js"></script>
  <script>
(function(){
  var endpoint='""" + csv_url + """';

  function fmtCurrency(v){
    if(!v||v==='')return '-';
    var n=parseFloat(v);
    return '$'+n.toLocaleString('en-US',{minimumFractionDigits:2,maximumFractionDigits:2});
  }
  function fmtPct(v){
    if(!v||v==='')return '-';
    return parseFloat(v).toFixed(2)+'%';
  }
  function cls(v){
    if(!v||v==='')return 'neutral';
    var n=parseFloat(v);
    return n>0?'positive':n<0?'negative':'neutral';
  }
  function fmtVal(v,isPct,isCur){
    if(!v||v==='')return '<span class="neutral">-</span>';
    var c=cls(v),f=isCur?fmtCurrency(v):isPct?fmtPct(v):parseFloat(v).toFixed(2);
    return '<span class="'+c+'">'+f+'</span>';
  }

  async function load(){
    try{
      var r=await fetch(endpoint);
      if(!r.ok)throw new Error('HTTP '+r.status);
      var text=await r.text();
      var lines=text.trim().replace(/\\r\\n/g,'\\n').replace(/\\r/g,'\\n').split('\\n');
      var headers=lines[0].split(',').map(function(h){return h.trim();});
      var data=[];
      for(var i=1;i<lines.length;i++){
        var vals=lines[i].split(',').map(function(v){return v.trim();});
        var row={};
        headers.forEach(function(h,idx){row[h]=vals[idx]||'';});
        data.push(row);
      }
      renderTable(data);
      renderStats(data);
    }catch(e){
      document.getElementById('stats').innerHTML='<div class="stat-card" style="grid-column:1/-1;"><h3>Error</h3><p style="font-size:1rem;color:#ef4444;">Unable to load data</p></div>';
      document.getElementById('tableBody').innerHTML='<tr><td colspan="9" style="text-align:center;padding:2rem;color:#ef4444;">Failed to load portfolio data.</td></tr>';
    }
  }

  function renderTable(data){
    var tbody=document.getElementById('tableBody');
    tbody.innerHTML='';
    data.forEach(function(row){
      var tr=document.createElement('tr');
      if(row['Cash Flow']&&row['Cash Flow']!=='')tr.classList.add('highlight-row');
      tr.innerHTML='<td>'+row['Date']+'</td>'+
        '<td>'+fmtCurrency(row['Equity'])+'</td>'+
        '<td>'+(row['Cash Flow']?fmtCurrency(row['Cash Flow']):'-')+'</td>'+
        '<td>'+fmtVal(row['Daily P/L'],false,true)+'</td>'+
        '<td>'+fmtVal(row['Daily %'],true,false)+'</td>'+
        '<td>'+fmtVal(row['Cumulative Profit'],false,true)+'</td>'+
        '<td>'+fmtVal(row['Cumulative %'],true,false)+'</td>'+
        '<td>'+fmtVal(row['Annualized %'],true,false)+'</td>'+
        '<td>'+fmtVal(row['Sharpe Ratio'],false,false)+'</td>';
      tbody.appendChild(tr);
    });
    var last=data[data.length-1];
    if(last)document.getElementById('lastUpdate').textContent=last['Date']||'—';
  }

  function renderStats(data){
    var last=data[data.length-1];
    var eq=parseFloat(last['Equity']);
    var cp=parseFloat(last['Cumulative Profit']);
    var cpct=parseFloat(last['Cumulative %']);
    var ann=parseFloat(last['Annualized %']);
    var sr=parseFloat(last['Sharpe Ratio']);
    document.getElementById('stats').innerHTML=
      '<div class="stat-card"><h3>Current Equity</h3><p>'+fmtCurrency(eq)+'</p></div>'+
      '<div class="stat-card '+(cp>=0?'positive':'negative')+'"><h3>Total Profit</h3><p>'+fmtCurrency(cp)+'</p></div>'+
      '<div class="stat-card '+(cpct>=0?'positive':'negative')+'"><h3>Total Return</h3><p>'+fmtPct(cpct)+'</p></div>'+
      '<div class="stat-card '+(ann>=0?'positive':'negative')+'"><h3>Annualized Return</h3><p>'+fmtPct(ann)+'</p></div>'+
      '<div class="stat-card '+(sr>=0?'positive':'negative')+'"><h3>Sharpe Ratio</h3><p>'+sr.toFixed(2)+'</p></div>';
  }

  if(document.readyState==='loading'){document.addEventListener('DOMContentLoaded',load);}
  else{load();}
})();
  </script>

</body>
</html>"""


def generate_all():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    reports_dir = os.path.join(script_dir, "reports")
    os.makedirs(reports_dir, exist_ok=True)
    for r in REPORTS:
        html = build_report_html(r["display_name"], r["account_name"], r["csv_file"])
        out_path = os.path.join(reports_dir, r["filename"] + ".html")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(html)
        print("  Written: reports/" + r["filename"] + ".html")
    print("\nDone! " + str(len(REPORTS)) + " report pages generated.")


if __name__ == "__main__":
    print("AI Velocity Fund - Strategy Report Page Generator")
    print("Generating " + str(len(REPORTS)) + " report pages...\n")
    generate_all()
