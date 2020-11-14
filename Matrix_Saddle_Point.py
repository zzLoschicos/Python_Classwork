# -*- coding:utf-8 -*-
"""
@author:壮壮Loschicos
@datetime:2020/11/14 20:29
@software: PyCharm
"""
"""
第5章-9 求矩阵鞍点的个数 (30分)
一个矩阵元素的“鞍点”是指该位置上的元素值在该行上最大、在该列上最小。
本题要求编写程序，求一个给定的n阶方阵的鞍点。
输入格式： 输入第一行给出一个正整数n（1≤n≤6）。随后n行，每行给出n个整数，其间以空格分隔。
输出格式： 鞍点的个数
"""
n = int(input())
s = list()
count = 0
for i in range(0, n):
    s.append(list(input().split()))
for i in s:
    a = max(i)
    for j in range(0, n):
        if a == i[j]:
            flag = 1
            for k in s:
                if a > k[j]:
                    flag = 0
                    break
            if flag == 1:
                count = count + 1
print(count)
