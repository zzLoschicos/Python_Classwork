# -*- coding:utf-8 -*-
"""
@author:壮壮Loschicos
@datetime:2020/11/14 20:19
@software: PyCharm
"""
"""
第5章-8 能被3,5和7整除的数的个数（用集合实现）
求指定区间内能被3,5和7整除的数的个数
"""
a, b = map(int, input().split())
s = set()
for i in range(a, b + 1):
    if i % 3 == 0 and i % 5 == 0 and i % 7 == 0:
        s.add(i)
print(len(s))
