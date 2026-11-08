import base64
s=open('/home/claude/portfolio/src_v3.html').read()
m={'{{IMG_ME}}':'me_cut.webp','{{IMG_DASH}}':'dashboard.jpg','{{IMG_ITIN}}':'itinerary.jpg','{{IMG_CHAT}}':'plan-with-ai.jpg','{{IMG_DAY}}':'day-by-day.jpg','{{IMG_CI1}}':'ci_baseline.jpg','{{IMG_CI2}}':'ci_slip.jpg','{{IMG_CI3}}':'ci_checks.jpg','{{IMG_CI4}}':'ci_phone.jpg','{{IMG_FT1}}':'ft_home.jpg','{{IMG_FT2}}':'ft_invest.jpg','{{IMG_FT3}}':'ft_chat.jpg'}
for k,fn in m.items():
    mt='png' if fn.endswith('png') else ('webp' if fn.endswith('webp') else 'jpeg')
    s=s.replace(k,'data:image/%s;base64,'%mt+base64.b64encode(open('/home/claude/portfolio/img/'+fn,'rb').read()).decode())
s=s.replace('{{CIH}}','576').replace('{{RESUME_PDF}}',base64.b64encode(open('/home/claude/resume/Mizuho_Li_resume_2026_v2.pdf','rb').read()).decode())
assert '{{' not in s.split('<script>')[1][:0] 
open('/home/claude/portfolio/index_v3.html','w').write(s)
print(len(s))
