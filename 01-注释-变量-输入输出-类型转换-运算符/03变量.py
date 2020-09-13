"""
    变量 = 值

    标识符：
        由数字、字母、下划线组成
        不能数字开头
        不能使用内置关键字
        严格区分大小写

    Debug

    数据类型
        数值：int float
        布尔型：True、False
        字符串：str
        列表：list
        元组：tuple
        集合：set
        字典：dict

    检测数据类型：
        type()
"""
a = 1
print(type(a))  # <class 'int'>
b = 1.1
print(type(b))  # <class 'float'>

c = True
print(type(c))  # <class 'bool'>

d = "HelloWorld"
print(type(d))  # <class 'str'>

e = [1, 2, 3]
print(type(e))  # <class 'list'>

f = (1, 2, 3)
print(type(f))  # <class 'tuple'>

g = {1, 2, 3}
print(type(g))  # <class 'set'>

h = {1: 'a', 2: "abc"}
print(type(h))  # <class 'dict'>
