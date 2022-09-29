n,m,k = map(int, input().split())
#n = 행 m=열 k=선택 칸 개수

#배열 만들기
a= [list(map(int,input().split())) for _ in range(n)]
#체크 칸 만들기
visit = [[False]*m for _ in range(n)]

answer = -100000

#x와 y의 좌표
dx = [0,0,1,-1]
dy = [1,-1,0,0]

#px = 이전에 선택한 행, py = 이전에 선택한 열, index=선택한 칸의 갯수, sum=선택한 칸의 합
def go(px,py, index, sum):
    if index == k:
        global answer
        if answer < sum:
            answer=sum
        return
    
    for x in range(px,n):
        #py if x == px else 0,m x가 이전 시작한 행과 같다면, 이어서 시작! 아니면 처음부터 
        for y in range(py if x == px else 0,m):
            if visit[x][y]:
                continue
            ok = True

            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if 0<=nx<n and 0<=ny<m:
                    if visit[nx][ny]:
                        ok=False
                
            if ok:
                visit[x][y] = True
                go(x,y,index+1,sum+a[x][y])
                visit[x][y] =False

go(0,0,0,0)
print(answer)