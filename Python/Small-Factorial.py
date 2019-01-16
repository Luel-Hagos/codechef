n=int(input())
k=[]
num=1
for i in range(n):
    x=int(input())
    k.append(x)
for i in range(len(k)):
    if k[i]==0:
        num=1
    else:
        for j in range(1,k[i]+1):
            num*=j
    print(num)
    num=1