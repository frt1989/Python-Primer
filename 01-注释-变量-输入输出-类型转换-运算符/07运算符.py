"""
    算数运算符
        +-*/
        // 整除
        %
        ** 指数 2**4 输出14
        ()
        优先级：() > ** > % // / * > + -
    赋值运算符
        =
    复合赋值运算符
        += -= *= /= //= %= **=
    比较运算符
        == != > < >= <=
    逻辑运算符
        and x and y 如果x为False，返回False，否则返回y的值
        or x or y 如果x为True，返回True，否则返回y的值
        not not x 如果x为True，返回False，如果x为False，返回True
"""
print(9 / 2)  # 4.5
print(9 // 2)  # 4

# 赋值
num = 1
print(num)

num1, float1, str1 = 1, 1.2, "abc"
print(num1)  # 1
print(float1)  # 1.2
print(str1)  # abc

num1 = float1 = str1 = "bcd"
print(num1)  # bcd
print(float1)  # bcd
print(str1)  # bcd
# 复合赋值
c = 100
c += 3 + 100
print(c)  # 203 ,先计算 3+100 c += 103
# 逻辑运算符 数字之间的逻辑运算
a = 0
b = 2
c = 3
# and运算符，只要有一个值为0，则结果为0，否则结果为最后一个非0数字
print(a and c)  # 0
print(b and c)  # 3
# or运算，只有所有值为0，结果才为0，否则结果为第一个非0数字
print(a or b)  # 2
print(b or c)  # 2
