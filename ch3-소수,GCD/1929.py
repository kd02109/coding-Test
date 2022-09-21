MAX = 1000000
check = [0]*(MAX+1)
check[0] = check[1] = True

for i in range(2,MAX+1):
    if not check[i]:
        j = i+i
        while j<= MAX:
            check[j]=True
            j+=i

n,m = map(int, input().split())
for i in range(n, m+1):
    if check[i]==False:
        print(i)
