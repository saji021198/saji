z,m=map(int,input().split())
p=list(map(int,input().split()))
g=[]
for i in p:
    if i<m:
        g.append(i)
v=(sorted(g))
print(*v)
