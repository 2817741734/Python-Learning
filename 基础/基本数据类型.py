# 标准数据类型
"""
Python3 中有六个标准的数据类型：

Number（数字）
String（字符串）
List（列表）
Tuple（元组）
Set（集合）
Dictionary（字典）
Python3 的六个标准数据类型中：

不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。

"""


# 变量赋值
"""
Python 中的变量不需要声明。每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。
在 Python 中，变量就是变量，它没有类型，我们所说的"类型"是变量所指的内存中对象的类型。
等号（=）用来给变量赋值。
等号（=）运算符左边是一个变量名,等号（=）运算符右边是存储在变量中的值。
"""
counter = 100  # 整型变量
miles = 1000.0  # 浮点型变量
name = "runoob"  # 字符串
print(counter)
print(miles)
print(name)


# 多个变量赋值
"""
Python允许你同时为多个变量赋值
"""
a1 = b1 = c1 = 1  # 创建一个整型对象，值为 1，从后向前赋值，三个变量被赋予相同的数值。
a2, b2, c2 = 1, 2, "runoob"  # 两个整型对象 1 和 2 的分配给变量 a 和 b，字符串对象 "runoob" 分配给变量 c，为多个对象指定多个变量。


# Number（数字）
"""
Python3 支持 int、float、bool、complex（复数）。
在Python 3里，只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。
像大多数语言一样，数值类型的赋值和计算都是很直观的。
内置的 type() 函数可以用来查询变量所指的对象类型。
"""
