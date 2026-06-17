#!/usr/bin/env python3
import json, os

D = '/Users/steven/Documents/Claude/Chinese_Overseas_Push/overseas_pool'
pool = json.load(open(os.path.join(D,'pool.json')))
uk = [c for c in pool['creators'] if c['country']=='United Kingdom']

# Shortlist = WorldFirst-relevant lean (money/business/career/cross-border) OR standout engagement.
# uid -> one-line why it's on the shortlist
SHORT = {
 '609bc907000000000101f2c0':"Most on-brief: UK cross-border ecommerce operator, already a WF scout Tier-1. The overseas-seller story writes itself.",
 '5f9802e8000000000101f7e8':"UK job/money audience at scale (45k fans, 154k lifetime saves). Overseas-Chinese-making-money-abroad is exactly WF's customer mindset.",
 '566533c1e00dd8764d6e8e50':"Business/strategy audience: Cambridge MBA, ex-Big-4 ESG, new-energy 出海 strategy. Content on global-work and going-overseas. 356-save top note.",
 '5a47ca404eacab642526922d':"Career-in-finance content in the UK (512-save top note). Audience is ambitious overseas Chinese professionals.",
 '5b783472c0abeb0001990bc0':"Finance/money lane: UK 理财 recommendations, cross-China-UK career. Direct topical overlap with WF's money message.",
 '64b88de600000000140370f9':"Finance/money lane: economics PhD, UK investing diary (十万到百万£). Money-minded overseas audience.",
 '58c35ff17fc5b850a6c59fcc':"Highest engagement in the UK set (1,261-save top note, 38k fans). Art/expat-life reach play for top-of-funnel awareness.",
 '60f8bf0f000000000100b083':"Business/creator: UK 11 years, investing + 裸辞创业 content. Entrepreneur audience.",
 '567bba2e4476087e37a2ca3a':"Business/founder: London-fashion-school designer running her own label. Small-brand-owner persona.",
}
for c in uk:
    c['shortlist'] = c['uid'] in SHORT
    c['why'] = SHORT.get(c['uid'],'')

uk.sort(key=lambda c:(not c['shortlist'], -c['fans']))
DATA = json.dumps(uk, ensure_ascii=False)
nshort = sum(1 for c in uk if c['shortlist'])

html = '''<!DOCTYPE html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex">
<title>UK Chinese KOL shortlist</title>
<style>
:root{--ink:#16181d;--muted:#6b7280;--faint:#9aa0a8;--line:#e7e8ec;--line2:#d8dade;--bg:#fff;--panel:#fafafb;--blue:#2f6df6;--gold:#b8860b;--green:#11a36b}
*{box-sizing:border-box}html{-webkit-font-smoothing:antialiased}
body{margin:0;background:var(--bg);color:var(--ink);font-family:-apple-system,BlinkMacSystemFont,"SF Pro Text",Inter,Segoe UI,Roboto,Helvetica,Arial,sans-serif;font-size:15px;line-height:1.5}
.wrap{max-width:1100px;margin:0 auto;padding:54px 30px 130px}
.eyebrow{font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:var(--faint);font-weight:600;margin:0 0 13px}
.eyebrow a{color:var(--blue);text-decoration:none}.eyebrow a:hover{text-decoration:underline}
h1{font-size:30px;letter-spacing:-.02em;margin:0 0 11px;font-weight:680;line-height:1.16}
.sub{font-size:16px;color:var(--muted);max-width:88ch;margin:0 0 8px}.sub b{font-weight:640;color:var(--ink)}
.stamp{font-size:12.5px;color:var(--faint);margin-top:12px}
hr.rule{height:1px;background:var(--line);border:0;margin:30px 0 22px}
h2{font-size:13px;letter-spacing:.12em;text-transform:uppercase;color:var(--faint);font-weight:650;margin:34px 0 14px}
.srow{display:flex;align-items:center;gap:14px;flex-wrap:wrap;margin-bottom:14px}
.chip{font:inherit;font-size:12.5px;padding:5px 13px;border:1px solid var(--line2);border-radius:20px;background:#fff;color:var(--muted);cursor:pointer;user-select:none}
.chip:hover{border-color:var(--ink);color:var(--ink)}.chip.on{background:var(--ink);color:#fff;border-color:var(--ink)}
#search{font:inherit;font-size:13.5px;padding:8px 13px;border:1px solid var(--line2);border-radius:9px;outline:none;width:220px}
#search:focus{border-color:var(--ink)}
.count{font-size:12.5px;color:var(--faint);font-variant-numeric:tabular-nums;margin-left:auto}
.card{border:1px solid var(--line);border-radius:13px;padding:16px 18px;margin:0 0 11px;transition:border-color .15s}
.card.short{border-color:var(--line2)}
.card:hover{border-color:var(--ink)}
.ctop{display:flex;align-items:baseline;gap:9px;flex-wrap:wrap}
.pk{width:15px;height:15px;cursor:pointer;accent-color:var(--ink);position:relative;top:2px}
.nm{font-weight:660;font-size:16px}
.tag{display:inline-block;font-size:9.5px;letter-spacing:.04em;font-weight:650;padding:1px 6px;border-radius:4px;border:1px solid;text-transform:uppercase}
.t-short{color:var(--gold);border-color:#ecd9b0}
.t-topic{color:var(--muted);border-color:var(--line2);text-transform:none;font-weight:600}
.t-video{color:var(--gold);border-color:#ecd9b0;text-transform:none}
.t-mixed{color:var(--blue);border-color:#c5d8fb;text-transform:none}
.prof{font-size:11px;color:var(--blue);text-decoration:none;margin-left:2px}.prof:hover{text-decoration:underline}
.stats{margin-left:auto;font-size:12px;color:var(--muted);font-variant-numeric:tabular-nums;white-space:nowrap}
.stats b{color:var(--ink);font-weight:650}
.bio{font-size:12.5px;color:var(--faint);margin:7px 0 0}
.why{font-size:13px;color:#2a2d33;margin:9px 0 0;padding-top:9px;border-top:1px solid var(--line)}
.why b{color:var(--gold);font-weight:650}
.card.picked{border-color:var(--green);background:#f6fbf8}
.foot{margin-top:30px;font-size:12.5px;color:var(--faint)}
.pickbar{position:fixed;left:0;right:0;bottom:0;z-index:9000;background:rgba(255,255,255,.94);backdrop-filter:blur(9px);border-top:1px solid var(--line2);padding:12px 30px;display:flex;align-items:center;gap:16px;flex-wrap:wrap}
.pickbar .pc{font-size:13px;font-weight:650;font-variant-numeric:tabular-nums}.pickbar .pc .faint{color:var(--faint);font-weight:500}
.pickbar .clearp{font:inherit;font-size:12px;color:var(--blue);background:none;border:0;cursor:pointer;display:none}.pickbar .clearp:hover{text-decoration:underline}
.pickbar .copyb{font:inherit;font-size:13px;font-weight:600;padding:10px 18px;border:0;border-radius:9px;background:var(--ink);color:#fff;cursor:pointer;margin-left:auto}
.pickbar .copyb:disabled{opacity:.4;cursor:default}
.pickbar .copied{font-size:12px;color:var(--green);opacity:0;transition:opacity .2s}
</style></head>
<body><div class="wrap">

<p class="eyebrow">WorldFirst &middot; discovery &middot; <a href="index.html">&larr; full overseas pool</a></p>
<h1>UK Chinese KOL shortlist</h1>
<p class="sub">The United Kingdom slice of the overseas pool: <b>__TOTAL__ Chinese-language creators based in the UK</b>. The <b style="color:#b8860b">__NSHORT__ shortlisted</b> ones lead, picked for WorldFirst relevance, money, business, career, cross-border, or standout engagement, each with a one-line reason. The rest follow as the wider reach bench.</p>
<div class="stamp">UK subset of the 12 Jun 2026 sweep &middot; one hard gate (UK ip), fans 2k&ndash;500k, posted &ge;10 &middot; shortlist is an editorial call, not a hard cut &middot; discovery only, no one contacted</div>

<hr class="rule">

<div class="srow">
  <button class="chip" id="shortToggle" onclick="toggleShort()">Shortlist only</button>
  <input id="search" type="text" placeholder="Search name or bio..." oninput="render()">
  <span class="count" id="count"></span>
</div>
<div id="list"></div>

<div class="foot">Discovery only. No contacting, booking, or paying anyone. Traction = profile lifetime saves + the one harvested note that surfaced each creator, not a recent-feed median. Re-pull recent feed before any brief. Live TikHub data, 12 Jun 2026.</div>
</div>

<div class="pickbar">
  <span class="pc"><span id="pcount">0</span> <span class="faint">picked</span></span>
  <button class="clearp" id="clearp" onclick="clearPicks()">clear</button>
  <button class="copyb" id="copyb" disabled onclick="copyPicks()">Copy my picks</button>
  <span class="copied" id="copied">Copied</span>
</div>

<script>
const DATA=__DATA__;
const TL={business:'Business',ecomm:'Ecommerce',finance_invest:'Finance/Invest',career_job:'Career/Job',study_abroad:'Study abroad',expat_life:'Expat life',food:'Food',travel:'Travel',beauty_fashion:'Beauty/Fashion',lifestyle:'Lifestyle',parenting:'Parenting'};
const picks=new Set();let shortOnly=false;
function fmtFans(n){return n>=10000?(n/10000).toFixed(1)+'w':n.toLocaleString();}
function render(){
  const q=document.getElementById('search').value.trim().toLowerCase();
  const rows=DATA.filter(c=>{
    if(shortOnly&&!c.shortlist)return false;
    if(q&&!(c.name.toLowerCase().includes(q)||(c.bio||'').toLowerCase().includes(q)))return false;
    return true;});
  const el=document.getElementById('list');el.innerHTML='';
  rows.forEach(c=>{
    const fcls=c.format==='video'?'t-video':c.format==='mixed'?'t-mixed':'';
    const fmtTag=c.format!=='image'?`<span class="tag ${fcls}">${c.format}</span>`:'';
    const d=document.createElement('div');
    d.className='card'+(c.shortlist?' short':'')+(picks.has(c.uid)?' picked':'');
    d.innerHTML=`
      <div class="ctop">
        <input type="checkbox" class="pk" ${picks.has(c.uid)?'checked':''} onclick="togglePick('${c.uid}',this)">
        <span class="nm">${c.name}</span>
        ${c.shortlist?'<span class="tag t-short">shortlist</span>':''}
        <span class="tag t-topic">${TL[c.topic]||c.topic}</span>${fmtTag}
        <a class="prof" href="https://www.xiaohongshu.com/user/profile/${c.uid}" target="_blank" rel="noopener">&#8599; XHS</a>
        <span class="stats"><b>${fmtFans(c.fans)}</b> fans &middot; <b>${c.lifetime_saves.toLocaleString()}</b> saves &middot; top note <b>${c.src_saves}</b></span>
      </div>
      <div class="bio">${c.bio||''}</div>
      ${c.why?`<div class="why"><b>Why shortlisted:</b> ${c.why}</div>`:''}`;
    el.appendChild(d);
  });
  document.getElementById('count').textContent=`showing ${rows.length} of ${DATA.length}`;
}
function toggleShort(){shortOnly=!shortOnly;document.getElementById('shortToggle').classList.toggle('on',shortOnly);render();}
function togglePick(uid,el){if(picks.has(uid))picks.delete(uid);else picks.add(uid);el.closest('.card').classList.toggle('picked',picks.has(uid));upd();}
function clearPicks(){picks.clear();render();upd();}
function upd(){document.getElementById('pcount').textContent=picks.size;document.getElementById('copyb').disabled=!picks.size;document.getElementById('clearp').style.display=picks.size?'inline':'none';}
function copyPicks(){
  const sel=DATA.filter(d=>picks.has(d.uid));
  let t='== uk_kol_shortlist ==\\n\\n'+sel.length+' UK creators picked\\n\\n';
  sel.forEach(c=>{t+=`${c.name} | ${TL[c.topic]||c.topic} | ${c.format} | ${fmtFans(c.fans)} fans | ${c.lifetime_saves.toLocaleString()} lifetime saves | xiaohongshu.com/user/profile/${c.uid}\\n`;});
  t+='\\n> UK-based overseas Chinese creators. Vet fit + re-pull recent feed before any brief. Never contact directly.\\n';
  navigator.clipboard.writeText(t).then(()=>{const e=document.getElementById('copied');e.style.opacity='1';setTimeout(()=>e.style.opacity='0',2200);});
}
render();
</script></body></html>'''

html = html.replace('__DATA__',DATA).replace('__TOTAL__',str(len(uk))).replace('__NSHORT__',str(nshort))
open(os.path.join(D,'uk.html'),'w',encoding='utf-8').write(html)
print(f'built uk.html: {len(uk)} UK creators, {nshort} shortlisted, {len(html)} bytes')
