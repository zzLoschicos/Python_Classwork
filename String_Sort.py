# -*- coding:utf-8 -*-
"""
@author:壮壮Loschicos
@datetime:2020/11/4 21:39
@software: PyCharm
"""
# 3、编写程序，要求输入一个字符串，然后将字符串中的所有字母全部后移一位，
# 最后一个字母移到字符串的开头，最后输出新的字符串。
arr = []
r = ""
m = input("请输入字符串：")
for string in m:
    arr.append(string)
last = arr[-1]
arr.insert(0, last)
arr.pop()
for str in arr:
    r = r + str
print(r)

