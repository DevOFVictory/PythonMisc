(O:=[(lambda P:(N:={*map(int,P.split())})and[a*b for a in N if(b:=2020-a)in N][0],lambda P:(N:={*map(int,P.split())})and[a*b*c for a in N for b in N if(c:=2020-a-b)in N][0],),(lambda P:sum((x:=[*map(int,p.split("-"))])[0]<=a.count(c[0])<=x[1]for p,c,a in map(str.split,P.splitlines())),lambda P:sum(1==sum(c[0]==a[int(x)-1]for x in p.split("-"))for p,c,a in map(str.split,P.splitlines()))),(lambda P:sum(l[(i*3)%len(l)]=="#"for i,l in enumerate(P.split())),lambda P:(o:=(X:=lambda a,b:sum(l[(i*a)%len(l)]=="#"for i,l in enumerate(P.split()[::b])))(1,2))and[o:=o*X(d,1)for d in[1,3,5,7]]and o),(lambda P:sum(all(map(k.count,"byr iyr eyr hgt hcl ecl pid".split()))for k in P.split("\n\n")),lambda P,f=__import__("re").fullmatch:sum(all([d:=dict(x.split(":")for x in K)]+[f(p,d.get(k,""))for p,k in[(r"19[2-9]\d|200[012]","byr"),(r"20(1\d|20)","iyr"),(r"20(2\d|30)","eyr"),(r"1([5-8]\d|9[0-3])cm|(59|6\d|7[0-6])+in","hgt"),(r"#[\da-f]{6}","hcl"),("amb|blu|brn|gry|grn|hzl|oth","ecl"),(r"\d{9}","pid")]])for K in map(str.split,P.split("\n\n")))),(lambda P:max(int(l.translate(l.maketrans("FLBR","0011")),2)for l in P.split()),lambda P:[*{*range(min(S:={int(l.translate(l.maketrans("FLBR","0011")),2)for l in P.split()}),max(S)+1)}-S][0]),(lambda P:sum(len(set(g)-{"\n"})for g in P.split("\n\n")),lambda P:sum(len(set.intersection(*map(set,g.split())))for g in P.split("\n\n"))),(lambda P,f=__import__("re").findall:len((g:={})or[[(m:=f("([a-z]+ [a-z]+) bag",l)),[g.setdefault(x,[]).append(m[0])for x in m[1:]]]for l in P.splitlines()]and(dfs:=lambda p:set.union({p},*map(dfs,g.get(p,[]))))("shiny gold"))-1,lambda P,r=__import__("re"):(g:={})or[g.setdefault(r.match(r"^(\w+ \w+)",l).group(1),[]).extend(r.findall(r"(\d+) (\w+ \w+) bag",l))for l in P.splitlines()]and(dfs:=lambda p:1+sum(dfs(q)*int(n)for n,q in g.get(p,[])))("shiny gold")-1,),(lambda P,p=[0],a=[0]:[*iter(lambda:(p[-1]not in p[:-1]and(k:=P.splitlines()[p[-1]].split(),a.append(a[-1]+(k[0]=="acc")*int(k[1])),p.append(p[-1]+(int(k[1])if"jmp"==k[0] else 1)))),False)]and a[-1],lambda P:(L:=P.splitlines())and next(iter(y[1]for x in range(len(P))if(y:=(lambda f,p=[0],a=[0],s=set():[*iter(lambda:((c:=p[-1])<len(L)and c not in s and(s.add(c),k:=L[c].split(),k[0]=="acc"and a.append(a.pop()+int(k[1])),p.append(p.pop()+(int(k[1])if"jmp"==k[0]and f!=c or"nop"==k[0]and f==c else 1)))),False)]and(p[-1]>=len(L),a[-1]))(x))[0]))),(lambda P:(n:=[*map(int,P.split())])and next(iter(x for i,x in enumerate(n[25:])if(s:=set())or 1-any((2*y-x and x-y in s)or s.add(y)for y in n[i:i+25]))),lambda P:(n:=[*map(int,P.split())],t:=next(iter(x for i,x in enumerate(n[25:])if(s:=set())or 1-any((2*y-x and x-y in s)or s.add(y)for y in n[i:i+25]))))and next(iter(min(n[a:b])+max(n[a:b])for a in range(len(n))for b in range(a+2,len(n))if(s:=sum(n[a:b])==t)))),(lambda P:(n:=sorted(map(int,P.split())))and(X:=[b-a for a,b in zip([0]+n,n)].count)(1)*(X(3)+1),lambda P:(n:=sorted(map(int,P.split())))and(d:={})or(c:=lambda i,j:j==n[-1]if i==len(n)else(0 if 3+j<n[i]else(d[(i,j)]if(i,j)in d else d.setdefault((i,j),c(i+1,j)+c(i+1,n[i])))))(0,0)),(lambda P:(L:=P.splitlines(),a:=set(),g:={(x,y):[(x+q,y+p)for p in[-1,0,1]for q in[-1,0,1]if(p or q)*(0<=y+p<len(L))*(0<=x+q<len(l))and L[y+p][x+q]!="."]for y,l in enumerate(L)for x,c in enumerate(l)if"."!=c})and next(len(a)for()in iter(tuple,1)if a==(a:={p for p,q in g.items()if not(c:=len(a&{*q}))and{p}-a or a&{p}and c<4})),lambda P:(L:=P.splitlines(),a:=set(),g:={(x,y):[f for p in[-1,0,1]for q in[-1,0,1]if(p or q)*(k:=1)and(f:=next((r*(x+k*q,y+k*p)for()in iter(tuple,0)if not(r:=(0<=y+k*p<len(L))*(0<=x+k*q<len(l)))or L[y+k*p][x+k*q]!="."or(k:=k+1)*0),0))]for y,l in enumerate(L)for x,c in enumerate(l)if"."!=c})and next(len(a)for()in iter(tuple,1)if a==(a:={p for p,q in g.items()if not(c:=len(a&{*q}))and{p}-a or a&{p}and c<5}))),(lambda P,x=0,y=0,p=1,q=0:[(c:=l[0],n:=int(l[1:]),y:=y+n*(c=="S")-n*(c=="N")+n*q*(c=="F"),x:=x+n*(c=="E")-n*(c=="W")+n*p*(c=="F"),[(k:=q,q:=p-p*2*(c=="L"),p:=k-k*2*(c=="R"))for()in(c in"LR")*n//90*[()]])for l in P.split()]and abs(x)+abs(y),lambda P,x=0,y=0,p=10,q=-1:[(c:=l[0],n:=int(l[1:]),p:=p+n*(c=="E")-n*(c=="W"),q:=q+n*(c=="S")-n*(c=="N"),x:=x+n*p*(c=="F"),y:=y+n*q*(c=="F"),[(k:=q,q:=p-p*2*(c=="L"),p:=k-k*2*(c=="R"))for()in(c in"LR")*n//90*[()]])for l in P.split()]and abs(x)+abs(y)),(lambda P:(L:=P.splitlines(),T:=int(L[0]))and int.__mul__(*min(((T//i+1)*i-T,i)for n in L[1].split(",")if"x"!=n and(i:=int(n)))),lambda P:(L:=P.splitlines(),G:=(lambda a,b:a and((r:=G(b%a,a))[0],r[2]-(b//a)*r[1],r[1])or(b,0,1)))and(lambda n,a:(q:=__import__("math").prod(n))and sum(y*(p:=q//x)*G(p,x)[1]for x,y in zip(n,a))%q)(*zip(*[(k,k-i)for i,x in enumerate(L[1].split(","))if"x"!=x and(k:=int(x))]))),(lambda P,r=__import__("re").match,m="X"*36:sum({int(g[1]):int("".join([n,x][n=="X"]for n,x in zip(m,f"{int(g[2]):036b}")),2)for l in P.splitlines()if(g:=r(r"^mem\[(\d+)\] = (\d+)$",l))or(m:=l.split()[2])*0}.values()),lambda P,r=__import__("re").match,m="X"*36:sum({((q:={t:str(min(1<<j&i,1))for j,t in enumerate(f)}),)and int("".join(q.get(*i)for i in enumerate(a)),2):int(g[2])for l in P.splitlines()if(g:=r(r"^mem\[(\d+)\] = (\d+)$",l))and(a:="".join(k[k[0]=="0"]for k in zip(m,f"{int(g[1]):036b}")),f:=[i for i in range(36)if"X"==a[i]])or(m:=l.split()[2])*0 for i in range(1<<len(f))}.values())),(lambda P:(N:=[*map(int,P.split(","))],H:=dict(zip(N,range(len(N)-1))))and(n:=N[-1],)and[0 for t in range(len(N),2020)if(o:=t-1-H.get(n,t-1),H.update({n:t-1}),n:=o)*0]or n,lambda P:(N:=[*map(int,P.split(","))],H:=dict(zip(N,range(len(N)-1))))and(n:=N[-1],)and[0 for t in range(len(N),30000000)if(o:=t-1-H.get(n,t-1),H.update({n:t-1}),n:=o)*0]or n),(lambda P:(I:=[*map(str.splitlines,P.split("\n\n"))])and sum(f*(1-any(x[0]<=f<=x[1]for r in I[0]for s in r.split(": ")[1].split("or")if(x:=[*map(int,s.split("-"))])))for t in I[2][1:]for f in map(int,t.split(","))),lambda P:(n:=len((I:=[*map(str.splitlines,P.split("\n\n"))])[0]),Z:=set(range(n)),V:=lambda R,n:any(k[0]<=n<=k[1]for r in R.split(":")[1].split("or")if(k:=[*map(int,r.split("-"))])),X:=lambda x:[*map(int,x.split(","))],M:=X(I[1][1]),w:=[{*Z}for _ in I[0]],W:=[None]*n,[w[r].remove(f)for t in map(X,I[2][1:])if all(any(V(r,f)for r in I[0])for f in t)for f in Z for r in Z if not V(I[0][r],t[f])],[(W.__setitem__(i,j:=w[i].pop()),[w[k].remove(j)for k in Z if j in w[k]])for _ in I[0]for i in Z if len(w[i])==1],__import__("math").prod(M[W[i]]for i,R in enumerate(I[0])if"departure"==R[:9]))[9]),(lambda P,N=[(i,j,k)for i in[-1,0,1]for j in [-1,0,1]for k in[-1,0,1]]:(S:={(0,i,j)for i,l in enumerate(P.splitlines())for j,c in enumerate(l)if"#"==c},[(S:={(x,y,z)for(x,y,z)in{(x+i,y+j,z+k)for(x,y,z)in S for(i,j,k)in N}if(c:=sum((x+i,y+j,z+k)in S for(i,j,k)in N if i or j or k))in(2,3)*(a:=(x,y,z)in S)or(1-a,c)==(1,3)})for _ in"."*6])and len(S),lambda P,N=[(i,j,k,l)for i in[-1,0,1]for j in [-1,0,1]for k in[-1,0,1]for l in[-1,0,1]]:(S:={(0,0,i,j)for i,l in enumerate(P.splitlines())for j,c in enumerate(l)if"#"==c},[(S:={(w,x,y,z)for(w,x,y,z)in{(w+h,x+i,y+j,z+k)for(w,x,y,z)in S for(h,i,j,k)in N}if(c:=sum((w+h,x+i,y+j,z+k)in S for(h,i,j,k)in N if any([h,i,j,k])))in(2,3)*(a:=(w,x,y,z)in S)or(1-a,c)==(1,3)})for _ in"."*6])and len(S)),(lambda P:sum(map((E:=(lambda e:(n:="",x:=0,b:="",[(k:=1,c=="("and(x and(b:=b+c),x:=x+1,k:=0),c==")"and(x:=x-1,(b:=b+c)if x else (n:=n+str(E(b)),b:=""),k:=0),k*x and(b:=b+c,k:=0),k and(n:=n+c))for c in e.replace(" ","")],o:=0,b:=0,x:=False,[(o:=[o+b,o*b][x],b:=0,x:=c=="*")for c in n+" "if not(c.isnumeric()and(b:=b*10+int(c),))],o)[-1])),P.splitlines())),lambda P,p=__import__("math").prod:sum(map((E:=(lambda e:(n:="",x:=0,b:="",[(k:=1,c=="("and(x and(b:=b+c),x:=x+1,k:=0),c==")"and(x:=x-1,(b:=b+c)if x else(n:=n+str(E(b)),b:=""),k:=0),k*x and(b:=b+c,k:=0),k and(n:=n+c))for c in e.replace(" ","")],p(sum(map(int,x.split("+")))for x in n.split("*")))[-1])),P.splitlines()))),(lambda P:(X:=[*map(str.splitlines,P.split("\n\n"))],R:=dict(l.split(": ")for l in X[0]),m:=lambda p,s:[j+k for j in([len(p[0])-2]*(p[0][1:-1]==s[:len(p[0])-2])if p[0][0]=='"'else M(p[0],s))for k in m(p[1:],s[j:])]if p else[0],M:=lambda i,s:set().union(*(m(r.split(),s)for r in R[i].split(" | ")))if s else[])and sum(len(m)in M("0",m)for m in X[1]),lambda P:(X:=[*map(str.splitlines,P.split("\n\n"))],R:={**dict(l.split(": ")for l in X[0]),"8":"42 | 42 8","11":"42 31 | 42 11 31"},m:=lambda p,s:[j+k for j in([len(p[0])-2]*(p[0][1:-1]==s[:len(p[0])-2])if p[0][0]=='"'else M(p[0],s))for k in m(p[1:],s[j:])]if p else[0],M:=lambda i,s:set().union(*(m(r.split(),s)for r in R[i].split(" | ")))if s else[])and sum(len(m)in M("0",m)for m in X[1])),(lambda P,E=lambda e:min(int(x:="".join(e).translate({46:48,35:49}),2),int(x[::-1],2)):(m:={})or[m.setdefault(e,[]).append(int(n.split()[1][:-1]))for n,*L in map(str.splitlines,P.split("\n\n"))if(t:=list(zip(*L)))for e in map(E,[L[0],L[-1],t[0],t[-1]])]and(b:=[v for v,*x in m.values()if not x])and __import__("math").prod({x for x in b if b.count(x)==2}),lambda Q,z=enumerate,Y=range,O=[1,0,3,2],E=lambda e:min(int(x:="".join(e).translate({46:48,35:49}),2),int(x[::-1],2)):(R:=lambda t,o,c=(3,1):c==o and[*map("".join,t)]or[3,2,0,1][c[0]]==c[1]and R([*zip(*t)],o,c[::-1])or R([l[::-1]for l in t],o,(O[c[0]],c[1])),m:={},P:={},[m.setdefault(e,[]).append((i,n))for N,*l in map(str.splitlines,Q.split("\n\n"))if(t:=list(zip(*l)),n:=int(N.split()[1][:-1]),P.update({n:[L[1:-1]for L in l[1:-1]]}))for i,e in z(map(E,[l[0],l[-1],t[0],t[-1]]))],G:={},[(G.setdefault(t1,{}).update({o1:(o2,t2)}),G.setdefault(t2,{}).update({o2:(o1,t1)}))for(o1,t1),(o2,t2)in[v for k,v in m.items()if len(v)==2]],B:={(C:=next(k for k,v in G.items()if len(v)==2))},D:=[(U:=(lambda k,c:B.add(c)or(1+U(O[G[c][k][0]],G[c][k][1])if k in G[c]else 1)))(k,C)for k in G[C]],[v.setdefault(i,None)for k, v in G.items()if k not in B for i in Y(4)],T:=[[None]*D[0]for _ in Y(D[1])],Q:=[(C,0,0,*G[C])],V:=set(),next(0 for()in iter(tuple,0)if not Q or(p:=Q.pop(0),p[0]not in V and(V.add(p[0]),T[p[1]].__setitem__(p[2],R(P[p[0]],p[3:5])),[(3<=len(G[f[1]])and G[f[1]].pop(f[0]),2>=len(G[f[1]])and(A==p[3]and(x:=O[f[0]],y:=[*(set(G[f[1]])-{x,f[0]})][0])or(y:=O[f[0]],x:=[*(set(G[f[1]])-{y,f[0]})][0]),Q.append((f[1],u,v,x,y))))for A,u,v in[(p[3],p[1],p[2]+1),(p[4],p[1]+1,p[2])]if(f:=G[p[0]].get(A))]))*0),I:=["".join(l)for t in T for l in zip(*t)])and sum(l.count("#")for l in I)-len({s for i in Y(4)for j in Y(4)if i not in(j,O[j])and(m:=R([18*" "+"# ",3*"#    #"+"##",6*" # "+"  "],(i,j)))for y in Y(len(I)-len(m)+1)for x in Y(len(I[0])-len(m[0])+1)if(p:=[(y+i,x+j)for i,l in z(m)for j,c in z(l)if"#"==c])if all(I[i][j]=="#"for i,j in p)for s in p})),(lambda P:(a:={},i:=[],[a.setdefault(x,[]).append(j)for l in P.splitlines()if(k:=l.split(" (contains "),i.extend(j:=k[0].split()))for x in k[1].strip(")").split(", ")],a:={0}.union(*[set(k[0]).intersection(*k)for k in a.values()]),sum(1-(x in a)for x in i))[4],lambda P:(a:={},[a.setdefault(x,[]).append(k[0].split())for l in P.splitlines()if(k:=l.split(" (contains "))for x in k[1].strip(")").split(", ")],a:={k:{*v[0]}.intersection(*v)for k,v in a.items()},f:={},next([]for()in iter(list,0)if not a or([t.remove(g)for k,v in[*a.items()]if 1==len(v)and(f.setdefault(k,g:=[*v][0]),a.pop(k))for t in a.values()if g in t])*0))and",".join(x[1]for x in sorted(f.items()))),(lambda P:(p:=[[*map(int,x.split()[2:])]for x in P.split("\n\n")],next(0 for()in iter(list,0)if not(p[0]and p[1])or p[(x:=(k:=[p[0].pop(0),p[1].pop(0)])[0]<k[1])].extend([k[x],k[1-x]])))and sum(x*(i+1)for i,x in enumerate((p[0]+p[1])[::-1])),lambda P:(c:=lambda p,q:(s:=set())or next(f*(bool(q),p+q)or(0,)for()in iter(list,0)if (f:=not(p and q))or(k:=(tuple(p),tuple(q)))in s or s.add(k)or[p,q][(w:=c(p[:d[0]],q[:d[1]])[0]if(d:=[p.pop(0),q.pop(0)])[0]<=len(p)and d[1]<=len(q)else d[1]>d[0])].extend(d[::1-2*w])))and sum(x*(i+1)for i,x in enumerate((c(*[[*map(int,x.split()[2:])]for x in P.split("\n\n")])[1])[::-1]))),(lambda P,r=range:(n:=[*map(int,P)],S:=dict(zip(n,n[1:]+n[:1])),c:=n[0],[0 for _ in r(100)if(u:=S[(t:=S[(s:=S[(f:=S[c])])])],d:=next(k for i in r(2,7)if(k:=(c-i)%len(S)+1)not in(f,s,t)),[S.__setitem__(*x)for x in[(c,u),(t,S[d]),(d,f)]],c:=S[c])*0])and((k:=lambda x:x-1 and str(x)+k(S[x])or"")(S[1])),lambda P,r=range:(n:=[*map(int,P)],S:=[*r(1,1000002)],[S.__setitem__(*x)for x in zip([-1]+n,n+[len(n)+1])],c:=n[0],[0 for _ in r(10000000)if(u:=S[(t:=S[(s:=S[(f:=S[c])])])],d:=next(k for i in r(2,7)if(k:=(c-i)%(len(S)-1)+1)not in(f,s,t)),[S.__setitem__(*x)for x in[(c,u),(t,S[d]),(d,f)]],c:=S[c])*0])and(f:=S[1])*S[f]),(lambda P:(g:=(lambda l:((((t:=g(l[1:]))[0]+1-2*(l[0]=="w"),t[1])if l[0]in"ew"else((t:=g(l[2:]))[0]+(l[:2]=="se")-(l[:2]=="nw"),t[1]+1-2*(l[0]=="n")))if l else(0,0))),b:=set(),[b:=b^{g(l)}for l in P.splitlines()])and len(b),lambda P:(g:=(lambda l:((((t:=g(l[1:]))[0]+1-2*(l[0]=="w"),t[1])if l[0]in"ew"else((t:=g(l[2:]))[0]+(l[:2]=="se")-(l[:2]=="nw"),t[1]+1-2*(l[0]=="n")))if l else(0,0))),n:=(lambda x,y:{(x+p,y+q)for p,q in[(1,0),(-1,0),(1,1),(0,1),(0,-1),(-1,-1)]}),s:=set(),[s:=s^{g(l)}for l in P.splitlines()],[0 for _ in"_"*100if(f:=set(),F:=set(),[(a*(c not in(1,2))and f.add((x,y)),2==c*(1-a)and F.add((x,y)))for p,q in s for x,y in{(p,q)}|n(p,q)if(c:=len(s&n(x,y)),a:=(x,y)in s)],s:=s-f|F)])and len(s)),(lambda P,k=1,i=0:(n:=[*map(int,P.splitlines())],next(0 for()in iter(list,0)if k in n or(k:=(k*7)%20201227,i:=i+1)*0))and pow(n[1-n.index(k)],i,20201227),)],[(P:=print,i and P(),P(f"=== Day {i+1:02} ==="),P(f"Part 1:",a(p:=open(f"{i+1:02}.txt").read().strip())),b and P(f"Part 2:",b[0](p)))for i,(a,*b)in [*enumerate(O)]])
