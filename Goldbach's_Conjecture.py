# -*- coding:utf-8 -*-
"""
@author:壮壮Loschicos
@datetime:2020/11/6 17:57
@software: PyCharm
"""

import math

N = int(input())
a = 0
b = 0
for i in range(2, int(math.sqrt(N)) + 1):
    for k in range(2, int(math.sqrt(i)) + 1):
        if i % k == 0:
            a = 0
            break
    else:
        a = i
        for j in range(2, int(math.sqrt(N - i)) + 1):
            if (N - i) % j == 0:
                b = 0
                break
        else:
            b = N - i
    if a > 0 and b > 0:
        break
print(f"{N} = {a} + {b}")
