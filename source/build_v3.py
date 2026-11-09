import re,base64,illus
B=open('/home/claude/portfolio/src_v1_backup.html').read()
def between(a,b,start=0):
    i=B.index(a,start); j=B.index(b,i+len(a)); return B[i:j]
def _ff(fam,wt,path):
    d=base64.b64encode(open('/tmp/fz/node_modules/@fontsource/'+path,'rb').read()).decode()
    return "@font-face{font-family:'%s';font-style:normal;font-weight:%s;font-display:swap;src:url(data:font/woff2;base64,%s) format('woff2')}"%(fam,wt,d)
fonts='<style>'+_ff('Newsreader','500','newsreader/files/newsreader-latin-500-normal.woff2')+_ff('Newsreader','500','newsreader/files/newsreader-latin-500-italic.woff2').replace('font-style:normal','font-style:italic')+''.join(_ff('Hanken Grotesk',w,'hanken-grotesk/files/hanken-grotesk-latin-%s-normal.woff2'%w) for w in ('400','500','600'))+_ff('Caveat','600','caveat/files/caveat-latin-600-normal.woff2')+'</style>'
root=between(':root{',"*{box-sizing:border-box}")
btn=''.join(l+'\n' for l in B.split('\n') if l.startswith('.btn'))
mid=between('/* work */','footer{')
# ---- content pieces
def articles(cls):
    return re.findall(r'<article class="%s">(.*?)</article>'%cls,B,flags=re.S)
work=articles('row'); proj=articles('proj')
WORK={'Agentic Creative Platform':('Jun 2026 – present','Carved out an MVP around the limits of image generation: designer time per mockup fell from ~30 hours to ~6, with ~10 minutes of system generation time.'),
'Ad Quality':('Nov 2025 – May 2026','An ML model that blocks policy-violating ads before players see them, about 20,000 a month.'),
'Publisher Tooling':('Jul 2025 – Nov 2025','Monthly resolution of tooling requests went from 10% to about 50%.')}
BUILD={'Trip Planner':"An AI travel planner that builds a personalized trip around your travel style and any bookings you already have, then lets you chat to revise the itinerary at every step.",
'Cycle Insights':"An AI assistant that gives personalized hormonal insights and nutrition advice for your cycle stage. Every claim is backed by research and checked by an evaluation framework to prevent false information.",
'Fintracker':"A finance dashboard that connects your accounts to show your net worth, analyze your spending, and advise on your goals. Its investment tab suggests next steps using economic and political context."}
def item(title,sub,date,body,thumb=''):
    d=f'<span class="s">{date}</span>' if date else ''
    th=f'<span class="thumb" aria-hidden="true">{thumb}</span>' if thumb else ''
    return f'<details class="item"><summary><span class="t">{title}</span>{d}{th}<span class="d">{sub}</span><span class="plus" aria-hidden="true"></span></summary><div class="body">{body}</div></details>'

THUMB={'Trip Planner':'''<svg viewBox="0 0 160 100" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path class="trail" d="M16 80C40 82 44 44 72 46S116 84 142 32" stroke-dasharray="2 5"/><circle cx="16" cy="80" r="4"/><circle cx="72" cy="46" r="4"/><g class="pin"><circle cx="142" cy="28" r="7"/><circle cx="142" cy="28" r="2" fill="currentColor"/></g><g class="lock"><rect x="56" y="58" width="20" height="14" rx="2"/><path d="M60 58v-4a6 6 0 0 1 12 0v4"/></g><g class="bubble"><path d="M20 12h42a4 4 0 0 1 4 4v14a4 4 0 0 1-4 4H40l-8 7v-7h-12a4 4 0 0 1-4-4V16a4 4 0 0 1 4-4z"/><circle cx="30" cy="23" r="1.4" fill="currentColor"/><circle cx="40" cy="23" r="1.4" fill="currentColor"/><circle cx="50" cy="23" r="1.4" fill="currentColor"/></g><path class="plane" d="M0 0l11 4.5-11 4.5 3-4.5z" fill="currentColor"/></svg>''','Cycle Insights':'''<svg viewBox="0 0 160 100" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 84H148" stroke-opacity=".35"/><path class="wave" d="M12 66C30 24 58 24 76 60S122 100 148 46"/><path d="M76 64V84" stroke-dasharray="2 4"/><circle class="now" cx="0" cy="0" r="4.5" fill="currentColor"/><path d="M20 30c0-10 9-16 20-16 0 11-7 19-20 16z"/><path d="M22 28l12-9"/><g><path d="M112 10h16l8 8v22h-24z"/><path d="M128 10v8h8"/><path d="M117 26h14M117 32h10"/><circle cx="136" cy="38" r="6" fill="#161513"/><path class="tick" d="M132.6 38.4l2.4 2.4 4.4-5"/></g></svg>''','Fintracker':'''<svg viewBox="0 0 160 100" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 14V82H98" stroke-opacity=".35"/><path class="line" d="M18 70L38 58 56 64 76 40 94 30" /><circle cx="38" cy="58" r="2.4"/><circle cx="56" cy="64" r="2.4"/><circle cx="76" cy="40" r="2.4"/><circle class="end" cx="94" cy="30" r="5" fill="currentColor"/><g><rect x="110" y="18" width="9" height="9" rx="1.5"/><path class="t1" d="M112 22.5l2 2 3-4"/><path d="M125 22.5h24"/><rect x="110" y="40" width="9" height="9" rx="1.5"/><path class="t2" d="M112 44.5l2 2 3-4"/><path d="M125 44.5h20"/><rect x="110" y="62" width="9" height="9" rx="1.5"/><path class="t3" d="M112 66.5l2 2 3-4"/><path d="M125 66.5h22"/></g></svg>'''}
work_html=''
for a in work:
    t=re.search(r'<h3>(.*?)</h3>',a).group(1); date,sub=WORK[t]
    body=a[a.index('</div>',a.index('class="rowhead"'))+6:]
    work_html+=item(t,sub,date,body,illus.thumb(t))
build_html=''
for a in proj:
    t=re.search(r'<h3>(.*?)</h3>',a).group(1)
    body=a[a.index('</h3>')+5:]
    build_html+=item(t,BUILD[t],'',illus.build(t)+body,illus.thumb(t))
box_ask=between('<div class="box">','\n    </div>\n  </div></section>',B.index('id="ask"'))
box_fit=between('<div class="box">','\n    </div>\n  </div></section>',B.index('id="match"'))
about=between('<div class="aboutbody">','\n</div>\n      </div>\n    </div>\n  </div></section>')
about=about.replace('<div class="aboutbody">','',1)
js=between('<script>','</script>',B.index('<footer>'))
js=js.replace(between('/* ---------- hero blinds','/* ---------- facts'),'')
js=js.replace('<script>','',1)
js=js.replace("let sample = null;","""const AI_PROXY = 'https://limiz6383githubio-proxy-nl1xkgr8m-mizuho1.vercel.app/api/ai';
function proxySample(){
  const call = async (prompt,opts,json)=>{
    const r = await fetch(AI_PROXY,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({prompt:json?prompt+'\\n\\nRespond with ONLY valid JSON, no markdown fences.':prompt,tier:(opts&&opts.modelTier)==='quick'?'quick':'default'})});
    if(r.status===429){const e=new Error('rate');e.code='rate_limited';throw e}
    if(!r.ok) throw new Error('proxy '+r.status);
    return (await r.json()).text||'';
  };
  const f = async (prompt,opts)=>{const text=await call(prompt,opts,false);return {text}};
  f.json = async (prompt,opts)=>{const t=(await call(prompt,opts,true)).replace(/^```(?:json)?\\s*|\\s*```$/g,'').trim();return JSON.parse(t)};
  return f;
}
let sample = null;""",1)
js=js.replace("sample = await (window.claude && window.claude.use ? window.claude.use('sample') : null); } catch(e){ sample = null; }","sample = await (window.claude && window.claude.use ? window.claude.use('sample') : null); } catch(e){ sample = null; }\n  if(!sample && AI_PROXY) sample = proxySample();",1)

js=js.replace(between('/* portrait: she turns','/* resume download'),'''/* portrait: hover and she waves hello */
(function(){
  const me=document.querySelector('.me'); if(!me)return;
  const wrap=me.parentElement; let off=null;
  const on=()=>{me.classList.add('on');clearTimeout(off)};
  const out=()=>{me.classList.remove('on')};
  wrap.addEventListener('pointerenter',e=>{on(); if(e.pointerType!=='mouse')off=setTimeout(out,2600)});
  wrap.addEventListener('pointerleave',out);
  wrap.addEventListener('click',()=>{on();off=setTimeout(out,2600)});
})();

''')

art=re.search(r'<figure class="me">.*?</figure>',B,flags=re.S).group(0)
art='''<figure class="me"><div class="art base" role="img" aria-label="Line drawing of Mizuho Li laughing, with sunglasses on her head, a knit scarf and a quilted bag, standing among pumpkins" style="--art:url({{ART_BASE}})"></div>
<div class="art wv" aria-hidden="true" style="--art:url({{ART_WAVE}})"></div>
<span class="hi" aria-hidden="true">hi!</span></figure>'''

css='''
:root{--hand:#E8C77A}
html{scroll-padding-top:20px;overflow-x:clip}body{overflow-x:clip}
body{font-size:16.5px}
.col{max-width:660px;margin:0 auto;padding:0 var(--s6)}
.top{padding:var(--s16) 0 0}
.head{display:flex;align-items:flex-end;justify-content:space-between;gap:var(--s4);margin-bottom:var(--s6)}
.me{aspect-ratio:900/1130;transform:none}
.art.wv{opacity:0;transform-origin:50% 100%;transition:opacity .4s ease .1s}
.art.base{opacity:1;transition:opacity .3s ease}
.me.on .art.wv{opacity:1;transition:opacity .45s ease;animation:sway 1.7s ease-in-out .3s infinite}
.me.on .art.base{opacity:0;transition:opacity .3s ease .3s}
@keyframes sway{0%,100%{transform:rotate(0)}25%{transform:rotate(-1.2deg)}75%{transform:rotate(1.2deg)}}
.hi{position:absolute;left:2%;top:6%;font:600 22px/1 'Caveat',cursive;color:var(--hand);opacity:0;transform:translateY(8px) rotate(4deg) scale(.85);pointer-events:none;transition:opacity .3s,transform .3s}
.me.on .hi{opacity:1;transform:rotate(8deg);transition:opacity .5s .3s,transform .7s cubic-bezier(.2,1.4,.4,1) .3s}
@media (prefers-reduced-motion:reduce){.me.on .art.wv{animation:none}}
.meWrap{width:clamp(110px,26vw,170px);flex:none;transform:rotate(-3deg);transform-origin:50% 60%;margin:0 -6px -6px 0}
h1.is{font:400 clamp(50px,11vw,76px)/1 var(--display);letter-spacing:-.015em;margin:0;display:flex;flex-wrap:wrap;align-items:baseline;gap:0 .28em}
.hand{font:600 1.18em/1 'Caveat',cursive;color:var(--hand);display:inline-block;position:relative;letter-spacing:0;min-width:3ch}
.hand span{display:inline-block;padding:0 .14em 0 .04em;margin-right:-.14em;animation:handin .55s cubic-bezier(.2,.9,.3,1) both}
@keyframes handin{from{opacity:0;transform:translateY(.35em) rotate(-4deg);clip-path:inset(-30% 100% -30% -30%)}to{opacity:1;transform:none;clip-path:inset(-30% -30% -30% -30%)}}
.bio{margin:var(--s8) 0 var(--s4);font-size:clamp(17px,2vw,19px);line-height:1.65;max-width:56ch}
.bio b{font-weight:600}
.meta{margin:0;font-size:14.5px;color:var(--muted);display:flex;flex-wrap:wrap;gap:var(--s2) var(--s4)}
.meta a{color:var(--muted)}.meta a:hover{color:var(--ink)}
.tabs{display:flex;gap:var(--s6);margin:var(--s12) 0 var(--s6);padding-bottom:var(--s1);overflow-x:auto;scrollbar-width:none;white-space:nowrap}
.tabs::-webkit-scrollbar{display:none}
.tabs button{all:unset;cursor:pointer;font:400 14.5px var(--body);color:var(--muted);padding:6px 0;border-bottom:1.5px solid transparent;transition:color .2s}
.tabs button:hover{color:var(--ink)}
.tabs button[aria-selected="true"]{color:var(--ink);border-bottom-color:var(--ink)}
.tabs button:focus-visible{outline:2px solid var(--accent);outline-offset:4px}
.panel{display:none;animation:phin .35s ease both}
.panel.on{display:block}
.item{border-bottom:1px solid var(--line)}
.item summary{list-style:none;cursor:pointer;display:grid;grid-template-columns:1fr auto;gap:2px var(--s4);padding:var(--s4) 0;align-items:baseline}
.item summary::-webkit-details-marker{display:none}
.item .t{font:400 17px var(--body);grid-column:1}
.item .s{grid-column:2;grid-row:1;font-size:13px;color:var(--muted)}
.item .d{grid-column:1 / -1;font-size:14.5px;color:var(--muted);line-height:1.5;padding-right:var(--s8)}
.item .plus{position:absolute}
.item summary{position:relative}
.item summary:hover .t{color:var(--accent)}
.item .plus{right:0;top:var(--s4);width:14px;height:14px;display:none}
.item .body{padding:var(--s2) 0 var(--s8)}
.item[open] .t{color:var(--accent)}
.item[open] .d{display:none}
.item .statement{font-size:clamp(22px,3vw,28px);margin:var(--s2) 0 var(--s3)}
.item .after{margin-bottom:var(--s6)}
.item .cols3{grid-template-columns:1fr;gap:var(--s6)}
.item .cols3[style]{max-width:none!important}
.item .kind{margin:0 0 var(--s3);font-size:14.5px;color:var(--muted)}
.item .lead{font-size:17.5px;line-height:1.55;margin:0}
.item dl.terms{margin-top:var(--s8)}
.item dl.terms>div{grid-template-columns:1fr;gap:var(--s1)}
.item dl.terms dt{font:600 15px var(--body)}
.item dl.terms dd{font-size:15.5px}
.item .gal-head{margin:var(--s8) 0 var(--s3)}
.item .gallery figure{flex-basis:92%}
.item .links{margin-top:var(--s4)}
.box{padding:var(--s6)}
.aboutbody .statement{font-size:clamp(24px,3.4vw,32px)}
.skills{grid-template-columns:1fr 1fr}
@media (max-width:520px){.skills{grid-template-columns:1fr}}
.timeline li{grid-template-columns:120px minmax(0,1fr)}
.foot{margin:var(--s24) 0 var(--s12);padding-top:var(--s8);border-top:1px solid var(--line);display:flex;flex-wrap:wrap;gap:var(--s3) var(--s6);justify-content:space-between;align-items:baseline;font-size:14px;color:var(--muted)}
.foot .say{font:400 24px/1.15 var(--display);color:var(--ink);width:100%}
.foot .say em{color:var(--hand)}
.foot a{color:var(--muted)}.foot a:hover{color:var(--ink)}
@media (prefers-reduced-motion:reduce){.hand span,.panel{animation:none!important}}
'''
html=f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Mizuho Li, Product Manager</title>
<meta name="description" content="Mizuho Li is a product manager in San Francisco who builds 0-to-1 AI products.">
{fonts}
<script>document.documentElement.className+=' js'</script>
<style>
{root}
*{{box-sizing:border-box}}
html{{scrollbar-color:var(--line) var(--paper)}}
body{{margin:0;background:var(--paper);color:var(--ink);font-family:var(--body);line-height:1.62;caret-color:var(--accent);accent-color:var(--accent);font-variant-numeric:tabular-nums}}
::selection{{background:var(--accent);color:var(--paper)}}
a{{color:inherit;text-decoration-line:underline;text-decoration-color:var(--line);text-decoration-thickness:1px;text-underline-offset:4px}}
a:hover{{color:var(--accent);text-decoration-color:var(--accent)}}
:focus-visible{{outline:2px solid var(--accent);outline-offset:3px}}
h1,h2,h3{{font-family:var(--display);font-weight:400;line-height:1;margin:0}}
p{{margin:0 0 1em;text-wrap:pretty}}
.muted{{color:var(--muted)}}
@keyframes phin{{from{{opacity:0;transform:translateY(6px)}}to{{opacity:1;transform:none}}}}
{btn}
{mid}
{css}
</style>
</head>
<body>
<main class="col" id="top">
  <div class="top">
    <div class="head">
    <h1 class="is">mizuho is <span class="hand" id="hand" aria-live="off"><span>building</span></span></h1>
    <div class="meWrap">{art}</div>
    </div>
    <p class="bio">I'm a product manager at <b>Xbox Media Solutions</b> in <b>San Francisco</b>, working on ad products and the tools behind them. I build 0-to-1 AI products, and on the side I build my own solutions to my own pain points. When I'm not working, I'm usually playing tennis, snowboarding, cooking, traveling, or trying lots of yummy food.</p>
    <div class="cta"><a class="btn primary" href="mailto:mizuholi.ml@gmail.com">Email me</a><a class="btn" href="#" data-resume>Resume &darr;</a><span class="open"><i></i>open to new roles</span><span class="meta"><a href="https://www.linkedin.com/in/mizuho-li">linkedin</a><a href="https://github.com/limiz6383">github</a></span></div>
  </div>

  <div class="tabs" role="tablist" aria-label="Sections">
    <button role="tab" id="t-work" aria-controls="work" aria-selected="true" data-tab="work">work</button>
    <button role="tab" id="t-builds" aria-controls="builds" aria-selected="false" data-tab="builds">builds</button>
    <button role="tab" id="t-fit" aria-controls="fit" aria-selected="false" data-tab="fit">check my fit</button>
    <button role="tab" id="t-ask" aria-controls="ask" aria-selected="false" data-tab="ask">ask me</button>
    <button role="tab" id="t-about" aria-controls="about" aria-selected="false" data-tab="about">about</button>
  </div>

  <section class="panel on" id="work" role="tabpanel" aria-labelledby="t-work">{work_html}</section>
  <section class="panel" id="builds" role="tabpanel" aria-labelledby="t-builds">{build_html}</section>
  <section class="panel" id="about" role="tabpanel" aria-labelledby="t-about">{about}</section>
  <section class="panel" id="ask" role="tabpanel" aria-labelledby="t-ask">{box_ask}
    </div></section>
  <section class="panel" id="fit" role="tabpanel" aria-labelledby="t-fit">{box_fit}
    </div></section>

  <div class="foot"><p class="say">Let's build something that <em>makes people smile.</em></p><a class="mail" href="mailto:mizuholi.ml@gmail.com">mizuholi.ml@gmail.com</a></div>
</main>
{illus.FILTER}
<script>
/* tabs */
(function(){{
  const tabs=[...document.querySelectorAll('[data-tab]')], panels=[...document.querySelectorAll('.panel')];
  function show(id,push){{
    if(!panels.some(p=>p.id===id))id='work';
    panels.forEach(p=>p.classList.toggle('on',p.id===id));
    tabs.forEach(t=>t.setAttribute('aria-selected',String(t.dataset.tab===id)));
    if(push)history.replaceState(null,'','#'+id);
  }}
  tabs.forEach(t=>t.addEventListener('click',()=>show(t.dataset.tab,true)));
  addEventListener('hashchange',()=>show(location.hash.slice(1),false));
  show(location.hash.slice(1)||'work',false);
  /* handwritten word */
  const words=['building','shipping','prototyping','learning'], el=document.getElementById('hand');
  if(el&&!matchMedia('(prefers-reduced-motion: reduce)').matches){{let i=0;setInterval(()=>{{i=(i+1)%words.length;el.innerHTML='<span>'+words[i]+'</span>'}},2800)}}
}})();
{js}
{illus.JS}
</script>
</body>
</html>
'''

import re as _re
_MAP={'13.5':'13','14':'14.5','15':'15.5','16':'16.5','17':'16.5','17.5':'16.5','26':'28'}
def _fs(m):
    return m.group(1)+_MAP.get(m.group(2),m.group(2))+'px'
_a=0; _b=html.index('</head>')
_css=html[_a:_b]
_css=_re.sub(r'(font-size:)(\d+(?:\.\d+)?)px',_fs,_css)
_css=_re.sub(r'(font:\d+ )(\d+(?:\.\d+)?)px',lambda m:m.group(1)+_MAP.get(m.group(2),m.group(2))+'px',_css)
_css=_css.replace('font:700 13px','font:600 13px')
_css=_css.replace("'Instrument Sans'","'Hanken Grotesk'").replace("'Instrument Serif'","'Newsreader'")
_css=_css.replace('clamp(50px,11vw,76px)','clamp(46px,10.4vw,70px)').replace('clamp(26px,3vw,38px)','clamp(25px,2.8vw,34px)').replace('font-size:26px;line-height:1.25','font-size:23px;line-height:1.3').replace('font-size:28px;line-height:1.22','font-size:26px;line-height:1.25')
_css=_css.replace('.hand{font:600 1.18em','.hand{font:600 1.3em')
_css+=''

_css=_css.replace('border-color:var(--accent);color:#fff}','border-color:var(--accent);color:var(--paper)}')
_css=_css.replace('font-size:clamp(26px,3vw,38px);line-height:1.16','font-size:clamp(26px,3vw,38px);line-height:1.25').replace('font-size:24px;line-height:1.15','font-size:26px;line-height:1.25').replace('font-size:28px;line-height:1.1;','font-size:28px;line-height:1.22;')
for _n,_i in (('fit','fit'),('ask','ask'),('about','about')):
    _m=re.search(r'<section class="panel"[^>]*id="'+_i+'"[^>]*>',html); html=html[:_m.end()]+illus.page(_n)+html[_m.end():]
html=html.replace('<h4>','<h4 aria-level="2">')
html=html.replace('building AI-core products','building AI&#8209;core products')
_w0=html.index('id="work"'); _w1=html.index('id="builds"',_w0)
_wk=html[_w0:_w1]
_wk=_re.sub(r'(<span class="d">)(.*?)(</span>)',lambda m:m.group(1)+_re.sub(r'(~?\d[\d,.]*%?\+?(?: hours| minutes)?)',r'<span class="num">\1</span>',m.group(2))+m.group(3),_wk)
html=html[:_w0]+_wk+html[_w1:]

_sk0=html.index('class="skills"'); _sk1=html.index('</div>\n      <ul class="timeline">',_sk0)
_sk=html[_sk0:_sk1]
_sk=_re.sub(r'<p>(.*?)</p>',lambda m:'<ul class="tags">'+''.join(f'<li>{x.strip()}</li>' for x in m.group(1).split(','))+'</ul>',_sk)
html=html[:_sk0]+_sk+html[_sk1:]
_css=_css[:_css.rindex('</style>')]+'.tabs-wide{}@media (min-width:900px){.col{max-width:980px;margin:0 auto;padding:0 40px}.top{padding-top:var(--s16)}h1.is{font-size:clamp(58px,5.6vw,80px)}.meWrap{width:clamp(170px,15vw,220px)}.bio{font-size:20px;max-width:none;line-height:1.55}.item .t{font-size:18.5px}#work .item .d{font-size:clamp(21px,1.7vw,25px)}.item .body p,.item .body li{max-width:70ch}.bio{max-width:70ch}.meWrap{margin-right:12px}.top{padding-top:clamp(32px,6vh,72px)}.col>.tabs{margin-top:56px}.answer,.answer *{max-width:68ch}.statement{text-wrap:balance}}.statement{text-wrap:balance}#work .item .d{font:500 21px/1.3 var(--display);color:var(--ink);letter-spacing:-.005em;padding-top:2px}#work .item .d .num{color:var(--accent)}.cta{display:flex;flex-wrap:wrap;align-items:center;gap:10px 12px;margin:var(--s6) 0 var(--s2)}.cta .btn{padding:11px 18px}.open{display:inline-flex;align-items:center;gap:8px;color:var(--muted);font-size:14.5px;margin-left:4px}.open i{width:8px;height:8px;border-radius:50%;background:#7BD88F;box-shadow:0 0 0 0 rgba(123,216,143,.6);animation:pulse 2.4s ease-out infinite}@keyframes pulse{70%{box-shadow:0 0 0 8px rgba(123,216,143,0)}100%{box-shadow:0 0 0 0 rgba(123,216,143,0)}}@media (prefers-reduced-motion:reduce){.open i{animation:none}}.item .d{font-size:15.5px;color:#CFCBBE}@media (max-width:700px){.tabs button{padding:13px 0}.meta{row-gap:0;align-items:center}.meta span,.meta a{display:inline-block;padding:11px 0}.chip{min-height:44px}.foot a{display:inline-block;padding:13px 3px}}h1.is{flex-direction:column;align-items:flex-start;flex-wrap:nowrap;gap:0}h1.is .hand{margin-top:-.04em}.cta{align-items:center}.cta .meta{margin-left:var(--s2)}.item:last-child{border-bottom:0}.foot{margin:var(--s24) 0 var(--s12);padding-top:0;border-top:0;flex-direction:column;align-items:center;text-align:center;gap:var(--s4)}.foot::before{content:"";width:28px;height:1px;background:var(--hand);opacity:.6;margin-bottom:var(--s8)}.foot .say{width:auto;font-size:clamp(24px,5.5vw,30px)}.foot>span{justify-content:center}.foot .mail{font-size:17px;color:var(--ink);text-decoration:underline;text-decoration-color:var(--line);text-underline-offset:5px;padding:12px 4px}.foot .mail:hover{text-decoration-color:var(--accent)}.tabs button{font-size:15.5px;color:#C9C5B8;padding:13px 0}.tabs button[aria-selected="true"]{color:var(--ink)}@media (max-width:700px){.tabs{gap:20px}}#builds .item summary{padding-right:var(--s8)}#builds .item .plus{display:block;right:2px;top:calc(var(--s4) + 6px);width:14px;height:14px}#builds .item .plus::before,#builds .item .plus::after{content:"";position:absolute;left:0;right:0;top:6px;height:1.5px;background:var(--muted);transition:transform .25s cubic-bezier(.2,.8,.2,1),background-color .2s}#builds .item .plus::after{transform:rotate(90deg)}#builds .item[open] .plus::after{transform:rotate(0)}#builds .item summary:hover .plus::before,#builds .item summary:hover .plus::after{background:var(--accent)}.answer .q{color:var(--ink)}.box{border-color:var(--line)}.answer,.answer *{max-width:none}.answer{max-width:none}@media (min-width:900px){.top .head{font-size:20px;max-width:70ch}.meWrap{width:clamp(170px,15vw,220px)}}@media (max-width:359px){h1.is{font-size:33px;white-space:nowrap}.meWrap{width:96px}}#builds .item summary{grid-template-columns:1fr auto;column-gap:var(--s4)}#builds .item .thumb{grid-column:2;grid-row:1 / span 2;margin-right:34px;align-self:center;width:210px}#builds .item .d{grid-column:1;padding-right:0}.thumb{display:block;border:1px solid var(--line);background:#161513;color:var(--ink);padding:6px}.thumb svg{display:block;width:100%;height:auto;overflow:visible}.item[open] .thumb{display:none}.thumb .trail{stroke-dashoffset:0}.thumb .plane{offset-path:path("M16 80C40 82 44 44 72 46S116 84 142 32");offset-rotate:auto;offset-distance:0%;transform-box:fill-box}.item summary:hover .thumb .plane,.item summary:focus-visible .thumb .plane{animation:fly 2.2s cubic-bezier(.45,.05,.3,1) forwards}.item summary:hover .thumb .trail{animation:flow 1.2s linear infinite}@keyframes fly{to{offset-distance:100%}}@keyframes flow{to{stroke-dashoffset:-14}}.thumb .pin{transform-box:fill-box;transform-origin:50% 100%}.item summary:hover .thumb .pin{animation:bob .9s ease-in-out infinite}@keyframes bob{50%{transform:translateY(-3px)}}.thumb .now{offset-path:path("M12 66C30 24 58 24 76 60S122 100 148 46");offset-distance:46.8%;transition:none}.item summary:hover .thumb .now{animation:slide 2.4s ease-in-out infinite alternate}@keyframes slide{from{offset-distance:46.8%}to{offset-distance:92%}}.thumb .tick{stroke-dasharray:12;stroke-dashoffset:0}.item summary:hover .thumb .tick{animation:draw .6s ease-out}@keyframes draw{from{stroke-dashoffset:12}to{stroke-dashoffset:0}}.thumb .line{stroke-dasharray:140;stroke-dashoffset:0}.item summary:hover .thumb .line{animation:draw2 1.1s ease-out}@keyframes draw2{from{stroke-dashoffset:140}to{stroke-dashoffset:0}}.thumb .t1,.thumb .t2,.thumb .t3{stroke-dasharray:10;stroke-dashoffset:0}.item summary:hover .thumb .t1{animation:draw3 .5s .3s backwards}.item summary:hover .thumb .t2{animation:draw3 .5s .6s backwards}.item summary:hover .thumb .t3{animation:draw3 .5s .9s backwards}@keyframes draw3{from{stroke-dashoffset:10}to{stroke-dashoffset:0}}.item summary:hover .thumb .end{animation:ping 1.1s ease-out}@keyframes ping{50%{r:7}}@media (prefers-reduced-motion:reduce){.thumb *{animation:none!important}}@media (max-width:620px){#builds .item .thumb{grid-column:1 / -1;grid-row:2;width:calc(100% + 32px);margin:6px 0 4px;height:124px;overflow:hidden}#builds .item .thumb svg{height:100%;width:auto;margin:0 auto}#builds .item .d{grid-row:3;grid-column:1 / -1}}.tags{list-style:none;margin:var(--s2) 0 0;padding:0;display:flex;flex-wrap:wrap;gap:6px}.tags li{font-size:13.5px;line-height:1;padding:7px 10px;border:1px solid var(--line);color:#CFCBBE;background:transparent}.skills .tags li:hover{border-color:var(--muted)}'+illus.CSS+''+illus.THUMBCSS+illus.PAGECSS+'b,strong{font-weight:600}h4{font:600 13px var(--body);letter-spacing:.02em}'+_css[_css.rindex('</style>'):]
html=html[:_a]+_css+html[_b:]
open('/home/claude/portfolio/src_v3.html','w').write(html)
print(len(html))
