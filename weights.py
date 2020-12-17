n=int(input())
i=n
glist=list()
wlist=list()
total=0
count=0
while i>0:
    g=int(input())
    glist.append(g)
    wlist.append(list(map(int, input().split())))
    i=i-1

for i in wlist:
    for j in i:
        total=total+j
        count=count+1


sum=total/count
print(count)
print(glist)
print(wlist)
print(sum)
