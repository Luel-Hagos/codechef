n=int(input())
k=[]
for i in range(n):
    k.append(int(input()))
k.sort()
for i in range(len(k)):
    print(k[i])