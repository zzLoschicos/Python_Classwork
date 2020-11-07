# -*- coding:utf-8 -*-
"""
@author:壮壮Loschicos
@datetime:2020/11/7 10:35
@software: PyCharm
"""
# 使用numpy生成数组，得到ndarray的类型
# ndarray :N-dimensional array  N维数组
# ndarray它是一系列同类型数据的集合，每个元素在内存中都有相同存储大小的区域，以 0 下标为开始进行集合中元素的索引

import numpy as np
import random

t1 = np.array([1, 2, 3])
print(t1)
print(type(t1))

t2 = np.array(range(10))
print(t2)
print(t2.dtype)

t3 = np.arange(4, 10, 2)
print(t3)
print(t3.dtype)
print("*" * 20)

# numpy中的数据类型
t4 = np.array(range(1, 4), dtype="float32")
print(t4)
print(t4.dtype)

t5 = np.array([1, 1, 0, 1, 0, 0], dtype=bool)
print(t5)
print(t5.dtype)

t6 = t5.astype("int8")
print(t6)
print(t6.dtype)

# numpy中的小数
t7 = np.array([random.random() for i in range(10)])
print(t7)
print(t7.dtype)

t8 = np.round(t7, 2)
print(t8)

