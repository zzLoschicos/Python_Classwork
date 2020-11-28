# -*- coding:utf-8 -*-
"""
@author:壮壮Loschicos
@contact: 13210707427@163.com
@datetime:2020/11/25 10:10
@software: PyCharm
"""
"""
第6章函数-1 使用函数求特殊a串数列和 (10分)
给定两个均不超过9的正整数a和n，要求编写函数fn(a,n) 求a+aa+aaa++⋯+aa⋯aa(n个a）之和，fn须返回的是数列和
函数接口定义：
fn(a,n)
其中 a 和 n 都是用户传入的参数。 a 的值在[1, 9]范围；n 是[1, 9]区间内的个位数。函数须返回级数和
a + aa +aaa + aaaa

a = 2 n = 3   2 + 22 + 222 i range(0, 3)
i = 0  10 ** i  = 1    sum = 0     sum = sum + a = a = 2
i = 1  10 ** 1  = 10   sum = 2     sum = sum * 10 + a = 20 + a = 22 
i = 2  10 ** 2  = 100  sum = 22    sum = sum * 10  + a = 22*10+a = 220+2 = 222

"""
def fn(a, n):
    sum = 0
    s = 0
    for i in range(0, n):
        s = s * 10 + a
        sum += s
    return sum


if __name__ == '__main__':
    a, b = input().split()
    s = fn(int(a), int(b))
    print(s)
