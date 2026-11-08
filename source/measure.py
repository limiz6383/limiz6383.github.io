import json,os,subprocess,illus
rows=[]
for t in illus._SC: rows.append(('t:'+t,illus._SC[t]))
for n,(vb,b,a) in illus._PG.items(): rows.append(('p:'+n,(b,a)))
html='<svg xmlns="http://www.w3.org/2000/svg" width="800" height="400">'+''.join(f'<g id="{k}">{b}{a}</g>' for k,(b,a) in rows)+'</svg>'
open('/tmp/m.html','w').write('<body>'+html)
js='''const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage();await p.goto('file:///tmp/m.html');
const r=await p.evaluate(()=>{const o={};document.querySelectorAll('svg>g').forEach(g=>{const b=g.getBBox();o[g.id]=[b.x,b.y,b.width,b.height]});return o});
require('fs').writeFileSync('/home/claude/portfolio/vb.json',JSON.stringify(r));console.log(r);await b.close()})()'''
open('/tmp/m.js','w').write(js)
subprocess.run(['node','/tmp/m.js'],cwd='/tmp')
