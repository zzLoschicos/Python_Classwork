# -*- coding:utf-8 -*-
"""
@author:壮壮Loschicos
@datetime:2020/11/14 20:15
@software: PyCharm
"""
"""
第5章-7 列表去重 
输入一个列表，去掉列表中重复的数字，按原来次序输出！
"""
lst = input()
lst = lst.replace('[', '')
lst = lst.replace(']', '')
lst = lst.replace(' ', '')
lst = lst.split(',')
res = list(set(lst))
res.sort(key=lst.index)
print(" ".join(res))
