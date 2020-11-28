# -*- coding:utf-8 -*-
"""
@author:壮壮Loschicos
@contact: 13210707427@163.com
@datetime:2020/11/25 10:27
@software: PyCharm
"""
"""
第6章函数-2 使用函数求素数和 (20分)
使用函数求素数和
prime(p), 其中函数prime当用户传入参数p为素数时返回True，
否则返回False. PrimeSum(m,n),函数PrimeSum返回区间[m, n]内所有素数的和。
题目保证用户传入的参数1<=m<n。
函数接口定义：
在这里描述函数接口：
prime(p)，返回True表示p是素数，返回False表示p不是素数
PrimeSum(m,n)，函数返回素数和
"""
import math


def prime(p):
    if p == 1:
        return False
    isPrime = True
    for i in range(2, int(math.sqrt(p))+1):
        if p % i == 0:
            isPrime = False
            break

    return isPrime


def PrimeSum(m, n):
    result = 0
    for num in range(m, n + 1):
        if prime(num) == True:
            result += num
    return result


if __name__ == '__main__':
    m, n = input().split()
    m = int(m)
    n = int(n)
    print(PrimeSum(m, n))
