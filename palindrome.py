str=input()
i=0

for char in str:

    if str[0]==str[i+1]:
        str1=str[0:i+2]
        t1=i+1
        break
    i=i+1

for char in str:
    if str[t1+1]==str[i+t1+2]:
        str2=str[(t1+1):(i+t1+3)]
        t2=i+t1+2
        break
    i=i+1
str3=str[t2+1:]
print(str1)
print(str2)
print(str3)
