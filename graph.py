m,n=map(int,input().split())
x=m
y=n
edge1=0
edge2=0
edge=1
e=0
sp=0
if x==y:
    path=0
    e=e+1
if e==0:
    while m>1:
        m=m-1
        if x%m==0:
            edge1=edge1+1
            if m==y:
                path=edge1
                sp=sp+1
                break
            x=m
    while n>1:
        n=n-1
        if y%n==0:
            edge2=edge2+1
            y=n
if sp==1:
    print(path)
else:
    path=edge1+edge2
    print(path)
