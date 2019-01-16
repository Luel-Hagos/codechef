n=int(input())
sum=0
summ=[]
for i in range(n):
    k=list(input())
    for i in range(len(k)):
        sum+=int(k[i])
    summ.append(sum)
    sum=0
for i in range(len(summ)):
    print(summ[i])