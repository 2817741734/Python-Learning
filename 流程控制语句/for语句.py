"""
for 语句
Python中 for 循环可以遍历任何可迭代对象，如一个列表或者一个字符串

形式：
for <variable> in <sequence>:
    <statements>
else:
    <statements>

注：
break 语句可以跳出 for 和 while 的循环体。如果你从 for 或 while 循环中终止，任何对应的循环 else 块将不执行。
continue 语句被用来告诉 Python 跳过当前循环块中的剩余语句，然后继续进行下一轮循环。

循环语句的 else 子句，它在穷尽列表(以for循环)或条件变为 false (以while循环)导致循环终止时被执行，但循环被 break 终止时不执行。

"""

# for 语句
languages = ["C", "C++", "Perl", "Python"]
for x in languages:
    print(x)

# 在 for 语句中使用 break 与 continue 语句
sites = ["Baidu", "Google", "Apple", "Taobao"]
for site in sites:
    if site == "Apple":
        print("Apple 找到啦！")
        # break
        # continue
    print(f"{site} 不是目标")
else:
    print("没有循环数据了!")
print("结束")


