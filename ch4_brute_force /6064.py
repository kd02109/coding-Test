#건너띄며 해보기
# 카잉 달력

t = int(input("테스트할 개수 입력: "))


for _ in range(t):
    m,n,x,y = map(int,(input("m,n,x,y 입력하세여: ").split()))
    print(m,n,x,y)
    x -=1
    y -=1
    k= x
    while k<m*n:
        if k%n ==y:
            print(k+1)
            break
        k+=m
    else:
        print(-1)

