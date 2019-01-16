n=int(input())
count=0
result=[]
for i in range(n):
    k=list(input())
    count=k.count('4')
    result.append(count)
for i in range(len(result)):
    print(result[i])