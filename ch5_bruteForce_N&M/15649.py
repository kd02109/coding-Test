import sys
'''
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 
길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

'''

n,m = map(int, input("1~n, m(배열의 개수):").split())
c =[False]*(n+1) #숫자 사용 여부
a=[0]*m #고른 수열 저장.

def go(index, n, m):
    #출력 부분 입력!
    if index == m:
        sys.stdout.write(' '.join(map(str,a))+'\n')
        return
    #알고리즘 진행 부분
    for i in range(1,n+1):
        if c[i]:
            continue
        c[i] =True
        a[index] = i
        print(a)
        print(c)
        go(index+1, n, m)
        c[i] = False
    #이해가 잘 안되넹? 
go(0,n,m)

