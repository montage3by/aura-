import re,sys
B=sys.argv[1]
svg=re.search(r'<svg.*?</svg>',open(B+'/mchs.html').read(),re.S).group(0)
HEAD="""<!doctype html><html><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600;700;800&display=swap" rel="stylesheet"><style>
*{margin:0;padding:0;box-sizing:border-box}body{width:1200px;height:1200px;font-family:'Open Sans',sans-serif;background:#0e1a26;color:#f3f1ec;overflow:hidden;position:relative}
.k{font-size:20px;letter-spacing:5px;font-weight:700;color:#cfb087;text-transform:uppercase}
.logo svg{height:52px;width:auto}.gl{background:#cfb087}
.m{color:#a9b1b9;font-weight:600}.mt{font-size:17px;letter-spacing:4px;font-weight:700;text-transform:uppercase}
</style></head><body>"""
def ph(f,css): return f"background:url('file://{B}/{f}') {css} no-repeat;filter:grayscale(15%) contrast(1.04)"
myths=[("Wi-Fi cameras are fine for a shop.","Wireless cameras are not allowed for business sites."),
("One camera over the door is enough.","At least two outdoor cameras. Faces and plates readable."),
("A week of recording is plenty.","Commercial sites keep 90 days of footage."),
("Install it and forget it.","A maintenance contract is required.")]
out={}
# V1 panel left + photo right
rows="".join(f'<div style="padding:20px 0;border-top:1px solid #2a3846"><div class="m" style="font-size:20px">"{m}"</div><div style="font-size:22px;font-weight:700;margin-top:6px">{f}</div></div>' for m,f in myths)
out['v1']=HEAD+f"""<div style="display:flex;height:1200px"><div style="width:540px;padding:70px 52px;position:relative">
<div class="k">Myth vs Fact · Hemaya</div><h1 style="font-size:46px;line-height:1.08;font-weight:800;margin:16px 0 34px">CCTV shortcuts that fail an inspection</h1>{rows}
<div class="logo" style="position:absolute;left:52px;bottom:60px">{svg}</div></div><div class="gl" style="width:6px"></div>
<div style="width:654px;{ph('p1.jpg','-130px 0/900px 1200px')}"></div></div></body></html>"""
# V2 photo top (barrier) + panel
out['v2']=HEAD+f"""<div style="height:720px;{ph('p3.jpg','0 -560px/1200px 1600px')}"></div><div class="gl" style="height:6px"></div>
<div style="padding:46px 70px;position:relative;height:474px"><div class="k">Myth vs Fact · Hemaya</div>
<h1 style="font-size:58px;line-height:1.08;font-weight:800;margin-top:16px">CCTV shortcuts that fail<br>an inspection</h1>
<p style="font-size:25px;color:#e3ded3;font-weight:600;margin-top:18px">4 myths I hear on commercial sites</p>
<div class="logo" style="position:absolute;right:70px;bottom:52px">{svg}</div></div></body></html>"""
# carousel
slides=[('p1.jpg','0 -330px/1200px 1600px',None),('p2.jpg','0 -480px/1200px 1600px',0),('p3.jpg','0 -560px/1200px 1600px',1),('p7.jpg','0 -330px/1200px 1600px',2),('p3.jpg','0 -260px/1200px 1600px',3)]
for i,(f,pos,mi) in enumerate(slides,1):
    if mi is None:
        body=f'<div class="k">Myth vs Fact · Hemaya</div><h1 style="font-size:58px;line-height:1.08;font-weight:800;margin-top:16px">CCTV shortcuts that fail<br>an inspection</h1><p style="font-size:25px;color:#e3ded3;font-weight:600;margin-top:18px">Swipe for the 4 myths I hear most often</p>'
    else:
        m,ft=myths[mi]
        body=f'<div class="k">Myth {mi+1} of 4</div><div class="m" style="font-size:30px;margin-top:22px">"{m}"</div><div class="mt" style="color:#cfb087;margin-top:26px">Fact</div><div style="font-size:44px;font-weight:800;line-height:1.12;margin-top:8px;max-width:900px">{ft}</div>'
    out[f'c{i}']=HEAD+f"""<div style="height:690px;{ph(f,pos)}"></div><div class="gl" style="height:6px"></div>
<div style="padding:44px 70px;position:relative;height:504px">{body}<div style="position:absolute;right:70px;bottom:48px" class="logo">{svg}</div>
<div style="position:absolute;left:70px;bottom:58px;font-size:19px;color:#6b7782;font-weight:700;letter-spacing:3px">{i} / 5</div></div></body></html>"""
for k,v in out.items(): open(f'{B}/myth_{k}.html','w').write(v)
