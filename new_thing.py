import numpy as np


n = int(input('n을 입력하세요'))
a = np.ones((n,n), dtype='int64')
# a[1,1
for i in range(n):
    for j in range(n):
        if (i+j)%2 ==0:
            a[i,j] =0

print(a)