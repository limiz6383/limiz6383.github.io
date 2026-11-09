# v4: theme, header, folder tabs, Fig rows + drawer, ask/fit rework
HEAD_SCRIPT = ("<script>(function(){var t=null;try{t=localStorage.getItem('theme')}catch(e){}"
               "if(t!=='light'&&t!=='dark')t=matchMedia('(prefers-color-scheme: light)').matches?'light':'dark';"
               "document.documentElement.setAttribute('data-theme',t)})()</script>")

def _svg(inner, cls=''):
    return f'<svg class="{cls}" viewBox="0 0 24 24" aria-hidden="true" focusable="false">{inner}</svg>'

ICON = {
 'mail': _svg('<path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><path d="M22 6l-10 7L2 6"/>'),
 'in': _svg('<path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"/><rect x="2" y="9" width="4" height="12"/><circle cx="4" cy="4" r="2"/>'),
 'gh': _svg('<path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"/>'),
 'doc': _svg('<path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5M12 11v6M9.5 14.5L12 17l2.5-2.5"/>'),
 'sun': _svg('<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/>', 'ic-sun'),
 'moon': _svg('<path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/>', 'ic-moon'),
 'x': _svg('<path d="M6 6l12 12M18 6L6 18"/>'),
}

UTIL = ('<header class="util"><span class="open"><i></i>open to new roles</span>'
  '<nav class="ulinks" aria-label="Contact and resume">'
  f'<a class="ib" href="mailto:mizuholi.ml@gmail.com" aria-label="Email" title="Email">{ICON["mail"]}</a>'
  f'<a class="ib" href="https://www.linkedin.com/in/mizuho-li" aria-label="LinkedIn" title="LinkedIn" target="_blank" rel="noopener">{ICON["in"]}</a>'
  f'<a class="ib" href="https://github.com/limiz6383" aria-label="GitHub" title="GitHub" target="_blank" rel="noopener">{ICON["gh"]}</a>'
  f'<a class="rbtn" href="#" data-resume>{ICON["doc"]}<span>Resume</span></a>'
  f'<button class="ib" id="theme" type="button" aria-label="Switch to light mode" title="Switch theme">{ICON["sun"]}{ICON["moon"]}</button>'
  '</nav></header>')

DRAWER = ('<div class="scrim" id="scrim" hidden></div>'
  '<aside class="drawer" id="drawer" role="dialog" aria-modal="true" aria-labelledby="dtitle" hidden tabindex="-1">'
  f'<div class="dhead"><span class="dfig" id="dfig"></span><button class="dclose" id="dclose" type="button" aria-label="Close details">{ICON["x"]}</button></div>'
  '<div class="dinner"><h2 id="dtitle"></h2><p class="ddate" id="ddate"></p><div class="dbody" id="dbody"></div></div></aside>')

ASK_BOX = ('<div class="box">'
  '<p class="askhead"><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M9 18h6M10 21h4M12 3a6 6 0 0 0-3.5 10.9c.6.5 1 1.2 1 2.1h5c0-.9.4-1.6 1-2.1A6 6 0 0 0 12 3z"/></svg>Ask me anything about my work</p>'
  '<form class="askrow" id="askform"><label for="askin" class="sr">Your question</label>'
  '<input id="askin" type="text" placeholder="e.g. How do you decide what to build first?" maxlength="200" autocomplete="off">'
  '<button class="btn primary" type="submit" id="askbtn">Ask</button></form>'
  '<p class="sugg">Not sure what to ask? Try one of these'
  '<svg class="sarrow" viewBox="0 0 60 40" aria-hidden="true" focusable="false"><g filter="url(#rough)"><path d="M6 8C22 4 40 12 46 30"/><path d="M38 26l8 6 3-10"/></g></svg></p>'
  '<div class="chips" id="chips"></div>'
  '<div class="answer" id="answer" aria-live="polite"><span class="q">Pick a question or type your own</span>Answers come from my resume and projects, nothing else.</div>'
  '<p class="note" id="asknote">Suggested questions use answers I wrote ahead of time. A question of your own is answered by Claude from the facts on this page, and I rate limit it.</p>'
  '</div>')

ASK_JS = r'''/* ---------- ask section ---------- */
const chips = document.getElementById('chips'), ans = document.getElementById('answer');
let streamTimer = null;
function show(q, a, stream){
  clearInterval(streamTimer);
  ans.innerHTML = ''; const s = document.createElement('span'); s.className='q'; s.textContent = q;
  const body = document.createElement('span'); ans.append(s, body);
  if(!stream || matchMedia('(prefers-reduced-motion: reduce)').matches){ body.textContent = a; return; }
  let i = 0; ans.classList.add('typing');
  streamTimer = setInterval(()=>{ i = Math.min(a.length, i + 3); body.textContent = a.slice(0,i); if(i>=a.length){ clearInterval(streamTimer); ans.classList.remove('typing'); } }, 16);
}
QA.forEach(([q,a])=>{
  const b = document.createElement('button'); b.type='button'; b.className='chip'; b.textContent=q; b.setAttribute('aria-pressed','false');
  b.onclick = ()=>{ chips.querySelectorAll('.chip').forEach(c=>c.setAttribute('aria-pressed','false')); b.setAttribute('aria-pressed','true'); show(q,a,true); };
  chips.append(b);
});
const STOP = new Set('a an the and or of to in on for with at by is are do does did you your i me my it this that what how why when where who can could would should about from as be have has'.split(' '));
const toks = t => (t.toLowerCase().match(/[a-z0-9+]+/g)||[]).filter(w=>w.length>2 && !STOP.has(w));
function bestSaved(q){
  const qt = new Set(toks(q)); if(!qt.size) return null;
  let best=null, score=0;
  QA.forEach(([sq,sa])=>{ const st = new Set(toks(sq)); let n=0; qt.forEach(w=>{ if(st.has(w)) n++; });
    const s = n / Math.max(2, Math.min(qt.size, st.size)); if(s>score){ score=s; best=[sq,sa]; } });
  return score >= 0.6 ? best : null;
}
let sample = null;
(async ()=>{ try { sample = await (window.claude && window.claude.use ? window.claude.use('sample') : null); } catch(e){ sample = null; } })();
const ASKLIM = { last:0, n:0 };
document.getElementById('askform').addEventListener('submit', async ev=>{
  ev.preventDefault();
  const inp = document.getElementById('askin'), q = inp.value.trim().slice(0,200); if(!q) return;
  chips.querySelectorAll('.chip').forEach(c=>c.setAttribute('aria-pressed','false'));
  const saved = bestSaved(q);
  if(saved){ show(saved[0], saved[1], true); inp.value=''; return; }
  if(!sample){ show(q, "I do not have that on this page. Try one of the suggested questions, or email me at mizuholi.ml@gmail.com.", true); inp.value=''; return; }
  const now = Date.now();
  if(now - ASKLIM.last < 8000){ show(q, 'One moment, I can take a new question every few seconds.'); return; }
  if(ASKLIM.n >= 6){ show(q, 'That is plenty of questions for now. Pick a suggested one above, or email me at mizuholi.ml@gmail.com.'); return; }
  ASKLIM.last = now; ASKLIM.n++;
  const btn = document.getElementById('askbtn'); btn.disabled = true;
  show(q, 'Thinking...');
  try {
    const r = await sample(
      `You answer questions from recruiters about Mizuho Li, speaking as Mizuho in first person. Use ONLY the facts below. If the question is not about Mizuho's work, experience, skills or projects, or the facts do not cover it, say you do not have that on this page and suggest emailing mizuholi.ml@gmail.com. Never invent employers, metrics, dates, or skills. Keep answers under 90 words, plain text, no markdown.\n\nFACTS:\n${FACTS}\n\nQUESTION: ${q}`,
      { cache:false, modelTier:'quick', kind:'ask', q });
    show(q, r.text, true);
  } catch(e){
    if(e && e.code==='off_topic'){ show(q, 'That one is outside what I can answer here. I am happy to talk about my work, projects, how I think about product, or what I am looking for. Try a suggested question, or email me at mizuholi.ml@gmail.com.', true); btn.disabled=false; return; }
    show(q, e && e.code==='rate_limited' ? 'Too many questions in a short time. Try again in a minute, or pick a suggested question.' : 'I could not get an answer right now. Pick a suggested question, or email mizuholi.ml@gmail.com.');
  }
  btn.disabled = false; inp.value='';
});

'''

FIT_GUARD = r'''
const JOBWORDS=['responsib','requirement','qualif','experience','you will','we are looking','looking for','the role','our team','product','manager','engineer','years','skills','about the','what you','apply','candidate','position','hiring','benefits','preferred','degree','collaborat','stakeholder'];
function looksLikeJob(t){ const s=t.toLowerCase(); return t.length>=200 && JOBWORDS.filter(w=>s.includes(w)).length>=4; }
const FITLIM={last:0,n:0};
function notJob(){
  res.innerHTML='<p class="mhead nj"><span class="rest">Of course it\'s a</span> <span class="ten">10/10</span> <span class="rest">fit, if you ask me</span> <svg class="smirk" viewBox="0 0 40 40" role="img" aria-label="smirking face"><g filter="url(#rough)"><path d="M20 4C11 3.6 4 10.5 4.4 20 4.8 29.5 12 36.4 21 35.8 30 35.2 36.4 28 35.8 19 35.3 10.8 29 4.3 20 4z"/><path d="M9.5 12.6c3-1.4 6-1.2 8.4.2"/><path d="M22.6 8.8c2.8-2 6-2 8.6-.2"/><path d="M9.6 18.8h8.6M22.4 18.8h8.6"/><path d="M10.6 18.8c.8 3 6 3 7 0M23.4 18.8c.8 3 6 3 7 0"/><circle cx="16.4" cy="21" r="1.1" fill="currentColor"/><circle cx="29.2" cy="21" r="1.1" fill="currentColor"/><path d="M13 28.4c4 1.2 9.6 .8 14.6-3.2"/><path d="M27.6 25.2l2.6-.4"/></g></svg></p><p class="njsub">That does not look like a job description though. Paste the responsibilities and requirements and I\'ll show you the receipts.</p>';
  res.classList.add('on'); setTimeout(()=>burst(res.querySelector('.ten')),250);
}
'''
FIT_CHECK = r'''if(!looksLikeJob(text)){ notJob(); return; }
  { const now=Date.now(); if(now-FITLIM.last<12000){ res.innerHTML='<p class="note">Give me a few seconds between checks.</p>'; res.classList.add('on'); return; } FITLIM.last=now; FITLIM.n++; }
  const useAI = FITLIM.n<=4;
  '''

CSS = r'''
html:root[data-theme="dark"]{--paper:#0E1512;--wash:#151F1A;--ink:#F2EFE5;--muted:#A9B5AB;--soft:#D6DBD0;--line:#2B3A33;--accent:#A9B9FF;--accent-soft:#1D2644;--hand:#F2D35E;--thumbbg:#151F1A;--ifill:#151F1A;color-scheme:dark}
html:root[data-theme="light"]{--paper:#F7F3E9;--wash:#EFE9D9;--ink:#16211B;--muted:#586359;--soft:#2D3830;--line:#D6CEB9;--accent:#3347C9;--accent-soft:#E1E5FB;--hand:#A97800;--thumbbg:#EFE9D9;--ifill:#EFE9D9;color-scheme:light}
body{transition:background-color .25s,color .25s}
.sr{position:absolute;left:-9999px}
/* utility bar */
.util{display:flex;align-items:center;justify-content:space-between;gap:var(--s4);padding:var(--s2) max(16px,calc((100vw - 980px)/2 + 40px));border-bottom:1px solid var(--line);flex-wrap:wrap}
.util .open{margin:0;font-size:14.5px}
.ulinks{display:flex;align-items:center;gap:6px}
.ib{display:inline-flex;align-items:center;justify-content:center;width:40px;height:40px;padding:0;border-radius:10px;color:var(--soft);border:1px solid transparent;background:none;cursor:pointer;text-decoration:none;transition:color .2s,background-color .2s,border-color .2s}
.ib:hover,.ib:focus-visible{color:var(--ink);background:var(--wash);border-color:var(--line)}
.ib svg,.rbtn svg{width:20px;height:20px;fill:none;stroke:currentColor;stroke-width:1.7;stroke-linecap:round;stroke-linejoin:round}
.rbtn{display:inline-flex;align-items:center;gap:8px;height:40px;padding:0 14px 0 11px;margin:0 6px;border:1px solid var(--ink);border-radius:10px;font:500 14.5px var(--body);color:var(--ink);text-decoration:none;transition:background-color .2s,color .2s}
.rbtn:hover,.rbtn:focus-visible{background:var(--ink);color:var(--paper)}
html[data-theme="dark"] .ic-moon{display:none}html[data-theme="light"] .ic-sun{display:none}
.top{padding-top:clamp(24px,5vh,56px)!important}
@media (max-width:560px){.util{flex-direction:column;align-items:flex-start;gap:4px}.rbtn{margin:0 4px}}
/* folder tabs */
.tabs{display:flex;gap:6px;margin:calc(var(--s12) - 6px) 0 0!important;padding:6px var(--s1) 0!important;overflow-x:auto;overflow-y:hidden;scrollbar-width:none;align-items:flex-end;border:0!important}
.tabs::-webkit-scrollbar{display:none}
.tabs button{all:unset;box-sizing:border-box;cursor:pointer;white-space:nowrap;padding:12px 20px 11px!important;font:500 15px var(--body)!important;color:var(--muted)!important;border:1px solid var(--line);border-bottom:0;border-radius:12px 12px 0 0;background:transparent;position:relative;margin-bottom:0;transition:color .2s,background-color .2s}
.tabs button:hover{color:var(--ink)!important;background:color-mix(in srgb,var(--wash) 60%,transparent)}
.tabs button:focus-visible{outline:2px solid var(--accent);outline-offset:-4px}
.tabs button[aria-selected="true"]{color:var(--ink)!important;background:var(--wash);margin-bottom:-1px;padding-bottom:12px!important;z-index:2;border-color:var(--line);border-bottom:1px solid var(--wash)}
.tabs button[aria-selected="true"]::after{display:none!important}
.panel{background:var(--wash);border:1px solid var(--line);border-radius:14px;padding:var(--s8) var(--s8) var(--s6);position:relative;z-index:1}
.tabs:has(button:first-child[aria-selected="true"])~.panel{border-top-left-radius:0}
.panel .box{border:0!important;padding:0!important;background:transparent!important}
@media (max-width:700px){.panel{padding:var(--s6) var(--s4) var(--s4)}.tabs button{padding:11px 14px 10px!important;font-size:14.5px!important}}
/* project rows as numbered figures */
.panel#work,.panel#builds{counter-reset:fig}
.panel#work .item,.panel#builds .item{border-bottom:1px solid var(--line)}
.panel#work .item summary,.panel#builds .item summary{display:grid!important;grid-template-columns:minmax(0,1fr) minmax(220px,300px)!important;grid-template-rows:auto auto 1fr auto!important;column-gap:var(--s8)!important;row-gap:6px!important;padding:var(--s8) 0!important;align-items:start!important;align-content:start!important}
.panel#work .item .t,.panel#builds .item .t{grid-column:1!important;grid-row:1!important;font:500 20px/1.25 var(--body)!important;color:var(--ink)}
.panel#work .item .s,.panel#builds .item .s{grid-column:1!important;grid-row:2!important;font:500 11.5px/1 ui-monospace,SFMono-Regular,Menlo,monospace!important;letter-spacing:.08em;text-transform:uppercase;color:var(--muted)!important;margin-bottom:6px}
.panel#work .item .d,.panel#builds .item .d{grid-column:1!important;grid-row:3!important;font:400 16px/1.6 var(--body)!important;color:var(--soft)!important;padding:0!important;letter-spacing:0}
.item .more{grid-column:1;grid-row:4;align-self:end;margin-top:var(--s3);font:500 14.5px var(--body);color:var(--muted);display:inline-flex;gap:8px;align-items:center;transition:color .2s,gap .2s}
.item .more i{font-style:normal;transition:transform .25s}
.item summary:hover .more,.item summary:focus-visible .more{color:var(--accent)}
.item summary:hover .more i{transform:translateX(4px)}
.panel#work .item .plus,.panel#builds .item .plus{display:none!important}
.panel#work .item summary,.panel#builds .item summary{cursor:pointer}
.panel#work .item .thumb,.panel#builds .item .thumb{display:flex!important;align-items:center;justify-content:center;position:relative;grid-column:2!important;grid-row:1 / 5!important;align-self:stretch!important;margin:0!important;width:auto!important;min-height:158px;height:auto!important;overflow:visible!important;border:1px solid var(--line)!important;border-radius:12px;background-color:var(--paper)!important;background-image:radial-gradient(color-mix(in srgb,var(--ink) 16%,transparent) 1px,transparent 1.3px);background-size:16px 16px;padding:30px 18px 14px!important;transition:border-color .25s}
.panel#work .item .thumb::before,.panel#builds .item .thumb::before{counter-increment:fig;content:"FIG " counter(fig) ".0";position:absolute;left:14px;top:11px;font:500 10.5px/1 ui-monospace,SFMono-Regular,Menlo,monospace;letter-spacing:.12em;color:var(--muted)}
.panel#work .item .thumb svg,.panel#builds .item .thumb svg{width:100%!important;max-width:220px;height:auto!important;margin:0!important}
.item summary:hover .thumb{border-color:var(--muted)!important}
.item summary:hover .t,.item summary:focus-visible .t{color:var(--accent)!important}
@media (max-width:700px){
 .panel#work .item summary,.panel#builds .item summary{grid-template-columns:minmax(0,1fr)!important;grid-template-rows:auto auto auto auto auto!important;padding:var(--s6) 0!important}
 .panel#work .item .thumb,.panel#builds .item .thumb{grid-column:1!important;grid-row:3!important;width:100%!important;min-height:150px;margin:var(--s3) 0 var(--s2)!important}
 .panel#work .item .d,.panel#builds .item .d{grid-row:4!important}.item .more{grid-row:5}
 .panel#work .item .thumb svg,.panel#builds .item .thumb svg{max-width:240px}}
/* drawer */
body.lock{overflow:hidden}
.scrim{position:fixed;inset:0;background:color-mix(in srgb,#000 58%,transparent);opacity:0;transition:opacity .3s;z-index:55}
.scrim.on{opacity:1}
.drawer{position:fixed;left:50%;top:50%;width:min(780px,calc(100vw - 32px));max-height:min(88vh,900px);max-height:min(88dvh,900px);background:var(--paper);border:1px solid var(--line);border-radius:18px;box-shadow:0 30px 80px color-mix(in srgb,#000 45%,transparent);z-index:60;transform:translate(-50%,-47%) scale(.97);opacity:0;transition:transform .3s cubic-bezier(.2,.8,.2,1),opacity .25s;overflow-y:auto;overscroll-behavior:contain;outline:none}
.drawer.on{transform:translate(-50%,-50%);opacity:1}
.dhead{border-radius:18px 18px 0 0}
.dhead{position:sticky;top:0;z-index:2;display:flex;align-items:center;justify-content:space-between;padding:14px var(--s8);background:color-mix(in srgb,var(--paper) 94%,transparent);backdrop-filter:blur(8px);border-bottom:1px solid var(--line)}
.dfig{font:500 11px/1 ui-monospace,SFMono-Regular,Menlo,monospace;letter-spacing:.12em;color:var(--muted)}
.dclose{all:unset;box-sizing:border-box;cursor:pointer;width:40px;height:40px;display:inline-flex;align-items:center;justify-content:center;border-radius:10px;border:1px solid var(--line);color:var(--ink);transition:background-color .2s}
.dclose:hover,.dclose:focus-visible{background:var(--wash)}.dclose:focus-visible{outline:2px solid var(--accent)}
.dclose svg{width:20px;height:20px;fill:none;stroke:currentColor;stroke-width:1.8;stroke-linecap:round}
.dinner{padding:var(--s8) var(--s8) var(--s24)}
.dinner h2{font:500 clamp(26px,3vw,32px)/1.15 var(--display);margin:0 0 6px}
.ddate{margin:0 0 var(--s8);font:500 11.5px/1 ui-monospace,SFMono-Regular,Menlo,monospace;letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}
.drawer .body{display:block!important;padding:0!important;border:0!important}
.drawer .body .row{border:0}
.drawer .body p,.drawer .body li{font-size:16px!important;line-height:1.65!important;color:var(--soft);max-width:none!important}
.drawer .body .statement{font:500 clamp(24px,2.6vw,28px)/1.25 var(--display)!important;color:var(--ink);margin:0 0 var(--s4)}
.drawer .body .statement .now,.drawer .body .num{color:var(--accent)}
.drawer .body .after{color:var(--ink)}
.drawer .body .cols3{display:block!important}
.drawer .body .cols3>div{margin:0 0 var(--s6)!important}
.drawer .body h4{font:500 11.5px/1 ui-monospace,SFMono-Regular,Menlo,monospace!important;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);margin:var(--s6) 0 var(--s2)!important}
.drawer .body img,.drawer .body figure img{max-width:100%;height:auto}
.drawer .how-art .hz{display:block;width:100%;height:auto}
@media (max-width:620px){.drawer .how-art .hz{display:none}.drawer .how-art .vt{display:block;max-width:340px}}
.drawer.on .how .nd{animation:pop .55s cubic-bezier(.2,.8,.2,1) backwards;animation-delay:calc(var(--i)*.22s)}
.drawer.on .how .arrow path:first-child{stroke-dasharray:1;stroke-dashoffset:0;animation:drawA .5s ease-out backwards;animation-delay:calc(var(--i)*.22s + .18s)}
.drawer.on .how .arrow .head{animation:fadeA .3s ease-out backwards;animation-delay:calc(var(--i)*.22s + .55s)}
.drawer .tags{margin-top:var(--s6)}
@media (max-width:700px){.drawer{width:100vw;height:100dvh;max-height:none;border:0;border-radius:0;top:0;left:0;transform:translateY(16px);}.drawer.on{transform:none}.dhead{border-radius:0;padding:12px var(--s4)}.dinner{padding:var(--s6) var(--s4) var(--s16)}}
@media (prefers-reduced-motion:reduce){.drawer,.scrim{transition:none}.drawer.on .how *{animation:none!important}}
/* ask me */
.askhead{display:flex;align-items:center;gap:10px;margin:0 0 var(--s3);font:500 19px var(--body);color:var(--ink)}
.askhead svg{width:26px;height:26px;flex:none;fill:none;stroke:var(--hand);stroke-width:1.7;stroke-linecap:round;stroke-linejoin:round}
.askrow{display:flex;gap:var(--s2);margin:0!important;flex-wrap:nowrap}
.askrow input{flex:1;min-width:0;font:400 16px var(--body);padding:14px 16px;border:1px solid var(--line);border-radius:12px;background:var(--paper);color:var(--ink)}
.askrow input:focus{outline:2px solid var(--accent);outline-offset:1px;border-color:transparent}
.askrow .btn{border-radius:12px;padding:0 22px}
.sugg{position:relative;margin:var(--s6) 0 var(--s3);font:500 14px var(--body);color:var(--muted)}
.sarrow{display:inline-block;width:46px;height:30px;margin-left:8px;vertical-align:-10px;fill:none;stroke:var(--hand);stroke-width:2;stroke-linecap:round;stroke-linejoin:round}
.chips{gap:var(--s2)}
.chip{border-radius:999px!important;padding:9px 16px!important;font:500 14.5px var(--body)!important;color:var(--soft)!important;background:var(--paper)!important;min-height:0!important}
.chip:hover{border-color:var(--muted)!important;color:var(--ink)!important}
.chip[aria-pressed="true"]{border-color:var(--accent)!important;color:var(--accent)!important;background:var(--accent-soft)!important}
.answer{border-radius:12px;margin-top:var(--s6)!important;font-size:16.5px!important;line-height:1.65;background:var(--paper)!important}
.answer.typing>span:last-child::after{content:"";display:inline-block;width:7px;height:1.05em;margin-left:2px;vertical-align:-2px;background:var(--hand);animation:blink 1s steps(2) infinite}
@keyframes blink{50%{opacity:0}}
.note{font-size:14px!important;color:var(--muted)!important}
/* fit */
#jdres{container-type:inline-size}
.mhead.nj{display:block;width:100%;max-width:none;margin:0 0 var(--s3);font-size:clamp(22px,5.2cqw,56px);line-height:1.12;text-wrap:balance}
.mhead.nj .ten{font-size:1em}
.njsub{margin:0;font-size:17px;line-height:1.6;color:var(--soft);max-width:none}
.smirk{display:inline-block;width:1.25em;height:1.25em;vertical-align:-.25em;color:var(--hand);fill:none;stroke:var(--hand);stroke-width:2.2;stroke-linecap:round;stroke-linejoin:round}
#jdtext{border-radius:12px!important;background:var(--paper)!important;font-size:16px}
.panel .box label{font-size:14.5px}
'''

JS = r'''
/* theme toggle */
(function(){const b=document.getElementById('theme');if(!b)return;
  function apply(t){document.documentElement.setAttribute('data-theme',t);b.setAttribute('aria-label',t==='dark'?'Switch to light mode':'Switch to dark mode')}
  apply(document.documentElement.getAttribute('data-theme')||'dark');
  b.addEventListener('click',()=>{const t=document.documentElement.getAttribute('data-theme')==='dark'?'light':'dark';apply(t);try{localStorage.setItem('theme',t)}catch(e){}});
})();
/* detail drawer */
(function(){
  const drawer=document.getElementById('drawer'),scrim=document.getElementById('scrim'),dbody=document.getElementById('dbody'),
        dtitle=document.getElementById('dtitle'),ddate=document.getElementById('ddate'),dfig=document.getElementById('dfig'),dclose=document.getElementById('dclose');
  let cur=null,body=null,lastFocus=null,closing=null;
  function open(item){
    if(cur)return; clearTimeout(closing);
    cur=item; body=item.querySelector('.body'); lastFocus=document.activeElement;
    dtitle.textContent=item.querySelector('.t').textContent;
    const s=item.querySelector('.s'); ddate.textContent=s?s.textContent:''; ddate.hidden=!s;
    const sib=[...item.parentElement.querySelectorAll('.item')]; dfig.textContent='FIG '+(sib.indexOf(item)+1)+'.0';
    dbody.appendChild(body); drawer.hidden=false; scrim.hidden=false; document.body.classList.add('lock'); drawer.scrollTop=0;
    requestAnimationFrame(()=>{drawer.classList.add('on');scrim.classList.add('on');dclose.focus({preventScroll:true})});
    dbody.querySelectorAll('figure[data-how]').forEach(f=>f.__auto&&f.__auto());
  }
  function close(){
    if(!cur)return;
    dbody.querySelectorAll('figure[data-how]').forEach(f=>f.__stop&&f.__stop());
    drawer.classList.remove('on');scrim.classList.remove('on');document.body.classList.remove('lock');
    const item=cur,b=body; cur=null;
    closing=setTimeout(()=>{item.appendChild(b);drawer.hidden=true;scrim.hidden=true},340);
    if(lastFocus&&lastFocus.focus)lastFocus.focus({preventScroll:true});
  }
  document.querySelectorAll('.panel .item').forEach(item=>{
    const sum=item.querySelector('summary'); sum.setAttribute('role','button'); sum.setAttribute('aria-haspopup','dialog');
    sum.addEventListener('click',e=>{e.preventDefault();open(item)});
  });
  dclose.addEventListener('click',close); scrim.addEventListener('click',close);
  addEventListener('keydown',e=>{
    if(!cur)return;
    if(e.key==='Escape'){e.preventDefault();close();return}
    if(e.key==='Tab'){const f=[...drawer.querySelectorAll('a[href],button,[tabindex="0"],input,textarea')].filter(x=>!x.disabled&&x.offsetParent!==null);
      if(!f.length)return;const a=f[0],z=f[f.length-1];
      if(e.shiftKey&&(document.activeElement===a||document.activeElement===drawer)){e.preventDefault();z.focus()}
      else if(!e.shiftKey&&document.activeElement===z){e.preventDefault();a.focus()}}
  });
})();
'''
