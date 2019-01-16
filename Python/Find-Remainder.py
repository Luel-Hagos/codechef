n=int(input())
k=[]
for i in range(n):
    A,B=input().split()
    B=int(B)
    A=int(A)
    k.append(A%B)
for i in range(len(k)):
    print(k[i])