# -*- coding:utf-8 -*-
"""
@author:壮壮Loschicos
@datetime:2020/11/7 16:54
@software: PyCharm
"""
# 导入numpy模块，并设置别称为np
import numpy as np
# # 显示numpy的版本号和配置文件
# ver = np.__version__
# print(ver)
# np.show_config()
# 创建一个大小为10的空向量
# shape 数组的维度，表示每个维度上的数组大小。
# np.empty 构造一个大小为 shape 的未初始化数组,
# np.zeros 构造一个大小为 shape 的全0数组,
# np.ones 构造一个大小为 shape 的全1数组,
# np.ones 构造一个大小为 shape 的全1数组,
# np.full 构造一个大小为 shape 的用指定值填满的数组,
print(np.empty(20))
print(np.zeros(10))
print(np.full(2, 3), 5.0)

