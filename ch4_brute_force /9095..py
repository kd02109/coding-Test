# 1, 2, 3더하기
k = int(input("테스트 케이스 개수를 입력하세요!: "))
for _ in range(k):
    ans=0
    n=int(input())
    for l1 in range(1,4):
        if l1 == n:
            ans+=1
        for l2 in range(1,4):
            if l1+l2 ==n:
                ans+=1
            for l3 in range(1,4):
                if l1+l2+l3 == n:
                    ans+=1


'''
이 방법은 아닌 것 같다. 참고만합시다. 재귀 방정식으로는 어떻게? 
'''