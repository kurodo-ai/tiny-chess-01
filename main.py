import os,json,time,urllib.request as U
H={2:[-33,-31,-18,-14,14,18,31,33],3:[-17,-15,15,17],4:[-16,-1,1,16]}
H[5]=H[3]+H[4];H[6]=H[5]
PV=[0,100,320,330,500,900,0]
FL="abcdefgh"
def MK(s):
 r=[0]*128
 for i,c in enumerate(s):
  j=(i//4)*16;v=(int(c)-5)*10;r[j+i%4]=r[j+7-i%4]=v
 return r
TS=["55555555556655675678678978995555","01221355256626672567256613550122","34444555456646664566455645553444","","","78656765454334322321211021102110"]
PS=[None]+[MK(x)for x in TS]
ND=BG=RB=0;TT={};I=10**7
def A(st,s,by):
 B=st[0];o=by*6
 for d in(15,17):
  t=s-d+2*d*by
  if not t&136 and B[t]==1+o:return 1
 for tt,sl in((2,0),(3,1),(4,1),(6,0)):
  for d in H[tt]:
   t=s+d
   while not t&136:
    if(p:=B[t]):
     if p==tt+o or sl and p==5+o:return 1
     break
    if not sl:break
    t+=d
 return 0
def G(st,co):
 B,T,C,E,K,V=st;ms=[];ap=ms.append
 for s in range(128):
  if s&136:continue
  p=B[s]
  if not p or p//7!=T:continue
  t=p-6*T
  if t==1:
   dr=16-32*T;one=s+dr;pz=one>>4 in(0,7);tg=[]
   if not B[one]:
    tg.append(one)
    if s>>4==1+5*T and not B[s+2*dr]:ap(s|(s+2*dr)<<7)
   for df in(-1,1):
    if not(w:=one+df)&136 and(B[w]and B[w]//7!=T or w==E>0):tg.append(w)
   for w in tg:
    if pz:ms+=[s|w<<7|q<<14 for q in range(2,6)]
    else:ap(s|w<<7)
  else:
   for d in H[t]:
    w=s+d
    while not w&136:
     if(cp:=B[w]):
      if cp//7!=T:ap(s|w<<7|cp<<21)
      break
     ap(s|w<<7)
     if t in(2,6):break
     w+=d
 return ms
def M(st,m):
 B=st[0][:];T=st[1];K=st[4][:];v=st[5]
 f=m&127;w=m>>7&127;pr=m>>14&7
 p=B[f];t=p-6*T;g=1-2*T
 v-=g*(PV[t]+PS[t][f^112 if T else f])
 if t==1 and B[w]==0 and w==st[3]and f&7!=w&7:
  c=w-16+32*T;B[c]=0;v+=g*(100+PS[1][c if T else c^112])
 elif B[w]:
  c=B[w];u=c-6+6*T;v+=g*(PV[u]+PS[u][w if T else w^112])
 n=pr or t;v+=g*(PV[n]+PS[n][w^112 if T else w]);B[w]=pr+6*T if pr else p;B[f]=0
 if t==6:K[T]=w
 return[B,1-T,st[2],w if t==1 and abs(w-f)==32 else 0,K,v]
def ST():
 B=[0]*128
 B[:8]=[4,2,3,5,6,3,2,4];B[112:120]=[x+6 for x in B[:8]];B[16:24]=[1]*8;B[96:104]=[7]*8
 return[B,0,15,0,[4,116],0]
def UC(m):
 return FL[m&7]+str((m>>4&7)+1)+FL[m>>7&7]+str((m>>11&7)+1)+("xxnbrq"[m>>14&7]if m>>14&7 else"")
def AP(st,u):
 mp={UC(m):m for m in G(st,0)}
 if u in mp:return M(st,mp[u])
 f=ord(u[0])-97+(int(u[1])-1)*16;w=ord(u[2])-97+(int(u[3])-1)*16
 st=M(st,f|w<<7)
 if abs(w-f)==2:
  rf,rt=(w+1,w-1)if w>f else(w-2,w+1);st[0][rt]=st[0][rf];st[0][rf]=0
 return st
def S(st,d,a,b,pl):
 global ND,RB
 ND+=1
 if ND>BG or ND&7<1 and time.time()>D:1/0
 B,T,C,E,K,V=st
 ky=(bytes(B),T);e=TT.get(ky)
 if e and e[0]>=d and pl and(not a<e[1]<b):return e[1]
 ic=A(st,K[T],1-T)
 v=V-V*T*2
 q=d<=0 and ic!=1
 if q:
  if v>=b:return v
  if v>a:a=v
 if d>2 and ic!=1 and v>=b and-S([B,1-T,C,0,K,V],d-3,-b,1-b,pl+1)>=b:return b
 bm=0;ms=G(st,0)
 if e:ms.sort(key=lambda m:m!=e[2])
 if q:ms=[m for m in ms if B[m>>7&127]or m>>14]
 bs=v if q else-I;lg=0
 for m in sorted(ms,key=lambda m:B[m>>7&127]*8-(m>>21),reverse=True):
  w=m>>7&127;cp=B[w];pr=m>>14&7
  ns=M(st,m)
  if A(ns,ns[4][T],1-T):continue
  lg+=1
  if lg==1:sc=-S(ns,d-1,-b,-a,pl+1)
  else:
   rd=d>2 and lg>3 and not cp and not pr and ic!=1
   sc=-S(ns,d-2 if rd else d-1,-a-1,-a,pl+1)
   if rd and sc>a:sc=-S(ns,d-1,-a-1,-a,pl+1)
   if sc>a and sc<b:sc=-S(ns,d-1,-b,-a,pl+1)
  if sc>bs:bs=sc;bm=m
  if pl==0:RB=bm
  if sc>a:a=sc
  if sc>=b:break
 if lg==0:return-I+pl if ic else v*q
 TT[ky]=d,bs,bm
 return bs
def CH(bg):
 global ND,BG,RB,D
 BG=bg;ND=RB=0;D=time.time()+4
 d=1
 while d<65:
  pv=RB
  try:S(GS,d,-I,I,0)
  except:RB=pv;break
  d+=1 if RB else 99
 return RB or None
def CU(g):
 global GS;GS=ST()
 L=g["legal_moves"]
 for u in g["moves"]:GS=AP(GS,u)
 try:
  m=CH(80000);u=UC(m)if m else""
  if u in L:return u
 except:pass
 return L[0]
def P(p,b):
 return json.loads(U.urlopen(U.Request(os.environ["MAKEFUN_ENV_URL"]+p,data=json.dumps(b).encode()),timeout=120).read())
def main():
 g={}
 while 1:
  try:
   s=g.get("status")
   if s=="done":return
   if s=="your_move":g=P("/move",{"game":g["game"],"move":CU(g)})
   else:g=P("/game",{})
  except:g={}
main()
