import json,os,urllib.request as U
V=[0,100,320,330,500,900,0]
DK=(-17,-16,-15,-1,1,15,16,17);DN=(-33,-31,-18,-14,14,18,31,33);DB=(-17,-15,15,17);DR=(-16,-1,1,16)
DT=((),(),DN,DB,DR,DK,DK)
CM=[15]*128;CM[4]=12;CM[7]=14;CM[0]=13;CM[116]=3;CM[119]=11;CM[112]=7
CL=(((6,1,(5,6)),(2,2,(1,2,3))),((118,4,(117,118)),(114,8,(113,114,115))))
SQ=[s for s in range(128)if not s&136]
ND=BG=0;RB=[0];GS=None;GN=-1;NA=0
I=10**6;Ab=Exception
def A(st,s,b):
 B=st[0];o=b*8
 for d in(15,17):
  t=s+d*(2*b-1)
  if not t&136 and B[t]==1+o:return 1
 for ds,tt,sl in((DN,2,0),(DK,6,0),(DB,3,1),(DR,4,1)):
  for d in ds:
   t=s+d
   while not t&136:
    p=B[t]
    if p:
     if p==tt+o or sl and p==5+o:return 1
     break
    if not sl:break
    t+=d
 return 0
def G(st,co):
 B,T,C,E=st[:4]
 ms=[];ap=ms.append
 for s in SQ:
  p=B[s]
  if not p or p>>3!=T:continue
  t=p&7
  if t==1:
   u=16-32*T;ds=[];one=s+u
   if not co and not B[one]:ds.append(one)
   for d in(u-1,u+1):
    w=s+d
    if not w&136 and(B[w]and B[w]>>3!=T or w==E):ds.append(w)
   for w in ds:
    if w>>4==7-7*T:
     for pr in(5,4,3,2):ap(s|w<<7|pr<<14)
    else:ap(s|w<<7)
   if not co and not B[one]and s>>4==1+5*T and not B[s+2*u]:ap(s|s+2*u<<7)
  elif t>1:
   for d in DT[t]:
    w=s+d
    while not w&136:
     q=B[w]
     if q:
      if q>>3!=T:ap(s|w<<7)
      break
     if not co:ap(s|w<<7)
     if t in(2,6):break
     w+=d
   if t==6 and not co and s==4+112*T:
    for w,bt,emp in CL[T]:
     if C&bt and not any(B[q]for q in emp)and not A(st,s,1-T)and not A(st,(s+w)//2,1-T):ap(s|w<<7)
 return ms
def M(st,m):
 B,T,C,E,K=st
 B=B[:];K=K[:]
 f=m&127;w=m>>7&127;pr=m>>14&7;p=B[f];t=p&7;cp=B[w]
 B[f]=0
 if t==1 and not cp and w==E and f&7!=w&7:
  cs=w-16+32*T;cp=B[cs];B[cs]=0
 B[w]=pr|(p&8)if pr else p
 if t==6:
  K[T]=w
  if abs(w-f)==2:rf,rt=(w+1,w-1)if w>f else(w-2,w+1);B[rt]=B[rf];B[rf]=0
 C&=CM[f]&CM[w]
 return[B,1-T,C,(f+w)//2 if t==1 and abs(w-f)==32 else-1,K]
def W(st):
 B,T=st[0],st[1]
 sc=0
 for s in SQ:
  p=B[s]
  if not p:continue
  t=p&7;c=p>>3;r=s>>4;rr=r^(7*c)
  if t==1:v=100+5*rr
  elif t==6:v=-10*rr
  else:v=V[t]
  sc+=v*(1-2*c)
 return sc if T==0 else-sc
def OS(st,m,tm):
 if m==tm:return 1<<30
 v=st[0][m>>7&127]&7 or m>>14&7
 return V[v]*32 if v else 0
def S(st,d,a,b,pl):
 global ND
 ND+=1
 if ND&1023==0 and ND>BG:raise Ab
 B,T,C,E,K=st
 ic=A(st,K[T],1-T)
 if ic and d>0:d+=1
 q=d<=0 and not ic
 if q:
  v=W(st)
  if v>=b:return b
  a=max(a,v)
 ms=G(st,q);ms.sort(key=lambda m:OS(st,m,RB[0]if pl==0 else 0),reverse=True)
 bs=-I if d>0 else a;bm=0;lg=0
 for m in ms:
  ns=M(st,m)
  if A(ns,ns[4][T],1-T):continue
  lg+=1
  sc=-S(ns,d-1,-b,-a,pl+1)
  if sc>bs:bs=sc;bm=m
  a=max(a,sc)
  if a>=b:break
 if not lg:return(-900000+pl)if ic else(0 if d>0 else a)
 if d>0:
  if pl==0:RB[0]=bm
  return bs
 return a
def CH(bg):
 global ND,BG
 BG=bg;ND=0;RB[0]=0;d=1
 while d<=64:
  try:S(GS,d,-I,I,0)
  except Ab:break
  d+=1
  if ND>BG:break
 return RB[0]or None
def UC(m):
 f=m&127;w=m>>7&127;pr=m>>14&7
 s="abcdefgh"[f&7]+str(f//16+1)+"abcdefgh"[w&7]+str(w//16+1)
 return s+("nbrq"[pr-2]if pr else"")
def ST():
 B=[0]*128
 for i,p in enumerate((4,2,3,5,6,3,2,4)):B[i]=p;B[112+i]=p+8;B[16+i]=1;B[96+i]=9
 return[B,0,15,-1,[4,116]]
def AP(st,u):
 mp={UC(m):m for m in G(st,0)}
 return M(st,mp[u])if u in mp else st
def P(p,b):
 return json.load(U.urlopen(U.Request(os.environ["MAKEFUN_ENV_URL"]+p,data=json.dumps(b).encode(),headers={"content-type":"application/json"})))
def CU(g):
 global GS,GN,NA
 mv=g["moves"];lm=g["legal_moves"]
 if g["game"]!=GN or len(mv)<NA:GS=ST();GN=g["game"];NA=0
 while NA<len(mv):GS=AP(GS,mv[NA]);NA+=1
 if GS[1]!=(g["colour"]!="white"):GN=-1;return lm[0]
 try:
  m=CH(42000 if g["plies"]<100 else 15000)
  if m is not None and UC(m)in lm:return UC(m)
 except Exception:pass
 return lm[0]
def main():
 for _ in range(9999):
  try:g=P("/game",{})
  except Exception:continue
  if g.get("status")=="done":return
  while g.get("status")=="your_move":
   u=CU(g)
   try:g=P("/move",{"game":g["game"],"move":u})
   except Exception:break
main()
