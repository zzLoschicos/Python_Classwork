# -*- coding:utf-8 -*-
"""
@author:壮壮Loschicos
@datetime:2020/11/4 21:16
@software: PyCharm
"""
# 1、已知List1=[1,2,3,4,5,6],请通过不同的方法（2种方法）实现，使得List2=[6,5,4,3,2,1]
list1 = [1, 2, 3, 4, 5, 6]
list2 = list1[::-1]
print(list2)
# list1 = [1, 2, 3, 4, 5, 6]
list3 = []
for i in range(5, -1, -1):
    #     print(list1[i])
    list3.append(list1[i])
print(list3)
