n,m = map(int,input().split())
num_list = list(map(int, input().split()))
num_list.sort()
s=[]

def dfs(start):
    if len(s) == m:
        print(" ".join(map(str,s)))
        return
    for i in range(start,len(num_list)):
        s.append(num_list[i])
        dfs(i)
        s.pop()
dfs(0)