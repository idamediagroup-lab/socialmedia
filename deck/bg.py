from PIL import Image, ImageDraw, ImageFilter
import math, random
W,H = 2560,1440
def base(dark=False):
    bg = (12,12,14) if dark else (246,247,248)
    img = Image.new("RGB",(W,H),bg)
    d = ImageDraw.Draw(img,"RGBA")
    cx,cy = W//2, H//2
    # radial speed burst rays
    ray = (255,255,255,26) if dark else (255,255,255,235)
    for i in range(120):
        a = i*(360/120)+random.uniform(-1,1)
        w = random.uniform(0.5,2.4)
        r1,r2 = 120, 2100
        a1,a2 = math.radians(a-w), math.radians(a+w)
        d.polygon([(cx,cy),(cx+r1*math.cos(a1),cy+r1*math.sin(a1)),
                   (cx+r2*math.cos(a1),cy+r2*math.sin(a1)),
                   (cx+r2*math.cos(a2),cy+r2*math.sin(a2)),
                   (cx+r1*math.cos(a2),cy+r1*math.sin(a2))], fill=ray)
    img = img.filter(ImageFilter.GaussianBlur(2))
    d = ImageDraw.Draw(img,"RGBA")
    # side chevrons
    ch = (255,255,255,70) if dark else (208,212,216,150)
    for side in (0,1):
        for k in range(5):
            off = 60+k*150; t=46
            if side==0: pts=[(off,180),(off+300,H//2),(off,H-180),(off+t,H-180),(off+300+t,H//2),(off+t,180)]
            else: pts=[(W-off,180),(W-off-300,H//2),(W-off,H-180),(W-off-t,H-180),(W-off-300-t,H//2),(W-off-t,180)]
            d.polygon(pts, fill=ch)
    # halftone corner texture
    dot=(255,255,255,60) if dark else (198,203,209,120)
    for gx in range(0,W,26):
        for gy in range(0,H,26):
            e=min(gx,W-gx)/W*2; v=min(gy,H-gy)/H*2
            if e<0.42 and (v<0.5 or v>0.5):
                r=max(0,4.5*(1-e/0.42))
                if r>0.6: d.ellipse([gx-r,gy-r,gx+r,gy+r],fill=dot)
    # black frame
    fr=(0,0,0)
    d.rectangle([0,0,W,26],fill=fr); d.rectangle([0,H-26,W,H],fill=fr)
    d.rectangle([0,0,22,H],fill=fr); d.rectangle([W-22,0,W,H],fill=fr)
    return img,d

def bars(d):
    # top angled black bar with red->green ends
    top=[(0,0),(1180,0),(1250,66),(1420,66),(1490,0),(W,0),(W,96),(1470,96),(1400,30),(1270,30),(1200,96),(0,96)]
    d.polygon(top,fill=(0,0,0))
    for x in range(0,760):
        a=int(255*(1-x/760)); d.line([(x,8),(x,74)],fill=(214,26,32,a))
    for x in range(W-820,W):
        a=int(255*((x-(W-820))/820)); d.line([(x,8),(x,74)],fill=(46,204,52,a))
    for x in range(180,700):
        a=int(200*(1-abs(x-430)/270)); d.line([(x,22),(x,34)],fill=(255,214,92,max(a,0)))
    # bottom bar
    d.polygon([(0,H-150),(W,H-150),(W,H),(0,H)],fill=(0,0,0))
    for x in range(120,760):
        a=int(255*(1-(x-120)/640)); d.line([(x,H-158),(x,H-146)],fill=(214,26,32,a))
    for x in range(W-820,W-160):
        a=int(255*((x-(W-820))/660)); d.line([(x,H-158),(x,H-146)],fill=(46,204,52,a))
    d.line([(150,H-138),(W-150,H-138)],fill=(214,168,58),width=3)

random.seed(7)
for name,dark in (("bg_light",False),("bg_dark",True)):
    img,d = base(dark); bars(d)
    img.save(f"{name}.png",quality=95)
    print(name,"ok")
