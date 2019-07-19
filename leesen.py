z=int(input())
p=list(map(int,input().split()))
g=[]
for i in p:
    if i<z:
        g.append(i)
v=(sorted(g))
print(*v)
