n=int(input())
summ=[]
sum=0
for i in range(n):
    k=list(input())
    sum+=int(k[0])+int(k[-1])
    summ.append(sum)
    del(k)
    sum=0
for i in range(len(summ)):
    print(summ[i])