#일곱난쟁이
import sys
n=9
a= input().split()
a= list(map(int,a))
a.sort()
total = sum(a)
for i in range(0, n):
    for j in range(i+1, n):
        if total - a[i] - a[j] == 100:
            for k in range(0, n):
                if i == k or j == k:
                    continue
                print(a[k])
            sys.exit(0)



