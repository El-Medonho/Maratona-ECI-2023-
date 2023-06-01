
s = input()    
n = len(s)

condicional = [0,0,0,0]
arr = []
for i in range(4):
    arr.append([])
    for j in range(14):
        arr[i].append(0)

i = 0
while(i < n):
    x = 0

    x = int(s[i]+s[i+1])

    ind = -1

    if(s[i+2] == 'C'): ind  = 0
    if(s[i+2] == 'E'): ind  = 1
    if(s[i+2] == 'U'): ind  = 2
    if(s[i+2] == 'P'): ind  = 3

    if(arr[ind][x] > 0): condicional[ind] = 1
    arr[ind][x] = 1

    i += 3

for i in range(4):
    if(condicional[i] > 0): print("erro")
    else:
        print(13 - sum(arr[i]))