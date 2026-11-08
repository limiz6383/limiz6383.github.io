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
    H=['<svg class="hz" viewBox="0 0 760 214" role="presentation" focusable="false">']
    for i,(ic,l1,l2,cap) in enumerate(nodes):
        cx=95+i*190
        H.append(f'<g class="nd" data-i="{i}" data-cap="{cap}" tabindex="0" role="button" aria-label="{l1} {l2}. {cap}" style="--i:{i}"><rect class="hit" x="{cx-92}" y="0" width="184" height="214" fill="transparent" stroke="none"/><g class="ic" transform="translate({cx-40},14) scale(1.25)" filter="url(#rough)">{ICONS[ic]}</g><text x="{cx}" y="150" text-anchor="middle">{l1}</text><text x="{cx}" y="171" text-anchor="middle">{l2}</text></g>')
        if i<len(nodes)-1: H.append(_arrow(cx+54,58,cx+190-54,58,18,i))
    H.append('</svg>')
    # vertical
    V=['<svg class="vt" viewBox="0 0 320 456" role="presentation" focusable="false">']
    for i,(ic,l1,l2,cap) in enumerate(nodes):
        cy=56+i*114
        V.append(f'<g class="nd" data-i="{i}" data-cap="{cap}" tabindex="0" role="button" aria-label="{l1} {l2}. {cap}" style="--i:{i}"><rect class="hit" x="0" y="{cy-52}" width="320" height="104" fill="transparent" stroke="none"/><g class="ic" transform="translate(18,{cy-32}) scale(1)" filter="url(#rough)">{ICONS[ic]}</g><text x="102" y="{cy-3}">{l1}</text><text x="102" y="{cy+19}">{l2}</text></g>')
        if i<len(nodes)-1: V.append(_arrow(50,cy+40,50,cy+114-40,-14,i))
    V.append('</svg>')
    return ('<figure class="how" data-how><div class="how-art">'+''.join(H)+''.join(V)+'</div>'
            f'<figcaption class="cap" aria-live="polite">{nodes[0][3]}</figcaption></figure>')
FILTER='<svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false"><filter id="rough" x="-5%" y="-5%" width="110%" height="110%"><feTurbulence type="fractalNoise" baseFrequency="0.04" numOctaves="2" seed="4" result="n"/><feDisplacementMap in="SourceGraphic" in2="n" scale="2.4"/></filter></svg>'
CSS=('.how{margin:var(--s2) 0 var(--s8)}.how-art svg{display:block;width:100%;height:auto;overflow:visible;color:var(--ink)}.how-art .vt{display:none;max-width:340px}'
'.how .nd{cursor:pointer;outline:none}.how .nd .ic{fill:none;stroke:currentColor;stroke-width:2;stroke-linecap:round;stroke-linejoin:round;transition:stroke .25s,transform .35s cubic-bezier(.2,.8,.2,1)}'
'.how .nd .fill{fill:#1c1b18}.how .nd .dotf{fill:currentColor;stroke:none}'
'.how .nd text{font:500 14.5px var(--body);fill:var(--ink);transition:fill .25s}.how .nd text:first-of-type{fill:var(--muted)}'
'.how .nd.on .ic,.how .nd:focus-visible .ic{stroke:var(--hand)}.how .nd.on text,.how .nd:focus-visible text{fill:var(--hand)}'
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

def thumb(title):
    nodes=FLOWS[title]; pos=[(10,4),(100,4),(100,72),(10,72)]
    g=['<svg viewBox="0 0 160 126" role="presentation" focusable="false">']
    for i,(ic,*_) in enumerate(nodes):
        x,y=pos[i]
        g.append(f'<g class="tn" style="--i:{i}" transform="translate({x},{y}) scale(.78)" filter="url(#rough)">{ICONS[ic]}</g>')
    g.append('<g class="ta"><path d="M68 29h22M90 29l-5-4M90 29l-5 4"/><path d="M125 57v11M125 68l-4-5M125 68l4-5"/><path d="M92 97H70M70 97l5-4M70 97l5 4"/></g>')
    g.append('</svg>')
    return ''.join(g)
THUMBCSS=('.thumb.fl{padding:8px 10px}.thumb.fl svg{color:var(--ink)}.thumb .tn{fill:none;stroke:currentColor;stroke-width:2.2;stroke-linecap:round;stroke-linejoin:round;transition:stroke .25s}'
'.thumb .tn .fill{fill:#1c1b18}.thumb .tn .dotf{fill:currentColor;stroke:none}.thumb .ta path{fill:none;stroke:var(--muted);stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round}'
'.item summary:hover .thumb .tn,.item summary:focus-visible .thumb .tn{animation:lit 2.4s linear infinite;animation-delay:calc(var(--i)*.6s)}'
'@keyframes lit{0%,24%{stroke:var(--hand)}25%,100%{stroke:currentColor}}'
'@media (prefers-reduced-motion:reduce){.thumb .tn{animation:none!important}}')
