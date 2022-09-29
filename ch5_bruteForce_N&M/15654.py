n,m = map(int,input().split())
num_list = list(map(int, input().split()))
num_list.sort()
s=[]

def dfs():
    if len(s) == m:
        print(" ".join(map(str,s)))
        return
    for i in num_list:
        if i in s:
            continue
        s.append(i)
        dfs()
        s.pop()
dfs()


