"""
while 循环语句

形式：
while <expr>:
    <statement(s)>
else:
    <additional_statement(s)>

形式解析：
expr 条件语句
如果为 true，则执行 statement(s) 语句块
如果为 false，则执行 additional_statement(s)

注：
break 语句可以跳出 for 和 while 的循环体。如果你从 for 或 while 循环中终止，任何对应的循环 else 块将不执行。
continue 语句被用来告诉 Python 跳过当前循环块中的剩余语句，然后继续进行下一轮循环。

循环语句的 else 子句，它在穷尽列表(以for循环)或条件变为 false (以while循环)导致循环终止时被执行，但循环被 break 终止时不执行。

"""

# while 语句
# 计算 1 到 100 的总和：
n = 100
Sum = 0
counter = 1
while counter <= n:
    Sum = Sum + counter
    counter += 1
print("1 到 %d 之和为: %d" % (n, Sum))

# 设置条件表达式永远不为 false 来实现无限循环:
# 无限循环在服务器上客户端的实时请求非常有用
var = 1
while var == 1:  # 表达式永远为 true
    num = int(input("输入一个数字  :"))
    print("你输入的数字是: ", num)
    if num == 999:  # 设置退出循环
        var = 0
print("Good bye!")

# while 循环使用 else 语句
# 例：循环输出数字，并判断大小：
count = 0
while count < 5:
    print(count, " 小于 5")
    count = count + 1
else:
    print(count, " 大于或等于 5")

# 简单语句组：
# 如果所写的while循环体中只有一条语句，可以写在同一行中：
flag: int = 1
# while flag: print('欢迎访问菜鸟教程!')
