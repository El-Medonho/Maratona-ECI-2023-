#voces podem usar dicionario, mas como eu nao lembro a sintaxe de dicionario em python e estou com preguica de pesquisar no momento,
#eu vou só fazer uma lista de 105 elementos que vai funcionar igual a um dicionario pra mim (notem que x vai até 100 nos constraints)

n = int(input())

ans = []
in_time = []
for i in range(105): 
    ans.append(0)
    in_time.append(-1)

tempo = 0

while(n):
    n-=1
    l = input().split(" ")
    op = l[0]
    x = int(l[1])

    if(op == 'R'):
        in_time[x] = tempo
        tempo += 1
    elif(op == 'E'):
        ans[x] += tempo - in_time[x]
        in_time[x] = -1
        tempo += 1
    else:
        tempo += x-1

for i in range(105):
    if(in_time[i] != -1): 
        print(i, end = ' ')
        print(-1)
        continue
    if(ans[i] > 0):
        print(i, end = ' ')
        print(ans[i])
