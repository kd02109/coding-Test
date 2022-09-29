n,m = map(int,input().split())
num_list = list(map(int, input().split()))
num_list.sort()
s=[]

def dfs():
    if len(s) == m:
        print(" ".join(map(str,s)))
        return
    for i in range(len(num_list)):
        s.append(num_list[i])
        dfs()
        s.pop()
dfs()