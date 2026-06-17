#!/usr/bin/env python3
import json, os

D = '/Users/steven/Documents/Claude/Chinese_Overseas_Push/overseas_pool'
pool = json.load(open(os.path.join(D,'pool.json')))
creators = pool['creators']
DATA = json.dumps(creators, ensure_ascii=False)

html = '''<!DOCTYPE html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex">
<title>Overseas Chinese KOL Pool</title>
<style>
:root{--ink:#16181d;--muted:#6b7280;--faint:#9aa0a8;--line:#e7e8ec;--line2:#d8dade;--bg:#fff;--panel:#fafafb;--sel:#16181d;--blue:#2f6df6}
*{box-sizing:border-box}html{-webkit-font-smoothing:antialiased}
body{margin:0;background:var(--bg);color:var(--ink);font-family:-apple-system,BlinkMacSystemFont,"SF Pro Text",Inter,Segoe UI,Roboto,Helvetica,Arial,sans-serif;font-size:15px;line-height:1.5}
.wrap{max-width:1240px;margin:0 auto;padding:54px 30px 130px}
.eyebrow{font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:var(--faint);font-weight:600;margin:0 0 13px}
h1{font-size:30px;letter-spacing:-.02em;margin:0 0 11px;font-weight:680;line-height:1.16}
.sub{font-size:16px;color:var(--muted);max-width:90ch;margin:0 0 8px}
.sub b{font-weight:640;color:var(--ink)}
.stamp{font-size:12.5px;color:var(--faint);margin-top:12px}
hr.rule{height:1px;background:var(--line);border:0;margin:30px 0 22px}
.filters{display:flex;flex-direction:column;gap:13px;margin-bottom:18px}
.frow{display:flex;align-items:flex-start;gap:12px;flex-wrap:wrap}
.flabel{font-size:10.5px;letter-spacing:.07em;text-transform:uppercase;color:var(--faint);font-weight:650;min-width:62px;padding-top:7px}
.chips{display:flex;gap:6px;flex-wrap:wrap;flex:1}
.chip{font:inherit;font-size:12.5px;padding:5px 12px;border:1px solid var(--line2);border-radius:20px;background:#fff;color:var(--muted);cursor:pointer;white-space:nowrap;user-select:none}
.chip:hover{border-color:var(--ink);color:var(--ink)}
.chip.on{background:var(--ink);color:#fff;border-color:var(--ink)}
.chip .n{opacity:.5;margin-left:5px;font-size:11px}
.chip.on .n{opacity:.6}
.srow{display:flex;align-items:center;gap:14px;flex-wrap:wrap;margin-top:4px}
#search{font:inherit;font-size:13.5px;padding:8px 13px;border:1px solid var(--line2);border-radius:9px;outline:none;width:240px}
#search:focus{border-color:var(--ink)}
.reset{font:inherit;font-size:12.5px;color:var(--blue);background:none;border:0;cursor:pointer;padding:0}
.reset:hover{text-decoration:underline}
.count{font-size:12.5px;color:var(--faint);font-variant-numeric:tabular-nums}
table{width:100%;border-collapse:collapse;font-size:13.5px}
th{text-align:left;font-size:10.5px;letter-spacing:.05em;text-transform:uppercase;color:var(--faint);font-weight:650;padding:0 9px 9px;border-bottom:1px solid var(--line2);cursor:pointer;white-space:nowrap;user-select:none}
th:hover{color:var(--ink)}th.nosort{cursor:default}th.nosort:hover{color:var(--faint)}
th.r,td.r{text-align:right;font-variant-numeric:tabular-nums}
th .ar{color:var(--ink);font-size:9px}
td{padding:9px;border-bottom:1px solid var(--line);vertical-align:middle}
tr.row:hover td{background:#fcfcfd}
.rk{color:var(--faint);font-variant-numeric:tabular-nums;font-size:12px}
.nm{font-weight:600;color:var(--ink)}
.prof{display:inline-block;font-size:11px;color:var(--blue);text-decoration:none;margin-left:6px;vertical-align:1px}
.prof:hover{text-decoration:underline}
.bio{font-size:11.5px;color:var(--faint);margin-top:2px;max-width:54ch;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.src{font-size:11px;color:var(--muted);max-width:30ch;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.pill{display:inline-block;font-size:10.5px;font-weight:600;padding:2px 8px;border-radius:5px;border:1px solid var(--line2);color:var(--muted);white-space:nowrap}
.fmt-video{color:#b8860b;border-color:#ecd9b0}
.fmt-mixed{color:var(--blue);border-color:#c5d8fb}
.pk{width:15px;height:15px;cursor:pointer;accent-color:var(--ink);vertical-align:middle}
th.pkh{width:26px;padding-left:0;cursor:default}td.pkc{padding-left:0;text-align:center}
tr.row.picked td{background:#f4f8f5}tr.row.picked:hover td{background:#eef5f0}
.foot{margin-top:30px;font-size:12.5px;color:var(--faint)}
.pickbar{position:fixed;left:0;right:0;bottom:0;z-index:9000;background:rgba(255,255,255,.94);backdrop-filter:blur(9px);border-top:1px solid var(--line2);padding:12px 30px;display:flex;align-items:center;gap:18px;flex-wrap:wrap}
.pickbar .pc{font-size:13px;font-weight:650;color:var(--ink);font-variant-numeric:tabular-nums}
.pickbar .pc .faint{color:var(--faint);font-weight:500}
.pickbar .clearp{font:inherit;font-size:12px;color:var(--blue);background:none;border:0;cursor:pointer}
.pickbar .clearp:hover{text-decoration:underline}
.pickbar .copyb{font:inherit;font-size:13px;font-weight:600;padding:10px 18px;border:0;border-radius:9px;background:var(--ink);color:#fff;cursor:pointer;margin-left:auto}
.pickbar .copyb:disabled{opacity:.4;cursor:default}
.pickbar .copied{font-size:12px;color:#11a36b;opacity:0;transition:opacity .2s}
</style></head>
<body><div class="wrap">

<p class="eyebrow">WorldFirst &middot; discovery &middot; broad pool &middot; <a href="uk.html" style="color:var(--blue);text-decoration:none">UK shortlist &rarr;</a></p>
<h1>Overseas Chinese KOL pool</h1>
<p class="sub">A deliberately <b>wide</b> net: overseas-based Chinese-language RedNote creators across every topic and format. This is the opposite of the WorldFirst scout, which gates hard to current ecommerce sellers, image-only posts, and the payment topic (that funnel finds ~5). Here the <b>only</b> hard gate is the one that actually matters: are they based overseas. Everything else is open and tagged so you can filter down to whatever a campaign needs.</p>
<div class="stamp">Swept 12 Jun 2026 &middot; 35 geo+topic queries &middot; one hard gate (overseas ip), fans 2k&ndash;500k, posted &ge;10 &middot; <b>__COUNT__ creators</b> &middot; 15 countries &middot; tagged by country, topic, format &middot; not contacted, discovery only</div>

<hr class="rule">

<div class="filters">
  <div class="frow"><span class="flabel">Country</span><div class="chips" id="f-country"></div></div>
  <div class="frow"><span class="flabel">Topic</span><div class="chips" id="f-topic"></div></div>
  <div class="frow"><span class="flabel">Format</span><div class="chips" id="f-format"></div></div>
  <div class="srow">
    <input id="search" type="text" placeholder="Search name or bio..." oninput="render()">
    <button class="reset" onclick="resetFilters()">Reset all</button>
    <span class="count" id="count"></span>
  </div>
</div>

<table id="tbl"><thead><tr>
  <th class="pkh nosort"></th>
  <th class="r nosort" style="width:30px">#</th>
  <th data-col="name">Creator</th>
  <th data-col="country">Country</th>
  <th data-col="topic">Topic</th>
  <th data-col="format">Format</th>
  <th data-col="fans" class="r">Fans <span class="ar">&#x2193;</span></th>
  <th data-col="lifetime_saves" class="r">Lifetime saves</th>
  <th data-col="src_saves" class="r">Top-note saves</th>
</tr></thead><tbody id="tbody"></tbody></table>

<div class="foot">Discovery only. No contacting, booking, or paying anyone. Loosened pool: traction shown is profile lifetime saves + the single harvested note that surfaced each creator (not a recent-feed median, unlike the WF scout). Use the WF scout board for campaign-grade vetting; use this to widen the net. Live TikHub data, 12 Jun 2026.</div>
</div>

<div class="pickbar">
  <span class="pc"><span id="pcount">0</span> <span class="faint">picked</span></span>
  <button class="clearp" id="clearp" onclick="clearPicks()" style="display:none">clear</button>
  <button class="copyb" id="copyb" disabled onclick="copyPicks()">Copy my picks</button>
  <span class="copied" id="copied">Copied</span>
</div>

<script>
const DATA = __DATA__;
const TOPIC_LABEL = {business:'Business',ecomm:'Ecommerce',finance_invest:'Finance/Invest',career_job:'Career/Job',study_abroad:'Study abroad',expat_life:'Expat life',food:'Food',travel:'Travel',beauty_fashion:'Beauty/Fashion',lifestyle:'Lifestyle',parenting:'Parenting',other:'Other'};
const fc=new Set(), ft=new Set(), ff=new Set();
const picks=new Set();
let sortCol='fans', sortAsc=false;

function fmtFans(n){return n>=10000?(n/10000).toFixed(1)+'w':n.toLocaleString();}
function fmtN(n){return n.toLocaleString();}
function counts(key){const m={};DATA.forEach(d=>{m[d[key]]=(m[d[key]]||0)+1});return m;}

function buildChips(){
  const cc=counts('country'), tc=counts('topic'), mc=counts('format');
  const ce=document.getElementById('f-country');
  Object.entries(cc).sort((a,b)=>b[1]-a[1]).forEach(([k,n])=>{
    ce.insertAdjacentHTML('beforeend',`<button class="chip" data-k="${k}" onclick="toggle('country','${k}',this)">${k}<span class="n">${n}</span></button>`);});
  const te=document.getElementById('f-topic');
  Object.entries(tc).sort((a,b)=>b[1]-a[1]).forEach(([k,n])=>{
    te.insertAdjacentHTML('beforeend',`<button class="chip" data-k="${k}" onclick="toggle('topic','${k}',this)">${TOPIC_LABEL[k]||k}<span class="n">${n}</span></button>`);});
  const fe=document.getElementById('f-format');
  ['image','video','mixed'].forEach(k=>{if(mc[k])fe.insertAdjacentHTML('beforeend',`<button class="chip" data-k="${k}" onclick="toggle('format','${k}',this)">${k}<span class="n">${mc[k]}</span></button>`);});
}
function toggle(kind,k,el){
  const set=kind==='country'?fc:kind==='topic'?ft:ff;
  if(set.has(k))set.delete(k);else set.add(k);
  el.classList.toggle('on',set.has(k));
  render();
}
function resetFilters(){
  fc.clear();ft.clear();ff.clear();
  document.querySelectorAll('.chip.on').forEach(c=>c.classList.remove('on'));
  document.getElementById('search').value='';
  render();
}
function filtered(){
  const q=document.getElementById('search').value.trim().toLowerCase();
  return DATA.filter(d=>{
    if(fc.size&&!fc.has(d.country))return false;
    if(ft.size&&!ft.has(d.topic))return false;
    if(ff.size&&!ff.has(d.format))return false;
    if(q&&!(d.name.toLowerCase().includes(q)||(d.bio||'').toLowerCase().includes(q)))return false;
    return true;
  });
}
function render(){
  let rows=filtered();
  rows.sort((a,b)=>{
    let av,bv;
    if(sortCol==='src_saves'){av=a.src_saves;bv=b.src_saves;}
    else if(sortCol==='name'||sortCol==='country'||sortCol==='topic'||sortCol==='format'){
      av=(a[sortCol]||'');bv=(b[sortCol]||'');return sortAsc?av.localeCompare(bv,'zh'):bv.localeCompare(av,'zh');}
    else{av=a[sortCol];bv=b[sortCol];}
    return sortAsc?av-bv:bv-av;
  });
  const tb=document.getElementById('tbody');tb.innerHTML='';
  rows.forEach((c,i)=>{
    const chk=picks.has(c.uid);
    const fcls=c.format==='video'?'fmt-video':c.format==='mixed'?'fmt-mixed':'';
    const tr=document.createElement('tr');
    tr.className='row'+(chk?' picked':'');
    tr.innerHTML=`
      <td class="pkc"><input type="checkbox" class="pk" ${chk?'checked':''} onclick="togglePick('${c.uid}',this)"></td>
      <td class="r rk">${i+1}</td>
      <td><span class="nm">${c.name}</span><a class="prof" href="https://www.xiaohongshu.com/user/profile/${c.uid}" target="_blank" rel="noopener">&#8599;&nbsp;XHS</a><div class="bio">${c.bio||''}</div></td>
      <td>${c.country}</td>
      <td>${TOPIC_LABEL[c.topic]||c.topic}</td>
      <td><span class="pill ${fcls}">${c.format}</span></td>
      <td class="r">${fmtFans(c.fans)}</td>
      <td class="r">${fmtN(c.lifetime_saves)}</td>
      <td class="r">${fmtN(c.src_saves)}</td>`;
    tb.appendChild(tr);
  });
  document.getElementById('count').textContent=`showing ${rows.length} of ${DATA.length}`;
  updateHeaders();
}
function updateHeaders(){
  document.querySelectorAll('th[data-col]').forEach(th=>{
    const col=th.dataset.col, base=th.textContent.replace(/[\\u2191\\u2193]/g,'').trim();
    th.innerHTML=base+(col===sortCol?' <span class="ar">'+(sortAsc?'&#x2191;':'&#x2193;')+'</span>':'');
  });
}
document.querySelectorAll('th[data-col]').forEach(th=>{
  th.addEventListener('click',()=>{const col=th.dataset.col;if(sortCol===col)sortAsc=!sortAsc;else{sortCol=col;sortAsc=false;}render();});
});
function togglePick(uid,el){if(picks.has(uid))picks.delete(uid);else picks.add(uid);el.closest('tr').classList.toggle('picked',picks.has(uid));updatePickbar();}
function clearPicks(){picks.clear();render();updatePickbar();}
function updatePickbar(){
  document.getElementById('pcount').textContent=picks.size;
  document.getElementById('copyb').disabled=picks.size===0;
  document.getElementById('clearp').style.display=picks.size?'inline':'none';
}
function copyPicks(){
  const sel=DATA.filter(d=>picks.has(d.uid));
  let t='== overseas_kol_pool ==\\n\\n'+sel.length+' creators picked from the broad overseas pool\\n\\n';
  sel.forEach(c=>{t+=`${c.name} | ${c.country} | ${TOPIC_LABEL[c.topic]||c.topic} | ${c.format} | ${fmtN(c.fans)} fans | ${fmtN(c.lifetime_saves)} lifetime saves | xiaohongshu.com/user/profile/${c.uid}\\n`;});
  t+='\\n> These passed the loosened pool gate (overseas + alive), NOT the WF campaign funnel.\\n> Vet for fit/format and re-pull recent feed before any brief. Never contact directly.\\n';
  navigator.clipboard.writeText(t).then(()=>{const e=document.getElementById('copied');e.style.opacity='1';setTimeout(()=>e.style.opacity='0',2200);});
}
buildChips();render();
</script></body></html>'''

html = html.replace('__DATA__', DATA).replace('__COUNT__', str(len(creators)))
open(os.path.join(D,'index.html'),'w',encoding='utf-8').write(html)
print('built index.html,', len(html), 'bytes,', len(creators), 'creators')
