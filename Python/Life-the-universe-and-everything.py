i=0
j=0
k=[]
while i!=42:
    k.append(int(input()))
    i=k[j]
    j+=1
k.append(int(input()))
for i in range(len(k)-2):
    print(k[i])