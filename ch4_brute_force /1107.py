#리모컨 문제
n = int(input("이동하고자 하는 채널: "))
m = int(input("고장난 버튼의 개수:  "))
broken = [False]* 10

if m>0:
    a= list(map(int, input("0~9번 중 고장난 버튼 입력: ").split()))
else:
    a=[]
for x in a:
    broken[x] = True


def possible(c):
    if c == 0:
        if broken[0]:
            return 0
        else:
            return 1
    l=0
    while c > 0:
        if broken[c%10]:
            return 0
        l +=1
        c//=10
    return l

ans=abs(n-100)
for i in range(0,1000000+1):
    c=i
    l=possible(c)
    if l>0:
        press = abs(c-n)
        if ans > l+press:
            ans = l+press
print(ans)