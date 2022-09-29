#수 이어쓰기!
n = int(input("1부터 연결할 수를 작성하세요: "))

ans = 0 # 정답
start = 1 # n과 비교하기 위한 값
length = 1 # 자릿수

while start<=n:
    end = start*10-1
    if(end>n):
        end = n
    ans += (end-start+1)*length
    start *= 10
    length +=1
print(ans)