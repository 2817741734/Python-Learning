"""
range()函数
用于生成一个等差级数链表

在不同方面 range() 函数返回的对象表现为它是一个列表，但事实上它并不是
当你迭代它时，它是一个能够像期望的序列返回连续项的对象
但为了节省空间，它并不真正构造列表

我们称此类对象是 可迭代的，即适合作为那些期望从某些东西中获得连续项直到结束的函数或结构的一个目标（参数）
迭代器：
1. for 语句
2. list() 函数 (它从可迭代（对象）中创建列表)

"""

# 所生成的链表中不包括范围中的结束值
for i in range(5):
    print(i)
print("over")

# range() 操作自定义数值范围
for i in range(5, 10):
    print(i)
print("over")

# range() 操作可以指定一个不同的步进值/步长（可以是负数）
for i in range(0, 10, 3):  # 步长为3
    print(i)
print("over")

for i in range(-10, -100, -30):  # 步长为-30
    print(i)
print("over")

# 直接打印很奇怪
print(range(10))
print("over")

# 结合使用 range() 和 len()，迭代链表索引
a1 = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a1)):
    print(i, a1[i])
print("over")
# 此功能也可以使用enumerate()实现
for i, item in enumerate(a1):
    print(i, item)
print("over")

# 使用 list() 函数 从可迭代（对象）中创建列表：
a2 = list(range(5))
print(a2)
