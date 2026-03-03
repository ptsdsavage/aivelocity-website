#!/usr/bin/env python3
"""
AI Velocity Fund - Chart Page Generator
Run: python3 update_charts.py
"""
import os

CHARTS = [
    {"filename":"d1l1s1","display_name":"Delta Momentum Live","csv_file":"alpaca_portfolio_history_DanSavage1Live.csv","start_date":"2025-11-15"},
    {"filename":"d1p1s1","display_name":"Delta Momentum Paper 1","csv_file":"alpaca_portfolio_history_DanSavage1P1.csv","start_date":"2026-01-01"},
    {"filename":"d1p2s1","display_name":"Delta Momentum Paper 2","csv_file":"alpaca_portfolio_history_DanSavage1P2.csv","start_date":"2026-01-01"},
    {"filename":"d1p3s1","display_name":"Delta Momentum Paper 3","csv_file":"alpaca_portfolio_history_DanSavage1P3.csv","start_date":"2026-01-01"},
    {"filename":"d2l1s1","display_name":"Delta Reversal Live","csv_file":"alpaca_portfolio_history_DanSavage2Live.csv","start_date":"2025-11-19"},
    {"filename":"d2p1s1","display_name":"Delta Reversal Paper 1","csv_file":"alpaca_portfolio_history_DanSavage2P1.csv","start_date":"2026-01-01"},
    {"filename":"n1l1s1","display_name":"Neutral Alpha Live","csv_file":"alpaca_portfolio_history_NikkiLive.csv","start_date":"2025-11-15"},
    {"filename":"n1p1s1","display_name":"Neutral Alpha Paper 1","csv_file":"alpaca_portfolio_history_NikkiP1.csv","start_date":"2026-01-01"},
    {"filename":"n1p2s1","display_name":"Neutral Alpha Paper 2","csv_file":"alpaca_portfolio_history_NikkiP2.csv","start_date":"2026-01-01"},
    {"filename":"n1p3s1","display_name":"Neutral Alpha Paper 3","csv_file":"alpaca_portfolio_history_NikkiP3.csv","start_date":"2026-01-01"},
    {"filename":"aiv001p1","display_name":"AIV001 Paper 1","csv_file":"alpaca_portfolio_history_Aiv001P1.csv","start_date":"2026-01-01"},
    {"filename":"aiv001p2","display_name":"AIV001 Paper 2","csv_file":"alpaca_portfolio_history_Aiv001P2.csv","start_date":"2026-01-01"},
    {"filename":"aiv001p3","display_name":"AIV001 Paper 3","csv_file":"alpaca_portfolio_history_Aiv001P3.csv","start_date":"2026-01-01"},
    {"filename":"aiv002p1","display_name":"AIV002 Paper 1","csv_file":"alpaca_portfolio_history_Aiv002P1.csv","start_date":"2026-01-01"},
    {"filename":"aiv002p2","display_name":"AIV002 Paper 2","csv_file":"alpaca_portfolio_history_Aiv002P2.csv","start_date":"2026-01-01"},
    {"filename":"aiv002p3","display_name":"AIV002 Paper 3","csv_file":"alpaca_portfolio_history_Aiv002P3.csv","start_date":"2026-01-01"},
    {"filename":"aiv003p1","display_name":"AIV003 Paper 1","csv_file":"alpaca_portfolio_history_Aiv003P1.csv","start_date":"2026-01-01"},
    {"filename":"aiv003p2","display_name":"AIV003 Paper 2","csv_file":"alpaca_portfolio_history_Aiv003P2.csv","start_date":"2026-01-01"},
    {"filename":"aiv004p1","display_name":"AIV004 Paper 1","csv_file":"alpaca_portfolio_history_Aiv004P1.csv","start_date":"2026-01-01"},
    {"filename":"aiv004p2","display_name":"AIV004 Paper 2","csv_file":"alpaca_portfolio_history_Aiv004P2.csv","start_date":"2026-01-01"},
    {"filename":"aiv005p1","display_name":"AIV005 Paper 1","csv_file":"alpaca_portfolio_history_Aiv005P1.csv","start_date":"2026-01-01"},
    {"filename":"aiv005p2","display_name":"AIV005 Paper 2","csv_file":"alpaca_portfolio_history_Aiv005P2.csv","start_date":"2026-01-01"},
]

def build_html(display_name, csv_file, start_date):
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
  <title>""" + display_name + """ - Portfolio Performance | AI Velocity Fund</title>
  <meta name="description" content=\"""" + display_name + """ portfolio performance vs SPY benchmark.\">
  <meta property="og:title" content=\"""" + display_name + """ - Portfolio Performance | AI Velocity Fund\">
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
  <script src="https://cdn.jsdelivr.net/npm/lightweight-charts@4.1.0/dist/lightweight-charts.standalone.production.js"></script>
  <style>
    .chart-hero{background:linear-gradient(135deg,#1b4d3e 0%,#0b1d3a 100%);padding:3rem 2rem;text-align:center;margin-bottom:2rem;border-radius:12px;box-shadow:0 10px 40px rgba(27,77,62,0.3);}
    .chart-hero-title{color:#fff;font-family:var(--font-serif);font-size:2.5rem;font-weight:700;margin-bottom:0.75rem;letter-spacing:-0.025em;}
    .chart-hero-subtitle{color:rgba(255,255,255,0.8);font-family:var(--font-sans);font-size:1.125rem;font-weight:500;}
    .chart-card{background:#fff;border-radius:12px;padding:2.5rem;max-width:1400px;margin:0 auto;box-shadow:0 4px 6px -1px rgba(0,0,0,0.1),0 2px 4px -1px rgba(0,0,0,0.06);}
    .chart-card-header{display:flex;justify-content:space-between;align-items:center;margin-bottom:2rem;flex-wrap:wrap;gap:1.5rem;}
    .chart-card-title-block{flex:1;min-width:250px;}
    .chart-card-title-block h2{color:#111827;font-family:var(--font-serif);font-size:1.875rem;font-weight:700;margin-bottom:0.5rem;letter-spacing:-0.025em;}
    .chart-card-title-block p{color:#6B7280;font-family:var(--font-sans);font-size:1rem;margin:0;}
    .time-selector{display:flex;gap:0.5rem;align-items:center;background:#f9fafb;padding:0.5rem;border-radius:10px;}
    .time-selector-label{color:#6B7280;font-family:var(--font-sans);font-size:0.875rem;font-weight:600;margin-right:0.5rem;}
    .time-btn{padding:0.625rem 1.25rem;border:2px solid transparent;background:white;color:#111827;border-radius:8px;cursor:pointer;font-family:var(--font-sans);font-size:0.875rem;font-weight:600;transition:all 0.2s ease;box-shadow:0 1px 2px rgba(0,0,0,0.05);}
    .time-btn:hover{background:#f3f4f6;transform:translateY(-1px);box-shadow:0 2px 4px rgba(0,0,0,0.1);}
    .time-btn.active{background:#1b4d3e;color:white;border-color:#1b4d3e;box-shadow:0 4px 6px rgba(27,77,62,0.3);}
    .chart-wrapper{position:relative;height:550px;margin-bottom:2rem;border:2px solid #e5e7eb;border-radius:12px;overflow:hidden;background:#fafafa;}
    #tradingViewChart{width:100%;height:100%;}
    .chart-legend{display:flex;justify-content:center;gap:4rem;padding:2rem 0;border-top:2px solid #e5e7eb;}
    .chart-legend-item{display:flex;flex-direction:column;align-items:center;gap:0.75rem;padding:1rem 2rem;background:#f9fafb;border-radius:12px;transition:all 0.2s ease;}
    .chart-legend-item:hover{background:#f3f4f6;transform:translateY(-2px);}
    .chart-legend-label{display:flex;align-items:center;gap:0.625rem;color:#6B7280;font-family:var(--font-sans);font-size:0.9375rem;font-weight:600;}
    .chart-legend-dot{width:14px;height:14px;border-radius:50%;box-shadow:0 2px 4px rgba(0,0,0,0.15);}
    .chart-legend-dot.strategy{background:#1b4d3e;}
    .chart-legend-dot.benchmark{background:#3b82f6;}
    .chart-legend-value{color:#111827;font-family:var(--font-mono);font-size:1.5rem;font-weight:700;letter-spacing:-0.025em;}
    .chart-legend-value.positive{color:#1b4d3e;}
    .chart-legend-value.negative{color:#ef4444;}
    .chart-hint{text-align:center;color:#6B7280;font-family:var(--font-sans);font-size:0.8125rem;margin-top:1rem;padding:0.75rem;background:#f9fafb;border-radius:8px;font-weight:500;}
    @media(max-width:768px){
      .chart-hero{padding:2rem 1.5rem;}
      .chart-hero-title{font-size:1.875rem;}
      .chart-card{padding:1.5rem;}
      .chart-card-header{flex-direction:column;align-items:flex-start;}
      .chart-card-title-block h2{font-size:1.5rem;}
      .time-selector{width:100%;flex-wrap:wrap;}
      .time-btn{flex:1;min-width:calc(50% - 0.25rem);}
      .chart-wrapper{height:400px;}
      .chart-legend{flex-direction:column;gap:1rem;}
      .chart-legend-item{width:100%;}
      .chart-legend-value{font-size:1.75rem;}
    }
  </style>
</head>
<body>
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-WCG69XDQ"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>

  <nav class="navbar" role="navigation" aria-label="Main navigation">
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
  </nav>

  <div style="max-width:1400px;margin:0 auto;padding:2rem 1.5rem;">

    <script>
      var strategyDisplayName = '""" + display_name + """';
      var csvFilePath = '""" + csv_url + """';
      var spyFilePath = 'https://www.machinetrader.io/csvfiles/spydata.csv';
      var accountStartDate = '""" + start_date + """';
    </script>

    <div class="chart-hero">
      <h1 class="chart-hero-title">""" + display_name + """ Portfolio Performance</h1>
      <p class="chart-hero-subtitle">Portfolio History and Performance Metrics</p>
    </div>

    <div class="chart-card">
      <div class="chart-card-header">
        <div class="chart-card-title-block">
          <h2>Portfolio vs SPY Benchmark</h2>
          <p>Cumulative returns compared to S&amp;P 500 ETF</p>
        </div>
        <div class="time-selector">
          <span class="time-selector-label">Time Period:</span>
          <button class="time-btn" onclick="setComparisonPeriod('1D',this)">1 Day</button>
          <button class="time-btn" onclick="setComparisonPeriod('1W',this)">1 Week</button>
          <button class="time-btn" onclick="setComparisonPeriod('1M',this)">1 Month</button>
          <button class="time-btn active" onclick="setComparisonPeriod('ALL',this)">All</button>
        </div>
      </div>
      <div class="chart-wrapper">
        <div id="tradingViewChart"></div>
      </div>
      <div class="chart-legend">
        <div class="chart-legend-item">
          <div class="chart-legend-label">
            <span class="chart-legend-dot strategy"></span>
            Portfolio Return
          </div>
          <div class="chart-legend-value" id="strategyValue">--</div>
        </div>
        <div class="chart-legend-item">
          <div class="chart-legend-label">
            <span class="chart-legend-dot benchmark"></span>
            SPY (Benchmark)
          </div>
          <div class="chart-legend-value" id="benchmarkValue">--</div>
        </div>
      </div>
      <div class="chart-hint">Scroll to zoom &middot; Drag to pan &middot; Double-click to reset</div>
    </div>

  </div>

  <footer class="footer">
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
  </footer>

  <script src="/js/site.js"></script>
  <script>
(function(){
  var COLORS={benchmark:'#3b82f6',strategy:'#1b4d3e'};
  var comparisonData=null,currentPeriod='ALL',chart=null,strategySeries=null,benchmarkSeries=null;

  async function loadData(){
    try{
      if(typeof LightweightCharts==='undefined'){
        await new Promise(function(res){
          var t=setInterval(function(){if(typeof LightweightCharts!=='undefined'){clearInterval(t);res();}},100);
        });
      }
      var r=await Promise.all([fetch(csvFilePath),fetch(spyFilePath)]);
      if(!r[0].ok)throw new Error('Portfolio CSV: '+r[0].status);
      if(!r[1].ok)throw new Error('SPY CSV: '+r[1].status);
      var texts=await Promise.all([r[0].text(),r[1].text()]);
      var spyMap=parseSpyCSV(texts[1],accountStartDate);
      var raw=parsePortfolioCSV(texts[0],spyMap);
      raw.sort(function(a,b){return a.time-b.time;});
      var seen=new Set(),unique=[];
      for(var i=raw.length-1;i>=0;i--){if(!seen.has(raw[i].time)){seen.add(raw[i].time);unique.unshift(raw[i]);}}
      comparisonData=unique;
      if(unique.length>0)initChart();
      else throw new Error('No data points found');
    }catch(e){
      var el=document.getElementById('tradingViewChart');
      if(el)el.innerHTML='<div style="display:flex;align-items:center;justify-content:center;height:100%;color:#ef4444;font-family:sans-serif;padding:2rem;">Error loading data: '+e.message+'</div>';
    }
  }

  function parseSpyCSV(text,startDate){
    var lines=text.trim().replace(/\\r\\n/g,'\\n').replace(/\\r/g,'\\n').split('\\n');
    var h=lines[0].split(',').map(function(x){return x.trim();});
    var di=h.indexOf('Date'),oi=h.indexOf('Open');
    if(di<0||oi<0)return {};
    var prices={},startPrice=null;
    for(var i=1;i<lines.length;i++){
      var v=lines[i].trim().split(',').map(function(x){return x.trim();});
      var d=v[di],p=parseFloat(v[oi]);
      if(!isNaN(p)&&d){prices[d]=p;if(d>=startDate&&startPrice===null)startPrice=p;}
    }
    if(startPrice===null)return {};
    var out={};
    for(var k in prices){if(k>=startDate)out[k]=(prices[k]-startPrice)/startPrice;}
    return out;
  }

  function parsePortfolioCSV(text,spyMap){
    var lines=text.trim().replace(/\\r\\n/g,'\\n').replace(/\\r/g,'\\n').split('\\n');
    var h=lines[0].split(',').map(function(x){return x.trim().replace(/"/g,'');});
    var di=h.indexOf('Date'),ci=h.indexOf('Cumulative %');
    if(di<0||ci<0)throw new Error('Missing columns in portfolio CSV');
    var out=[];
    for(var i=1;i<lines.length;i++){
      var v=lines[i].trim().split(',').map(function(x){return x.trim();});
      if(v.length<=ci)continue;
      var d=v[di],pct=parseFloat(v[ci]);
      if(isNaN(pct)||!d)continue;
      var ts;
      if(d.indexOf('-')>0&&d.split('-')[0].length===4){ts=Math.floor(new Date(d+'T00:00:00').getTime()/1000);}
      else if(d.indexOf('/')>0){var p=d.split('/');var yr=parseInt(p[2]);if(yr<100)yr+=2000;ts=Math.floor(new Date(yr,parseInt(p[0])-1,parseInt(p[1])).getTime()/1000);}
      else{ts=Math.floor(new Date(d).getTime()/1000);}
      if(!isNaN(ts))out.push({time:ts,strategy:pct/100,spy:spyMap[d]||0});
    }
    return out;
  }

  function getWeek(d){
    var u=new Date(Date.UTC(d.getFullYear(),d.getMonth(),d.getDate()));
    var day=u.getUTCDay()||7;u.setUTCDate(u.getUTCDate()+4-day);
    var y=new Date(Date.UTC(u.getUTCFullYear(),0,1));
    return Math.ceil((((u-y)/86400000)+1)/7);
  }

  function filterData(data,period){
    if(!data||!data.length)return data;
    if(period==='ALL'||period==='1D')return data;
    var out=[],curKey=null,last=null;
    data.forEach(function(pt){
      var dt=new Date(pt.time*1000);
      var key=period==='1W'?(dt.getFullYear()+'W'+getWeek(dt)):(dt.getFullYear()+'-'+dt.getMonth());
      if(key!==curKey){if(last)out.push(last);curKey=key;last=pt;}else{last=pt;}
    });
    if(last)out.push(last);
    return out;
  }

  function setLegendValue(id,val){
    var el=document.getElementById(id);
    if(!el)return;
    el.textContent=val.toFixed(2)+'%';
    el.className='chart-legend-value'+(val>0?' positive':val<0?' negative':'');
  }

  function updateLegend(data){
    if(!data||!data.length)return;
    var last=data[data.length-1];
    setLegendValue('strategyValue',last.strategy*100);
    setLegendValue('benchmarkValue',last.spy*100);
  }

  function updateChart(){
    if(!comparisonData||!strategySeries||!benchmarkSeries)return;
    var filtered=filterData(comparisonData,currentPeriod);
    strategySeries.setData(filtered.map(function(d){return{time:d.time,value:d.strategy*100};}));
    benchmarkSeries.setData(filtered.map(function(d){return{time:d.time,value:d.spy*100};}));
    chart.timeScale().fitContent();
    updateLegend(filtered);
  }

  function initChart(){
    var container=document.getElementById('tradingViewChart');
    if(!container)return;
    if(chart)chart.remove();
    chart=LightweightCharts.createChart(container,{
      width:container.clientWidth,height:container.clientHeight,
      layout:{background:{color:'#ffffff'},textColor:'#6B7280',fontSize:12,fontFamily:'IBM Plex Sans, sans-serif'},
      grid:{vertLines:{color:'rgba(0,0,0,0.05)'},horzLines:{color:'rgba(0,0,0,0.05)'}},
      crosshair:{mode:LightweightCharts.CrosshairMode.Normal},
      rightPriceScale:{borderColor:'rgba(0,0,0,0.1)',scaleMargins:{top:0.1,bottom:0.1}},
      timeScale:{borderColor:'rgba(0,0,0,0.1)',timeVisible:true,secondsVisible:false},
      handleScroll:{mouseWheel:true,pressedMouseMove:true,horzTouchDrag:true,vertTouchDrag:true},
      handleScale:{mouseWheel:true,pinch:true,axisPressedMouseMove:true}
    });
    strategySeries=chart.addLineSeries({color:COLORS.strategy,lineWidth:2,priceFormat:{type:'custom',formatter:function(p){return p.toFixed(2)+'%';}}});
    benchmarkSeries=chart.addLineSeries({color:COLORS.benchmark,lineWidth:2,priceFormat:{type:'custom',formatter:function(p){return p.toFixed(2)+'%';}}});
    chart.subscribeCrosshairMove(function(param){
      if(param.time){
        var sd=param.seriesData.get(strategySeries),bd=param.seriesData.get(benchmarkSeries);
        if(sd&&bd){setLegendValue('strategyValue',sd.value);setLegendValue('benchmarkValue',bd.value);}
      }else{updateLegend(filterData(comparisonData,currentPeriod));}
    });
    window.addEventListener('resize',function(){if(chart&&container)chart.applyOptions({width:container.clientWidth,height:container.clientHeight});});
    updateChart();
  }

  window.setComparisonPeriod=function(period,btn){
    currentPeriod=period;
    document.querySelectorAll('.time-btn').forEach(function(b){b.classList.remove('active');});
    if(btn)btn.classList.add('active');
    updateChart();
  };

  if(document.readyState==='loading'){document.addEventListener('DOMContentLoaded',loadData);}
  else{loadData();}
})();
  </script>

</body>
</html>"""


def generate_all():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    charts_dir = os.path.join(script_dir, "charts")
    os.makedirs(charts_dir, exist_ok=True)
    for chart in CHARTS:
        html = build_html(chart["display_name"], chart["csv_file"], chart["start_date"])
        out_path = os.path.join(charts_dir, chart["filename"] + ".html")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(html)
        print("  Written: charts/" + chart["filename"] + ".html")
    print("\nDone! " + str(len(CHARTS)) + " chart pages generated.")


if __name__ == "__main__":
    print("AI Velocity Fund - Chart Page Generator")
    print("Generating " + str(len(CHARTS)) + " chart pages...\n")
    generate_all()
