import math
N = int(input())

m = input().split()
for x in range(N):
    m[x]=int(m[x])
m.sort()
low = [0]*(math.ceil(N/2))
for x in range(math.ceil(N/2)):
    low[x]=m[x]
high = [0]*(N//2)
for x in range(N//2):
    high[x]=m[x+math.ceil(N/2)]
low.reverse()
for x in range(math.ceil(N/2)):
    print(low[x],end =" ")
    if (not (x==N//2 and N%2==1)):
        print(high[x],end=" ")
