"""
函数

定义规则：
函数代码块以 def 关键词开头，后接函数标识符名称和圆括号 ()。
任何传入参数和自变量必须放在圆括号中间，圆括号之间可以用于定义参数。
函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
函数内容以冒号 : 起始，并且缩进。
return [表达式] 结束函数，选择性地返回一个值给调用方，不带表达式的 return 相当于返回 None。

语法格式：
def 函数名（参数列表）:
    函数体

调用函数时可使用的正式参数类型：
必需参数
关键字参数
默认参数
不定长参数

"""


# 简单打印
def hello():
    print("Hello World!")


hello()


# 比较两个数，并返回较大的数
def maxd(a, b):
    if a > b:
        return a
    else:
        return b


a = 4
b = 5
print(maxd(a, b))


# 计算面积函数
def area(width, height):
    return width * height


def print_welcome(name):
    print("Welcome", name)


print_welcome("Yubo")
w = 4
h = 5
print("width =", w, " height =", h, " area =", area(w, h))


# python 传不可变对象实例（类似 C++ 的值传递）
def change(a):
    # print(id(a))  # 指向的是同一个对象
    a = 10
    # print(id(a))  # 一个新对象


a = 1
# print(id(a))
change(a)


# python 传可变对象实例（类似 C++ 的引用传递）
def changeme(mylist):
    """修改传入的列表"""
    mylist.append([1, 2, 3, 4])
    print("函数内取值: ", mylist)
    return


# 调用changeme函数
mylist = [10, 20, 30]
changeme(mylist)
print("函数外取值: ", mylist)


# 调用函数时参数：必需参数
# 必需参数须以正确的顺序传入函数。调用时的数量必须和声明时的一样。
# 可写函数说明
def printme(str):
    "打印任何传入的字符串"
    print(str)
    return
# 调用 printme 函数，不加参数会报错
printme(str)


# 调用函数时参数：关键字参数
# 关键字参数和函数调用关系紧密，函数调用使用关键字参数来确定传入的参数值。
# 使用关键字参数允许函数调用时参数的顺序与声明时不一致，因为 Python 解释器能够用参数名匹配参数值。
# 以下实例中演示了函数参数的使用不需要使用指定顺序：
# 可写函数说明
def printinfo(name, age):
    "打印任何传入的字符串"
    print("名字: ", name)
    print("年龄: ", age)
    return
# 调用printinfo函数
printinfo(age=50, name="runoob")


# 调用函数时参数：默认参数
# 调用函数时，如果没有传递参数，则会使用默认参数。
# 以下实例中如果没有传入 age 参数，则使用默认值：
# 可写函数说明
def printinfo(name, age=35):
    "打印任何传入的字符串"
    print("名字: ", name)
    print("年龄: ", age)
    return
# 调用printinfo函数
printinfo(age=50, name="runoob")
print("------------------------")
printinfo(name="runoob")


# 调用函数时参数：不定长参数
"""
需要一个函数能处理比当初声明时更多的参数，这些参数叫做不定长参数
和上述 2 种参数不同，声明时不会命名。基本语法如下：
def functionname([formal_args,] *var_args_tuple ):
   "函数_文档字符串"
   function_suite
   return [expression]
"""
# 加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数
# 可写函数说明
def printinfo(arg1, *vartuple):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    print(vartuple)  # 加了星号 * 的参数会以元组(tuple)的形式导入
# 调用printinfo 函数
printinfo(70, 60, 50, 40)

# 如果在函数调用时没有指定参数，它就是一个空元组。
# 可以不向函数传递未命名的变量。如下实例：
# 可写函数说明
def printinfo(arg1, *vartuple):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    for var in vartuple:
        print(var)
    return
# 调用printinfo 函数
printinfo(10)  # 传入空元组
printinfo(70, 60, 50)


"""
还有一种就是参数带两个星号 ** ，参数会以字典的形式导入
基本语法如下：
def functionname([formal_args,] **var_args_dict ):
   "函数_文档字符串"
   function_suite
   return [expression]
"""
# 加了两个星号 ** 的参数会以字典的形式导入：
# 可写函数说明
def printinfo(arg1, **vardict):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    print(vardict)
# 调用printinfo 函数
printinfo(1, a=2, b=3)

# 声明函数时，参数中星号 * 可以单独出现，例如：
def f(a,b,*,c):
    return a+b+c
# 如果单独出现星号 *，则星号 * 后的参数必须用关键字传入：
# f(1,2,3) 报错
f(1, 2, c=3)  # 正常


"""
Python 使用 lambda 来创建匿名函数。
lambda 只是一个表达式，函数体比 def 简单很多。
lambda 的主体是一个表达式，而不是一个代码块。仅仅能在 lambda 表达式中封装有限的逻辑进去。
lambda 函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数。
虽然 lambda 函数看起来只能写一行，却不等同于 C 或 C++ 的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。

lambda 函数语法：
lambda [arg1 [,arg2,.....argn]]:expression

"""
# 设置参数a加上10：
x = lambda a : a + 10
print(x(5))

# 设置两个参数：
# 可写函数说明
sum = lambda arg1, arg2: arg1 + arg2
# 调用sum函数
print("相加后的值为 : ", sum(10, 20))
print("相加后的值为 : ", sum(20, 20))

# 我们可以将匿名函数封装在一个函数内，这样可以使用同样的代码来创建多个匿名函数。
# 以下实例将匿名函数封装在 myfunc 函数中，通过传入不同的参数来创建不同的匿名函数：
def myfunc(n):
    return lambda a: a * n
mydoubler = myfunc(2)
mytripler = myfunc(3)
print(mydoubler(11))
print(mytripler(11))

"""
return 语句
return [表达式] 语句用于退出函数，选择性地向调用方返回一个表达式。
不带参数值的 return 语句返回 None
"""
# 以下实例演示了 return 语句的用法：
# 可写函数说明
def sum(arg1, arg2):
    # 返回2个参数的和."
    total = arg1 + arg2
    print("函数内 : ", total)
    return total
# 调用sum函数
total = sum(10, 20)
print("函数外 : ", total)

"""
强制位置参数
Python3.8 新增了一个函数形参语法 / 用来指明函数形参必须使用指定位置参数，不能使用关键字参数的形式。
在以下的例子中：
形参 a 和 b 必须使用指定位置参数
c 或 d 可以是位置形参或关键字形参
e 和 f 要求为关键字形参

def f(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)
"""
def f(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)
# f(10, b=20, c=30, d=40, e=50, f=60)  # 报错 b 不能使用关键字参数的形式
# f(10, 20, 30, 40, 50, f=60)  # 报错 e 必须使用关键字参数的形式
f(10, 20, 30, d=40, e=50, f=60)
