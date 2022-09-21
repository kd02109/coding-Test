def uclid(num1, num2):
    if(num2==0):
        return num1
    else:
        return uclid(num2, num1%num2)


a,b = map(int,(input().split()))
gcd = uclid(a,b)
lcm = gcd*(a//gcd)*(b//gcd)
print(gcd, lcm)
    


