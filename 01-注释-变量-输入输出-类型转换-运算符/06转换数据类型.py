"""
    int(x[,base]) 将x转换为一个整数
    float(x)      将x转换为一个浮点数
    str(x)      将对象x转换为字符串
    eval(str)   用来计算在字符串中的有效Python表达式，并返回一个对象
    tuple(s)    将序列s转换为一个元组
    list(s)     将序列s转换为一个列表
"""
# 接受用户输入
num = input("请输入数字：")
# 打印数据类型
print(type(num))  # <class 'str'>
# 打印转换后的数据类型
print(type(int(num)))  # <class 'int'>

# eval 将字符串中的数据转换成python表达式原本类型
str1 = "100"
str2 = "[1,2,3]"
str3 = "(1,2,3)"
print(type(eval(str1)))  # <class 'int'>
print(type(eval(str2)))  # <class 'list'>
print(type(eval(str3)))  # <class 'tuple'>
