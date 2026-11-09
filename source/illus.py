# Simple line illustrations that explain how each project works.
ICONS = {
 'cal': '<rect x="6" y="12" width="48" height="44" rx="6"/><path d="M18 6v12M42 6v12M6 26h48"/><path d="M30 33c0 0-8 9-8 14a8 8 0 0 0 16 0c0-5-8-14-8-14z"/>',
 'phase': '<rect x="4" y="14" width="56" height="38" rx="6"/><path d="M19 22c0 0-6 7-6 10.5a6 6 0 0 0 12 0c0-3.5-6-10.5-6-10.5z"/><path d="M33 26h20M33 36h14"/>',
 'shield': '<path d="M32 5L54 13V30C54 44 44 54 32 60C20 54 10 44 10 30V13Z"/><path d="M21 31l8 8 14-16"/>',
 'bowl': '<path d="M6 34h52c0 14-11 23-26 23S6 48 6 34z"/><path d="M20 34c-2-10 4-18 13-20 2 10-3 18-13 20z"/><path d="M36 34c0-8 6-14 15-14 0 8-6 14-15 14z"/><path d="M24 30l7-9M40 30l6-6"/>',
 'sliders': '<path d="M6 18h52M6 32h52M6 46h52"/><circle cx="20" cy="18" r="5.5" class="fill"/><circle cx="43" cy="32" r="5.5" class="fill"/><circle cx="29" cy="46" r="5.5" class="fill"/>',
 'ticket': '<rect x="4" y="14" width="38" height="28" rx="4"/><path d="M24 14v28" stroke-dasharray="3 4"/><path d="M10 24h8M10 32h6"/><rect x="38" y="36" width="22" height="18" rx="3" class="fill"/><path d="M43 36v-5a6 6 0 0 1 12 0v5"/>',
 'chat': '<path d="M8 10h48a4 4 0 0 1 4 4v24a4 4 0 0 1-4 4H30L20 52V42H8a4 4 0 0 1-4-4V14a4 4 0 0 1 4-4z"/><circle cx="20" cy="26" r="2" class="dotf"/><circle cx="32" cy="26" r="2" class="dotf"/><circle cx="44" cy="26" r="2" class="dotf"/>',
 'apply': '<rect x="6" y="18" width="52" height="28" rx="14"/><path d="M22 32l7 7 13-14"/>',
 'bank': '<path d="M6 24L32 8l26 16z"/><path d="M10 56h44M14 28v24M26 28v24M38 28v24M50 28v24"/>',
 'chart': '<path d="M8 6v48h50"/><path d="M14 44l12-12 10 6 18-22"/><circle cx="54" cy="16" r="4.5" class="fill"/>',
 'globe': '<circle cx="32" cy="32" r="24"/><ellipse cx="32" cy="32" rx="10" ry="24"/><path d="M8 32h48M13 19h38M13 45h38"/>',
 'list': '<rect x="6" y="8" width="13" height="13" rx="2.5"/><rect x="6" y="26" width="13" height="13" rx="2.5"/><rect x="6" y="44" width="13" height="13" rx="2.5"/><path d="M9 14l3 3 5-6M9 32l3 3 5-6M9 50l3 3 5-6M28 14h30M28 32h26M28 50h28"/>',
}
FLOWS = {
 'Trip Planner': [
  ('sliders','Your travel','style','Learns your budget, group size and travel style, so the first plan already looks like yours.'),
  ('ticket','Bookings','stay put','Flights, shows and reservations lock in, and the rest of the day is built around them.'),
  ('chat','Chat to','change it','Talk any part of the trip through with the AI, at every step.'),
  ('apply','Press Apply,','get a new version','Nothing changes until you apply, and every apply makes a version you can review.'),
 ],
 'Cycle Insights': [
  ('cal','Where you are','in your cycle','Reads your Oura data against your own baseline and your cycle stage.'),
  ('phase','One short','insight','Turns it into a brief, hedged note for that phase, with at most one action.'),
  ('shield','Research-backed,','safety-checked','Every claim traces to a research source, and a second model reviews each draft before it goes out.'),
  ('bowl','Simple nutrition','for your stage','Ends with practical food guidance to nourish your hormones, never numeric targets.'),
 ],
 'Fintracker': [
  ('bank','Connect your','accounts','Links your bank and brokerage read-only, and the data stays on your machine.'),
  ('chart','Net worth and','spending','Rolls everything up into one net worth and sorts where the money goes.'),
  ('globe','Economic and','political context','Weighs the wider picture against your own financial goals.'),
  ('list','Next steps,','with reasons','Ends in an ordered list of what to do next, each step showing its reasoning.'),
 ],
}
def _arrow(x1,y1,x2,y2,bend,i):
    mx,my=(x1+x2)/2,(y1+y2)/2
    cx,cy=(mx,my-bend) if abs(x2-x1)>abs(y2-y1) else (mx+bend,my)
    # arrowhead direction from control point to end
    import math
    ang=math.atan2(y2-cy,x2-cx); L=9
    a1=(x2-L*math.cos(ang-0.5),y2-L*math.sin(ang-0.5)); a2=(x2-L*math.cos(ang+0.5),y2-L*math.sin(ang+0.5))
    return (f'<g class="arrow" style="--i:{i}"><path pathLength="1" d="M{x1:.1f} {y1:.1f}Q{cx:.1f} {cy:.1f} {x2:.1f} {y2:.1f}"/>'
            f'<path class="head" d="M{a1[0]:.1f} {a1[1]:.1f}L{x2:.1f} {y2:.1f}L{a2[0]:.1f} {a2[1]:.1f}"/></g>')
def build(title):
    nodes=FLOWS[title]
    # horizontal
    H=['<svg class="hz" viewBox="0 0 740 164" role="presentation" focusable="false">']
    for i,(ic,l1,l2,cap) in enumerate(nodes):
        x=i*190
        H.append(f'<g class="nd" data-i="{i}" data-cap="{cap}" tabindex="0" role="button" aria-label="{l1} {l2}. {cap}" style="--i:{i}"><rect class="hit" x="{x-8}" y="0" width="186" height="164" fill="transparent" stroke="none"/><g class="ic" transform="translate({x-7.5},14) scale(1.25)" filter="url(#rough)">{ICONS[ic]}</g><text x="{x}" y="118">{l1}</text><text x="{x}" y="139">{l2}</text></g>')
        if i<len(nodes)-1: H.append(_arrow(x+88,56,x+190-12,56,16,i))
    H.append('</svg>')
    # vertical
    V=['<svg class="vt" viewBox="0 0 320 456" role="presentation" focusable="false">']
    for i,(ic,l1,l2,cap) in enumerate(nodes):
        cy=56+i*114
        V.append(f'<g class="nd" data-i="{i}" data-cap="{cap}" tabindex="0" role="button" aria-label="{l1} {l2}. {cap}" style="--i:{i}"><rect class="hit" x="0" y="{cy-52}" width="320" height="104" fill="transparent" stroke="none"/><g class="ic" transform="translate(-5,{cy-32})" filter="url(#rough)">{ICONS[ic]}</g><text x="76" y="{cy-3}">{l1}</text><text x="76" y="{cy+19}">{l2}</text></g>')
        if i<len(nodes)-1: V.append(_arrow(27,cy+40,27,cy+114-40,-12,i))
    V.append('</svg>')
    return ('<figure class="how" data-how><div class="how-art">'+''.join(H)+''.join(V)+'</div>'
            f'<figcaption class="cap" aria-live="polite">{nodes[0][3]}</figcaption></figure>')
FILTER='<svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false"><filter id="rough" x="-5%" y="-5%" width="110%" height="110%"><feTurbulence type="fractalNoise" baseFrequency="0.018" numOctaves="1" seed="4" result="n"/><feDisplacementMap in="SourceGraphic" in2="n" scale="2.2"/></filter><filter id="rough2" x="-5%" y="-5%" width="110%" height="110%"><feTurbulence type="fractalNoise" baseFrequency="0.026" numOctaves="1" seed="11" result="n"/><feDisplacementMap in="SourceGraphic" in2="n" scale="2.8"/></filter></svg>'
CSS=('.how{margin:var(--s2) 0 var(--s8)}.how-art svg{display:block;width:100%;height:auto;overflow:visible;color:var(--ink)}.how-art .vt{display:none;max-width:340px}'
'.how .nd{cursor:pointer}.how .nd:focus-visible{outline:2px solid var(--accent);outline-offset:3px;border-radius:6px}.how .nd .ic{fill:none;stroke:currentColor;stroke-width:2;stroke-linecap:round;stroke-linejoin:round;transition:stroke .25s,transform .35s cubic-bezier(.2,.8,.2,1)}'
'.how .nd .fill{fill:var(--ifill)}.how .nd .dotf{fill:currentColor;stroke:none}'
'.how .nd text{font:500 14.5px var(--body);fill:var(--ink);transition:fill .25s}.how .nd text:first-of-type{fill:var(--muted)}'
'.how .nd.on .ic,.how .nd:focus-visible .ic{stroke:var(--hand)}.how .nd.on text,.how .nd:focus-visible text{fill:var(--handtx)}'
'.how .nd:hover .ic{stroke:var(--hand)}.how .nd:hover text{fill:var(--hand)}'
'.how .arrow path{fill:none;stroke:var(--muted);stroke-width:1.6;stroke-linecap:round;stroke-linejoin:round;filter:url(#rough)}'
'.how .cap{margin-top:var(--s4);min-height:3.2em;max-width:60ch;font:500 18px/1.35 var(--display);color:var(--ink)}'
'.item[open] .how .nd{animation:pop .55s cubic-bezier(.2,.8,.2,1) backwards;animation-delay:calc(var(--i)*.22s)}'
'.item[open] .how .arrow path:first-child{stroke-dasharray:1;stroke-dashoffset:0;animation:drawA .5s ease-out backwards;animation-delay:calc(var(--i)*.22s + .18s)}'
'.item[open] .how .arrow .head{animation:fadeA .3s ease-out backwards;animation-delay:calc(var(--i)*.22s + .55s)}'
'@keyframes pop{from{opacity:0;transform:translateY(8px)}}@keyframes drawA{from{stroke-dashoffset:1}}@keyframes fadeA{from{opacity:0}}'
'@media (max-width:620px){.how-art .hz{display:none}.how-art .vt{display:block}.how .cap{font-size:17px}}'
'@media (prefers-reduced-motion:reduce){.item[open] .how *{animation:none!important}}')
JS='''
(function(){
  const reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
  document.querySelectorAll('figure[data-how]').forEach(fig=>{
    const cap=fig.querySelector('.cap'); const det=fig.closest('details'); let timer=null,stopped=false;
    const nodes=i=>fig.querySelectorAll('.nd[data-i="'+i+'"]');
    function set(i,user){
      fig.querySelectorAll('.nd').forEach(n=>n.classList.toggle('on',+n.dataset.i===i));
      const n=nodes(i)[0]; if(n)cap.textContent=n.dataset.cap; if(user)stopAuto();
    }
    function stopAuto(){stopped=true;clearInterval(timer)}
    function auto(){ stopped=false; let i=0; set(0); clearInterval(timer);
      if(reduce)return; timer=setInterval(()=>{ if(stopped||!det.open){clearInterval(timer);return} i++; if(i>3){clearInterval(timer);set(0);return} set(i); },2600); }
    fig.querySelectorAll('.nd').forEach(n=>{
      const i=+n.dataset.i;
      n.addEventListener('pointerenter',()=>set(i,true));
      n.addEventListener('focus',()=>set(i,true));
      n.addEventListener('click',()=>set(i,true));
      n.addEventListener('keydown',e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();set(i,true)}});
    });
    if(det)det.addEventListener('toggle',()=>{ if(det.open)auto(); else stopAuto(); });
  });
})();
'''

_SC={
'Trip Planner':(
 '<path d="M14 10h42a4 4 0 0 1 4 4v14a4 4 0 0 1-4 4H34l-9 8v-8H14a4 4 0 0 1-4-4V14a4 4 0 0 1 4-4z"/>'
 '<circle cx="23" cy="21" r="1.6" class="dotf"/><circle cx="35" cy="21" r="1.6" class="dotf"/><circle cx="47" cy="21" r="1.6" class="dotf"/>'
 '<rect x="16" y="64" width="54" height="40" rx="6"/><path d="M33 64v-7a4 4 0 0 1 4-4h12a4 4 0 0 1 4 4v7M30 64v40M56 64v40"/>'
 '<path d="M120 62C108 48 102 40 102 31a18 18 0 0 1 36 0c0 9-6 17-18 31z"/><circle cx="120" cy="31" r="6" class="fill"/>',
 '<path class="trail" d="M76 84C104 96 134 88 122 70"/><path class="trail" d="M118 76l4-7 7 4"/>'),
'Cycle Insights':(
 '<circle cx="24" cy="24" r="11"/><circle cx="60" cy="24" r="11"/><path class="fill" d="M60 13a11 11 0 0 0 0 22z"/>'
 '<circle cx="96" cy="24" r="11" class="solid"/><circle cx="132" cy="24" r="11"/><path class="fill" d="M132 13a11 11 0 0 1 0 22z"/>'
 '<path d="M40 24h8M76 24h8M112 24h8" stroke-dasharray="2 4"/>'
 '<path d="M44 66h72c0 20-15 34-36 34S44 86 44 66z"/><path d="M62 66c-3-13 4-21 15-23 3 12-3 20-15 23zM88 66c0-9 6-16 17-16 0 9-6 16-17 16z"/>'
 '<path d="M132 70v12M126 76h12M26 82v8M22 86h8"/>',
 '<path class="trail" d="M62 66c-3-13 4-21 15-23 3 12-3 20-15 23z"/><circle class="acc" cx="96" cy="24" r="11"/>'),
'Fintracker':(
 '<path d="M12 10v94h138"/><rect x="26" y="78" width="18" height="26"/><rect x="56" y="64" width="18" height="40"/><rect x="86" y="48" width="18" height="56"/>'
 '<ellipse cx="132" cy="96" rx="13" ry="4.5"/><path d="M119 96v-9M145 96v-9"/><ellipse cx="132" cy="87" rx="13" ry="4.5"/><path d="M119 87v-9M145 87v-9"/><ellipse cx="132" cy="78" rx="13" ry="4.5" class="fill"/>'
 '<circle cx="134" cy="30" r="12"/><path d="M128 24l12 12M128 36l12-12" opacity="0"/><circle cx="134" cy="30" r="5"/>',
 '<path class="trail" d="M20 62L52 46l24 8 38-30"/><path class="trail" d="M102 22l13 1-1 13"/>'),
}
import json,os
_VB=json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'vb.json'))) if os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)),'vb.json')) else {}
def _off(key,W,H,center=True,pad=2):
    b=_VB.get(key)
    if not b: return 0,0
    x,y,w,h=b
    return ((W-w)/2-x if center else pad-x), ((H-h)/2-y if center else pad-y)
def thumb(title):
    base,acc=_SC[title]; dx,dy=_off('t:'+title,160,116)
    return f'<svg viewBox="0 0 160 116" role="presentation" focusable="false"><g transform="translate({dx:.1f},{dy:.1f})"><g class="sc pen" filter="url(#rough2)" transform="translate(.9,.7) rotate(-.7 80 58)">{base}</g><g class="sc" filter="url(#rough)">{base}</g><g class="sa" filter="url(#rough)">{acc}</g></g></svg>'
THUMBCSS=('.thumb{border:0!important;background:transparent!important}.thumb svg{color:var(--ink)}.thumb .sc,.thumb .sa{fill:none;stroke:currentColor;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round}'
'.thumb .sc.pen,.pgart .sc.pen{stroke-width:1;opacity:.5}.thumb .sc.pen .fill,.thumb .sc.pen .solid,.thumb .sc.pen .dotf,.pgart .sc.pen .dotf{fill:none}.thumb .sc .fill{fill:var(--ifill)}.thumb .sc .dotf{fill:currentColor;stroke:none}.thumb .sc .solid{fill:currentColor}'
'.thumb .sc .tooth{stroke-width:5}.thumb .sa{stroke:var(--hand)}.thumb .sa .trail{stroke-dasharray:none}.thumb .sa .acc{fill:none}'
'.item summary:hover .thumb .sa .trail,.item summary:focus-visible .thumb .sa .trail{animation:drawT 1.1s ease-out}'
'@keyframes drawT{from{stroke-dasharray:200;stroke-dashoffset:200}to{stroke-dasharray:200;stroke-dashoffset:0}}'
'@media (prefers-reduced-motion:reduce){.thumb .sa *{animation:none!important}}')

_SC['Agentic Creative Platform']=(
 '<circle cx="34" cy="50" r="26"/><path d="M34 50V32M34 50l13 8"/>'
 '<rect x="98" y="20" width="54" height="72" rx="5"/><circle cx="116" cy="42" r="7"/><path d="M98 86l18-20 12 12 8-8 16 14"/>',
 '<path d="M66 56h22M88 56l-6-5M88 56l-6 5"/><path d="M142 6v10M137 11h10M88 100v8M84 104h8"/>')
_SC['Ad Quality']=(
 '<rect x="12" y="14" width="68" height="88" rx="5"/><circle cx="34" cy="38" r="7"/><path d="M12 92l22-26 14 14 10-10 22 22"/>'
 '<path d="M126 20L150 29V56C150 72 140 82 126 88 112 82 102 72 102 56V29Z"/><path d="M114 54l9 9 15-18"/>',
 '<circle cx="46" cy="58" r="36"/><path d="M20 84L72 32"/>')
_SC['Publisher Tooling']=(
 '<rect x="14" y="14" width="20" height="20" rx="3"/><rect x="14" y="48" width="20" height="20" rx="3"/><rect x="14" y="82" width="20" height="20" rx="3"/>'
 '<path d="M46 24h46M46 58h38M46 92h42"/><circle cx="130" cy="58" r="14"/><circle cx="130" cy="58" r="5"/>'
 '<path class="tooth" d="M130 36v6M130 74v6M108 58h6M146 58h6M114 42l4 4M142 70l-4-4M146 42l-4 4M114 74l4-4"/>',
 '<path d="M18 24l5 5 9-10M18 58l5 5 9-10M18 92l5 5 9-10"/>')

_PG={
 'fit':('0 0 300 110',
  '<rect x="8" y="10" width="50" height="90" rx="4"/><path d="M18 30h30M18 44h30M18 58h22M18 72h28"/>'
  '<circle cx="126" cy="55" r="30"/><circle cx="174" cy="55" r="30"/>'
  '<rect x="242" y="10" width="50" height="90" rx="4"/><path d="M252 30h30M252 44h24M252 58h30M252 72h18"/>',
  '<path d="M138 55l9 9 17-19"/><path d="M66 55h20M86 55l-5-4M86 55l-5 4M234 55h-20M214 55l5-4M214 55l5 4"/>'),
 'ask':('0 0 300 110',
  '<path d="M12 10h96a5 5 0 0 1 5 5v44a5 5 0 0 1-5 5H44l-14 14V64H12a5 5 0 0 1-5-5V15a5 5 0 0 1 5-5z"/>'
  '<path d="M178 40h104a5 5 0 0 1 5 5v44a5 5 0 0 1-5 5h-18v14l-14-14h-72a5 5 0 0 1-5-5V45a5 5 0 0 1 5-5z"/>'
  '<path d="M196 60h70M196 76h46"/><circle cx="60" cy="43" r="1.8" class="dotf"/>',
  '<path d="M48 22a12 12 0 1 1 14 12c-4 2-6 4-6 8"/><path d="M280 14v12M274 20h12M142 84v8M138 88h8"/>'),
 'about':('0 0 380 80',
  '<g transform="translate(0,6)"><g transform="rotate(-38 32 32)"><ellipse cx="32" cy="20" rx="14" ry="18"/><path d="M32 2v36M18 20h28"/><path d="M27 38l-2 9h14l-2-9"/><rect x="28" y="47" width="8" height="14" rx="3"/></g></g>'
  '<g transform="translate(86,6)"><path d="M4 58L32 8l28 50z"/><path d="M20 30l6 6 6-6 6 6 6-6"/></g>'
  '<g transform="translate(166,8)"><path d="M10 30h44v20a6 6 0 0 1-6 6H16a6 6 0 0 1-6-6z"/><path d="M6 30h52M2 38h8M54 38h8"/><path d="M22 22c-3-4 3-6 0-10M34 22c-3-4 3-6 0-10M46 22c-3-4 3-6 0-10"/></g>'
  '<g transform="translate(246,8)"><path d="M4 30L58 6 44 56 30 38z"/><path d="M30 38l28-32"/></g>'
  '<g transform="translate(318,8)"><path d="M4 34h52c0 14-11 22-26 22S4 48 4 34z"/><path d="M14 34c4-6 8-6 12 0s8 6 12 0M18 8l12 22M26 6l14 24"/></g>',
  '<circle cx="46" cy="6" r="6"/><path d="M42 3c3 1 5 4 5 8" stroke-width="1.6"/>'),
}
def page(name):
    vb,base,acc=_PG[name]; W,H=[float(v) for v in vb.split()[2:]]
    b=_VB.get('p:'+name)
    if b:
        x,y,w,h=b; pad=2.5; vb=f'0 0 {w+2*pad:.1f} {h+2*pad:.1f}'; dx,dy=pad-x,pad-y
    else: dx=dy=0
    return f'<div class="pgart pg-{name}" aria-hidden="true"><svg viewBox="{vb}" focusable="false"><g transform="translate({dx:.1f},{dy:.1f})"><g class="sc pen" filter="url(#rough2)" transform="translate(.9,.7) rotate(-.5 {W/2:.0f} {H/2:.0f})">{base}</g><g class="sc" filter="url(#rough)">{base}</g><g class="sa" filter="url(#rough)">{acc}</g></g></svg></div>'
PAGECSS=('.pgart.pg-fit,.pgart.pg-ask{display:flex;justify-content:center}.pgart{margin:0 0 var(--s8)}.pgart svg{display:block;width:100%;max-width:300px;height:auto;overflow:visible;color:var(--ink)}.pgart.pg-about svg{max-width:400px}'
'.pgart .sc,.pgart .sa{fill:none;stroke:currentColor;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round}.pgart .sa{stroke:var(--hand)}'
'.pgart .sc .dotf{fill:currentColor;stroke:none}'
'.panel.on .pgart .sa path{stroke-dasharray:200;animation:pgdraw 1.2s .15s ease-out backwards}@keyframes pgdraw{from{stroke-dashoffset:200}to{stroke-dashoffset:0}}'
'@media (prefers-reduced-motion:reduce){.pgart .sa path{animation:none!important}}'
'.panel#work .item summary,.panel#builds .item summary{grid-template-columns:1fr auto;grid-template-rows:min-content min-content 1fr;column-gap:var(--s4);row-gap:2px;align-items:start;align-content:start}'
'.panel#work .item .t,.panel#builds .item .t{grid-column:1;grid-row:1}'
'.panel#work .item .s,.panel#builds .item .s{grid-column:1;grid-row:2;font-size:13px;color:var(--muted)}'
'.panel#work .item .d,.panel#builds .item .d{grid-column:1;grid-row:3;font:400 14.5px/1.55 var(--body);color:var(--soft);letter-spacing:0;padding:4px 0 0}'
'.panel#work .item .d .num{color:var(--accent)}.panel#work .body p:not(.statement),.panel#work .body li{font-size:14.5px;line-height:1.62}.panel#work .body .after{color:var(--soft)}'
'.panel#work .item summary{padding-right:var(--s8)}.panel#work .item .plus{display:block;right:2px;top:calc(var(--s4) + 6px);width:14px;height:14px}'
'.panel#work .item .plus::before,.panel#work .item .plus::after{content:"";position:absolute;left:0;right:0;top:6px;height:1.5px;background:var(--muted);transition:transform .25s cubic-bezier(.2,.8,.2,1),background-color .2s}'
'.panel#work .item .plus::after{transform:rotate(90deg)}.panel#work .item[open] .plus::after{transform:rotate(0)}'
'.panel#work .item summary:hover .plus::before,.panel#work .item summary:hover .plus::after{background:var(--accent)}'
'.panel#work .item .thumb,.panel#builds .item .thumb{grid-column:2;grid-row:1 / 4;align-self:center;margin-right:34px;width:210px}'
'@media (max-width:620px){.panel#work .item .thumb,.panel#builds .item .thumb{grid-column:1 / -1;grid-row:3;width:calc(100% + 32px);margin:8px -16px 4px;height:124px;overflow:hidden}'
'.panel#work .item .thumb svg,.panel#builds .item .thumb svg{height:100%;width:auto;margin:0 auto}.panel#work .item .d,.panel#builds .item .d{grid-row:4;grid-column:1 / -1}}')


# ---- v5: redrawn, looser hand-drawn scenes (wobbly outlines, overshoots, hatching) ----
THUMBCSS+='.thumb .sc .hat{stroke-width:1.1;opacity:.85}.thumb .sc.pen .hat{opacity:.5}'
_SC['Agentic Creative Platform']=(
 '<path d="M34 27C48 26 60 38 59 52 58 66 47 78 33 77 19 76 9 65 10 51 11 38 21 28 34 27Z"/>'
 '<path d="M34 52L33 36M34 52L46 59"/><path d="M34 29v4M57 52h-4M34 75v-4M11 52h4"/>'
 '<path d="M20 29l-6-6M48 29l6-6M14 74l-5 8M54 74l5 8"/>'
 '<g class="hat"><path d="M41 71l13-13M46 74l11-11M36 74l15-15"/></g>'
 '<path d="M101 22L151 25 149 84 99 81 101 22Z"/><path d="M98 80l-2-2M152 24l3 1"/>'
 '<path d="M114 38c4-2 8 1 7 5-1 4-6 5-9 2-2-3-1-6 2-7z"/>'
 '<path d="M100 79L119 56 130 68 138 59 149 77"/>'
 '<g class="hat"><path d="M110 80l9-10M119 80l10-11M129 80l9-10M139 80l8-9"/></g>',
 '<path d="M66 52C74 47 83 57 92 51M86 45l7 6-6 6"/><path d="M146 8v11M140.5 13.5h11M88 92v9M83.5 96.5h9"/>')
_SC['Ad Quality']=(
 '<path d="M14 24L72 21 74 86 13 89 14 24Z"/><path d="M22 33c8-1 18-1 28-2"/>'
 '<path d="M20 80l15-19 10 12 8-8 11 13"/><path d="M28 47c3-2 7 0 6 3-1 3-5 3-7 1-1-1-1-3 1-4z"/>'
 '<g class="hat"><path d="M30 84l9-10M40 84l9-10M50 84l8-9"/></g>'
 '<path d="M127 18C135 24 143 26 151 27 151 46 148 66 127 88 106 70 103 47 104 28 113 27 120 24 127 18Z"/>'
 '<path d="M114 54l9 10 17-20"/><g class="hat"><path d="M112 36l-1 14M118 33l-1 8"/></g>',
 '<path d="M46 20C67 19 84 37 84 58S67 95 46 95 8 79 9 58 26 21 46 20Z"/><path d="M19 85L74 31"/>')
_SC['Publisher Tooling']=(
 '<path d="M13 14l21 1-1 20-20-1z"/><path d="M14 48l20-1 1 21-20 1z"/><path d="M13 82l21 1-1 20-20-1z"/>'
 '<path d="M46 25c14-3 30 1 46-1M46 58c10-2 26 1 38-1M46 93c12-2 28 1 42-1"/>'
 '<path d="M130 43C139 43 146 50 145 58S138 73 130 72 115 66 115 58 121 44 130 43Z"/><path d="M130 52c4 0 6 3 6 6s-3 6-6 6-6-3-6-6 2-6 6-6z"/>'
 '<path class="tooth" d="M130 34v7M130 75v7M107 58h7M146 58h7M114 41l5 5M141 70l-5-5M146 41l-5 5M114 75l5-5"/>'
 '<g class="hat"><path d="M54 33c8-1 22 0 30-1M54 66c6-1 16 0 24-1"/></g>',
 '<path d="M18 24l5 6 10-12M18 58l5 6 10-12M18 93l5 6 10-12"/>')
_SC['Trip Planner']=(
 '<path d="M12 12C25 9 45 11 58 12c4 0 4 3 4 6v12c0 3-1 4-5 4H36l-9 9v-9H14c-3 0-4-2-4-5V17c0-3 0-5 2-5z"/>'
 '<circle cx="23" cy="22" r="1.6" class="dotf"/><circle cx="35" cy="22" r="1.6" class="dotf"/><circle cx="47" cy="22" r="1.6" class="dotf"/>'
 '<path d="M14 67C28 65 50 66 68 67c3 0 3 3 3 5v28c0 3-1 5-4 5-16 1-36 1-52 0-3 0-3-3-3-5V72c0-3 1-5 2-5z"/>'
 '<path d="M32 66v-7c0-3 2-4 4-4h12c2 0 4 1 4 4v7M29 67l-1 38M56 67l1 38"/>'
 '<g class="hat"><path d="M18 76l7-7M18 86l8-8M62 96l6-6M62 86l7-7"/></g>'
 '<path d="M120 64C106 50 100 42 101 32 102 20 112 13 122 14c10 1 17 9 16 19-1 9-7 18-18 31Z"/><path d="M120 24c5 0 8 3 8 7s-4 8-8 7-8-3-8-7 3-7 8-7z"/>'
 '<path d="M104 71c8 3 20 3 29 0"/>',
 '<path class="trail" d="M76 86C104 98 134 90 122 72"/><path class="trail" d="M118 78l4-7 7 4"/>')
_SC['Cycle Insights']=(
 '<path d="M24 12C31 12 36 17 36 24S31 36 24 36 12 31 12 24 17 12 24 12Z"/>'
 '<path d="M60 12C67 12 72 17 72 24S67 36 60 36 48 31 48 24 53 12 60 12Z"/><g class="hat"><path d="M52 18v13M55.5 14.5v20M59 13v22"/></g>'
 '<path d="M96 12C103 12 108 17 108 24S103 36 96 36 84 31 84 24 89 12 96 12Z" class="solid"/>'
 '<path d="M132 12C139 12 144 17 144 24S139 36 132 36 120 31 120 24 125 12 132 12Z"/><g class="hat"><path d="M136 15v19M139.5 17v15M143 21v8"/></g>'
 '<path d="M40 24h4M76 24h4M112 24h4" stroke-dasharray="2 3"/>'
 '<path d="M44 67C60 65 100 65 116 67 115 87 100 101 80 101S46 87 44 67Z"/>'
 '<path d="M62 66C57 52 66 44 78 42 82 54 76 62 62 66ZM64 62L77 46"/><path d="M88 66c0-10 7-16 18-17 0 9-7 16-18 17z"/>'
 '<g class="hat"><path d="M52 76l10 12M62 74l12 14M96 78l-9 14"/></g>'
 '<path d="M133 70v12M127 76h12M26 82v8M22 86h8"/>',
 '<path class="trail" d="M62 66C57 52 66 44 78 42 82 54 76 62 62 66z"/><path class="acc" d="M96 12C103 12 108 17 108 24S103 36 96 36 84 31 84 24 89 12 96 12Z"/>')
_SC['Fintracker']=(
 '<path d="M12 10c1 30 0 62 0 94 40 1 92 0 138 0"/>'
 '<path d="M26 78h18v26H26Z"/><path d="M56 64h18v40H56Z"/><path d="M86 48h18v56H86Z"/>'
 '<g class="hat"><path d="M28 100l14-14M28 92l14-14M58 100l14-14M58 90l14-14M58 80l14-14M88 100l14-14M88 90l14-14M88 80l14-14M88 70l14-14"/></g>'
 '<ellipse cx="132" cy="97" rx="13" ry="4.5"/><path d="M119 97v-9M145 97v-9"/><ellipse cx="132" cy="88" rx="13" ry="4.5"/><path d="M119 88v-9M145 88v-9"/><ellipse cx="132" cy="79" rx="13" ry="4.5" class="fill"/>'
 '<path d="M134 18C141 18 147 24 146 31S139 43 133 42 122 37 122 30 127 18 134 18Z"/><path d="M134 25c4 0 6 3 6 6s-3 6-6 6-6-3-6-6 2-6 6-6z"/>',
 '<path class="trail" d="M20 62L52 46l24 8 38-30"/><path class="trail" d="M102 22l13 1-1 13"/>')
