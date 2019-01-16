n=int(input())
result_1=[]
result_2=[]
k1=0
k2=0
x1=0
y1=0
for i in range(n):
    x,y=input().split()
    x=int(x)
    y=int(y)
    k1+=x
    k2+=y
    x1=k1-k2
    y1=k2-k1
    result_1.append(x1)
    result_2.append(y1)
winner_1=max(result_1)
winner_2=max(result_2)
if winner_1>winner_2:
    print(1,winner_1)
else:
    print(2,winner_2)