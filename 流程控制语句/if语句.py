"""
if 条件语句
通过一条或多条语句的执行结果（True 或者 False）来决定执行的代码块

关键字：
if – elif – else

形式：
if condition_1:
    statement_block_1
elif condition_2:
    statement_block_2
else:
    statement_block_3

形式执行解析：
如果 "condition_1" 为 True 将执行 "statement_block_1" 块语句
如果 "condition_1" 为False，将判断 "condition_2"
如果"condition_2" 为 True 将执行 "statement_block_2" 块语句
如果 "condition_2" 为False，将执行"statement_block_3"块语句

"""

x = int(input("Please enter an integer: "))
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')
