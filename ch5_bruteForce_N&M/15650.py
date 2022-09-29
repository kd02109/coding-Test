n,m = map(int, input().split())
# n : 1 ~ n까지 자연수
# m : 몇 자리 수열

s=[]
def dfs(start):
    if len(s) == m:
        print(" ".join(map(str,s)))
        return
    for i in range(start, n+1):
        if i not in s:
            s.append(i)
            dfs(i+1)
            s.pop()

dfs(1)