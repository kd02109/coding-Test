# 퇴사!

inf = -10**9
n = int(input())
t = [0]*(n+1)
p = [0]*(n+1)

for i in range(1, n+1):
    t[i], p[i] = map(int, input().split())
ans = 0

def go(day, sum_m):
    global ans
    if(day == n+1):
        ans = max(ans,sum_m)
        return
    if day > n+1:
        return

    go(day+1,sum_m)
    go(day+t[day],sum_m+p[day])


go(1,0)
print(ans)