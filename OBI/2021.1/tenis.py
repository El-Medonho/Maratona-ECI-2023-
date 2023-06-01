ans = 0
for i in range(6):
    x = input()
    if(x == 'V'): ans+=1

if(ans >= 5): print(1)
elif(ans >= 3): print(2)
elif(ans >= 1): print(3)
else: print(0)