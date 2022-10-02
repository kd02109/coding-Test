#암호 만들기

def check(password):
    mo = 0
    ja = 0
    for i in password:
        if i in "aeiou":
            mo+=1
        else:
            ja+=1
    if (mo>=1 and ja>=2):
        return True
    else:
        return False


def go(alpha, password, length, index):
    if( len(password)==length):
        if check(password):
            print(password)
        return
    if(index >= len(alpha)):
        return
    go(alpha, password+alpha[index],length,index+1)
    go(alpha, password,length,index+1)

l, c = map(int, input().split())
alpha = input().split()
alpha.sort()
go(alpha,"",l,0)

