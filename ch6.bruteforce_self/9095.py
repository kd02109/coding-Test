#1,2,3, 더하기




def go(sum_num, goal):
    if(sum_num == goal):
        return 1
    if(sum_num > goal):
        return 0
    now = 0
    for i in range(1,4):
        now += go(sum_num+i,goal)
    return now


t= int(input())
for _ in range(t):
    n = int(input())
    print(go(0, n))
