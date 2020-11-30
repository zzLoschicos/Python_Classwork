# Python_Classwork
## 练习题目
*  1、已知List1=[1,2,3,4,5,6],请通过不同的方法（2种方法）实现，使得List2=[6,5,4,3,2,1]。[Reverse_List.py](https://github.com/zzLoschicos/Python_Classwork/blob/main/Reverse_List.py)
*  2、给定任意奇数个整数，要求计算中间数（数值大小处于中间得数）并输出。[Middle_number.py](https://github.com/zzLoschicos/Python_Classwork/blob/main/Middle_number.py)
*  3、编写程序，要求输入一个字符串，然后将字符串中的所有字母全部后移一位，最后一个字母移到字符串的开头，最后输出新的字符串。[String_Sort.py](https://github.com/zzLoschicos/Python_Classwork/blob/main/String_Sort.py)
*  4、编写程序，删除列表中的所有素数。[RemovePrimeNumbers.py](https://github.com/zzLoschicos/Python_Classwork/blob/main/RemovePrimeNumbers.py)
*  5、求一个3×3矩阵的两条对角线元素之和（注意：两条对角线交叉点处的元素只计算一次。）[SumDiagonals.py](https://github.com/zzLoschicos/Python_Classwork/blob/main/SumDiagonals.py) 
## PAT 练习2
*  1、给定公司N名员工的工龄，要求按工龄增序输出每个工龄段有多少员工。[Employment_Statistics.py](https://github.com/zzLoschicos/Python_Classwork/blob/main/Employment_Statistics.py)
*  2、将一个3×3矩阵转置（即行和列互换）。[Matrix_Transpose.py](https://github.com/zzLoschicos/Python_Classwork/blob/main/Matrix_Transpose.py)
*  3、验证“哥德巴赫猜想”。[Goldbach's_Conjecture.py](https://github.com/zzLoschicos/Python_Classwork/blob/main/Goldbach's_Conjecture.py)
*  4、输入一个嵌套列表，再输入层数，求该层的数字元素个数。[Number_Elements.py](https://github.com/zzLoschicos/Python_Classwork/blob/main/Number_Elements.py)

## PTA练习（字典和集合）
*  1、输入一个1到7的数字，输出对应的星期名的缩写。[Week_Abbreviation.py](https://github.com/zzLoschicos/Python_Classwork/blob/main/Week_Abbreviation.py)
*  2、利用集合分析活动投票情况。第一小队有五名队员，序号是1,2,3,4,5;第二小队也有五名队员，序号6,7,8,9,10。输入一个得票字符串，求第二小队没有得票的队员。[Active_Voting.py](https://github.com/zzLoschicos/Python_Classwork/blob/main/Active_Voting.py)
*  3、求矩阵鞍点的个数一个矩阵元素的“鞍点”是指该位置上的元素值在该行上最大、在该列上最小。本题要求编写程序，求一个给定的n阶方阵的鞍点。[Matrix_Saddle_Point.py](https://github.com/zzLoschicos/Python_Classwork/blob/main/Matrix_Saddle_Point.py)
*  4、输入一个列表，去掉列表中重复的数字，按原来次序输出！[List_Iniq.py](https://github.com/zzLoschicos/Python_Classwork/blob/main/List_Iniq.py)
*  5、能被3,5和7整除的数的个数（用集合实现），求指定区间内能被3,5和7整除的数的个数[NumSet.py](https://github.com/zzLoschicos/Python_Classwork/blob/main/NumSet.py)

## PTA练习（函数）
*  1、 给定两个均不超过9的正整数a和n，要求编写函数fn(a,n) 求a+aa+aaa++⋯+aa⋯aa(n个a）之和，fn须返回的是数列和 [Def_A_Sum.py](https://github.com/zzLoschicos/Python_Classwork/blob/main/Def_A_Sum.py))
*  2、 使用函数求素数和prime(p), 其中函数prime当用户传入参数p为素数时返回True，否则返回False. PrimeSum(m,n),函数PrimeSum返回区间[m, n]内所有素数的和。[Def_Prime_Sum.py](https://github.com/zzLoschicos/Python_Classwork/blob/main/Def_Prime_Sum.py)
*  3、 本题要求实现一个统计整数中指定数字的个数的简单函数。CountDigit(number,digit )其中number是整数，digit为[1, 9]区间内的整数。函数CountDigit应返回number中digit出现的次数。[Def_Num_Count.py](https://github.com/zzLoschicos/Python_Classwork/blob/main/Def_Num_Count.py)
*  4、 使用函数输出指定范围内Fibonacci数的个数(用字典实现)[Def_Fibonacci_Count.py](https://github.com/zzLoschicos/Python_Classwork/blob/main/Def_Fibonacci_Count.py)
*  5、 缩写词是由一个短语中每个单词的第一个字母组成，均为大写。[Def_Acronym_Phrase.py](https://github.com/zzLoschicos/Python_Classwork/blob/main/Def_Acronym_Phrase.py)

## 数据结构_Python实现
### 排序
#### 冒泡排序
1、 实现冒泡排序,代码文件:[DS_Python/Sorts/Bubble_Sort.py](https://github.com/zzLoschicos/Python_Classwork/blob/main/DS_Python/Sorts/Bubble_Sort.py)
>冒泡排序  
0.如果遇到相等的值不进行交换，那这种排序方式是稳定的排序方式.  
    1.原理：比较两个相邻的元素，将值大的元素交换到右边  
    2.思路：依次比较相邻的两个数，将比较小的数放在前面，比较大的数放在后面。  
　  (1)第一次比较：首先比较第一和第二个数，将小数放在前面，将大数放在后面。  
    (2)比较第2和第3个数，将小数放在前面，大数放在后面。  
　　......  
　　(3)如此继续，知道比较到最后的两个数，将小数放在前面，大数放在后面，重复步骤，直至全部排序完成  
　　(4)在上面一趟比较完成后，最后一个数一定是数组中最大的一个数，所以在比较第二趟的时候，最后一个数是不参加比较的。  
　　(5)在第二趟比较完成后，倒数第二个数也一定是数组中倒数第二大数，所以在第三趟的比较中，最后两个数是不参与比较的。  
　　(6)依次类推，每一趟比较次数减少依次。  


2、 实现选择排序，代码文件：[DS_Python/Sorts/Selection_Sort.py](https://github.com/zzLoschicos/Python_Classwork/blob/main/DS_Python/Sorts/Selection_Sort.py)
> 选择排序（Selection sort）是一种简单直观的排序算法。  
它的工作原理是每一次从待排序的数据元素中选出最小（或最大）的一个元素，存放在序列的起始位置，所以称为：选择排序。  
1、原理  
　　设第一个元素为比较元素，依次和后面的元素比较，比较完所有元素找到最小的元素，将它和第一个元素互换  
　重复上述操作，我们找出第二小的元素和第二个位置的元素互换，以此类推找出剩余最小元素将它换到前面，即完成排序  
