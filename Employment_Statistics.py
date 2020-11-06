# -*- coding:utf-8 -*-
"""
@author:壮壮Loschicos
@datetime:2020/11/6 17:13
@software: PyCharm
"""
# 给定公司N名员工的工龄，要求按工龄增序输出每个工龄段有多少员工。
n = int(input())
data = list(map(int, input().split()))
del data[n:]
num = {}
for i in data:
    if i not in num:
        num[i] = 1
    else:
        num[i] += 1
for k, v in sorted(num.items()):
    print(str(k) + ":" + str(v))
