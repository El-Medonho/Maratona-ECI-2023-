n = int(input())
arr = []

while(n):
    n-=1
    x = int(input())

    if(x == 0): arr.pop()
    else: arr.append(x)

print(sum(arr))