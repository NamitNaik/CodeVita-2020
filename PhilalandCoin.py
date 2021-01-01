T=int(input())
if(T>=1 and T<=100):
    i=1
    lst1=list()
    lst2=list()
    while(i<=T):
        N=int(input())
        if(N>=1 and N<=5000):
            lst1.append(N)
            i=i+1
        else:
            i=i+1
            continue
    for i in lst1:
        den=0
        sum=0
        count=0
        while(sum<=int(i)):
            if sum==int(i):
                break
            den=den+1
            sum=sum+den
            count=count+1
        lst2.append(count)
    for j in lst2:
        print(j)
else:
    quit()
