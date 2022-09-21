MAX = 1000000
# 리스트의 갯수 백만개로 증가
d= [1] * (MAX+1)
s= [0] * (MAX+1)
for i in range(2,MAX+1):
    j=1
    while i*j <= MAX:
        d[i*j] += i
        j+=1
        ''' 
        1*1+=1, 1*2 +=1 1*3+=1 ... 1*1000000 +=1
        2*1+=2 2*2+=2 2*3+=2
        3*1+=3 3*2+=3 3*3+=3
        배수 집어널기
        '''
# g(n) 모음        
for i in range(1, MAX+1):
    s[i] = s[i-1] +d[i]

# 뽑을 배열의 개수
t = int(input())
ans = []
for _ in range(t):
    #g(n)값을 찾을 자연수 선택
    n = int(input())
    ans.append(s[n])

print("\n".join(map(str,ans))+"\n")