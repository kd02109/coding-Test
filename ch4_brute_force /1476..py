#날짜 계산 문제
e,s,m = map(int, input().split())
e -=1
s -=1
m -=1
year = 0

while True:
    if year%15 == e and year%28 ==s and year % 19 ==m:
        print(year+1)
        break
    year+=1

    '''
E,S,M = map(int,input().split())
e,s,m = 1,1,1
year = 1
while True:
    if e == E and s == S and m == M:
        print(year)
        break
    e += 1
    s += 1
    m += 1
    if e == 16:
        e = 1
    if s == 29:
        s = 1
    if m == 20:
        m = 1
    year += 1

    '''