n=int(input())
k=[]
for i in range(n):
    x,y=input().split()
    x=int(x)
    y=int(y)
    k.append(x+y)
for i in range(len(k)):
    print(k[i])