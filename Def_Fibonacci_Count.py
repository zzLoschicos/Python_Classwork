# -*- coding:utf-8 -*-
"""
@author:壮壮Loschicos
@contact: 13210707427@163.com
@datetime:2020/11/26 21:39
@software: PyCharm
"""
"""
第6章函数-4 使用函数输出指定范围内Fibonacci数的个数 (20分)
本题要求实现一个计算Fibonacci数的简单函数，并利用其实现另一个函数,
输出两正整数m和n（0<m<n≤100000）之间的所有Fibonacci数的数目。 
所谓Fibonacci数列就是满足任一项数字是前两项的和（最开始两项均定义为1）的数列,
fib(0)=fib(1)=1。其中函数fib(n)须返回第n项Fibonacci数；
函数PrintFN(m,n)用列表返回[m, n]中的所有Fibonacci数。

函数接口定义：
在这里描述函数接口。例如：
fib(n),返回fib(n)的值
PrintFN(m,n)，用列表返回[m, n]中的所有Fibonacci数。

1 1 2 3 5 8 
"""


def fib(n):
    f = {0: 1, 1: 1}  # 创建一个字典
    if n in f:  # 判断输入的n值是否在字典f内
        return f[n]  # 返回字典的值
    else:
        m = fib(n - 1) + fib(n - 2)  # 如果不在字典内，则计算ｎ-1 和 n-2 的fib值  并相加
        f[n] = m  # 将f[n]的值赋给 m
        return m  # 返回m


def PrintFN(m, n):
    lst = []
    i = 0
    while fib(i) <= n:  # 判断fib(i)的值 是否满足 小于n
        if fib(i) >= m:  # 如果fib(i)的值 大于m
            lst.append(fib(i))  # 则将fib(i)的值加到列表中
        i += 1  # 对i + 1
    return lst  # 返回列表


if __name__ == '__main__':
    m, n, i = input().split()
    n = int(n)
    m = int(m)
    i = int(i)
    b = fib(i)
    print("fib({0}) = {1}".format(i, b))
    fiblist = PrintFN(m, n)
    print(len(fiblist))
