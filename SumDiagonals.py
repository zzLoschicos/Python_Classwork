# -*- coding:utf-8 -*-
"""
@author:壮壮Loschicos
@datetime:2020/11/5 19:30
@software: PyCharm
"""
# 求一个3×3矩阵的两条对角线元素之和（注意：两条对角线交叉点处的元素只计算一次。）
l = [1, 1, 1], [2, 2, 2], [3, 3, 3]
for i in l:
    for n in i:
        print(n, end=" ")
    print()
num = 0
for i in range(3):
    a = l[i]
    for j in range(3):
        b = a[j]
        if i == j:
            num += b
for i in range(2, -1, -1):
    c = l[i]
    for j in range(3):
        d = c[j]
        if abs(i-j) == 2:
            num += d
print(f"两条对角线元素之和为{num}")