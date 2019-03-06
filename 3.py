length = int(input())
arr = [0]*2001
inp = input().split()
for x in range(length):
    arr[int(inp[x])]+=1

longest = 0
pms = 0

'''
for height in range(arr[0]+arr[1],arr[-1]+arr[-2]+1):
    c_arr = arr[:]
    y = 0;
    length = 0
    while (y < len(c_arr)):
        x = y+1;
        while (x < len(c_arr)):
            if (c_arr[x]+c_arr[y]==height):
                length+=1
                c_arr.pop(x)
                c_arr.pop(y)
                y = -1
                break
            x+=1
        y+=1
    if (length>longest):
        pms = 1
        longest = length
    elif (length == longest):
        pms +=1

lens = [0]*(arr[-1]*arr[-2])
for x in range(len(arr)-1):
    for y in range(x,len(arr)):
        lens[arr[x]+arr[y]-1]+=1
for x in range(len(lens)):
    if (lens[x]>longest):
        longest = lens[x]
        pms = 1
    elif (lens[x]==longest):
        pms+=1;
'''
def boards(height, lens):
    a = max(1,height-2000)
    b = height-a
    num_boards = 0
    lengths = lens[:]
    while (a <= (height/2)):
        if (a==b):
            boards = lengths[a]/2
            lengths[a]-=boards*2
            num_boards+=boards
        else:
            print(a,b)
            boards = min(lengths[a],lengths[b])
            lengths[a]-=boards
            lengths[b]-=boards
            num_boards += boards;
        a+=1
        b+=1
    return(num_boards)

for x in range(2,4001):
    ans = boards(x,arr)
    if (ans > longest):
        longest = ans
        pms = 0
    if (ans == longest):
        pms+=1
print(longest," ",pms)
