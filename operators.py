# Arithmetic Operators
a = 21
b = 5
print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b}') # 标准除法
print(f'{a} // {b} = {a // b}')  # 整除，向下取整到最近的整数
print(f'{a} % {b} = {a % b}')  # 取模，返回余数
print(f'{a} ** {b} = {a ** b}')  # 幂运算，a 的 b 次方

# Comparison Operators
print("\n--- Comparison Operators ---")
a = 6
b = 5
print(f'{a} == {b} is {a == b}')  # 等于
print(f'{a} != {b} is {a != b}')  # 不等于
print(f'{a} > {b} is {a > b}')    # 大于
print(f'{a} < {b} is {a < b}')    # 小于
print(f'{a} >= {b} is {a >= b}')  # 大于或等于
print(f'{a} <= {b} is {a <= b}')  # 小于或等于

# Assignment Operators
print("\n--- Assignment Operators ---")
a = 10
b = 3
print(f'Initial a: {a}')

c = a
c += b  # 等同于 c = c + b
print(f'a += b: {c}')

c = a
c -= b  # 等同于 c = c - b
print(f'a -= b: {c}')

c = a
c *= b  # 等同于 c = c * b
print(f'a *= b: {c}')

c = a
c /= b  # 等同于 c = c / b
print(f'a /= b: {c}')

# 海象运算符 (Walrus operator, Python 3.8+)
# 它在更大的表达式的一部分中将一个值赋给一个变量。
print("\n--- Walrus Operator ---")
text = 'hello python'
if (n := len(text)) > 10:
    print(f'The string is long enough ({n} characters)')

# Logical Operators
print("\n--- Logical Operators ---")
x = True
y = False

print(f'{x} and {y} is {x and y}')
print(f'{x} or {y} is {x or y}')
print(f'not {x} is {not x}')

# 使用非布尔值的求值
a = 10  # True
b = 0   # False
print(f'{a} and {b} returns {a and b}') # 返回第一个 Falsy 值或最后一个 Truthy 值
print(f'{a} or {b} returns {a or b}')   # 返回第一个 Truthy 值或最后一个 Falsy 值

# Bitwise Operators
print("\n--- Bitwise Operators ---")
a = 5  # Binary: 0b101
b = 9  # Binary: 0b1001
print(f'Binary of {a} is {bin(a)}')
print(f'Binary of {b} is {bin(b)}')

# 为了清晰起见，我们用 4 位来对齐它们：
# a = 0101
# b = 1001

# 位与 (&): 如果两个位都是 1，则结果位设置为 1。
# 0101 & 1001 = 0001 (十进制 1)
print(f'{a} & {b} = {a & b}')

# 位或 (|): 如果两个位中有一个是 1，则结果位设置为 1。
# 0101 | 1001 = 1101 (十进制 13)
print(f'{a} | {b} = {a | b}')

# 位异或 (^): 如果只有两个位中有一个是 1，则结果位设置为 1。
# 0101 ^ 1001 = 1100 (十进制 12)
print(f'{a} ^ {b} = {a ^ b}')

# 位非 (~): 反转所有位。
# ~a 等同于 -(a+1)
print(f'~{a} = {~a}')

# 左移 (<<): 将位向左移动，右侧用零填充。
# 等同于乘以 2**n。
# 5 << 2 表示 0101 变为 10100 (十进制 20)
print(f'{a} << 2 = {a << 2}')

# 右移 (>>): 将位向右移动，丢弃右侧的位。
# 等同于进行 2**n 的整除。
# 9 >> 2 表示 1001 变为 10 (十进制 2)
print(f'{b} >> 2 = {b >> 2}')

# Membership Operators
print("\n--- Membership Operators ---")
my_list = [1, 3, 5, 7]
print(f'3 in {my_list} is {3 in my_list}')
print(f'4 not in {my_list} is {4 not in my_list}')

greeting = "hello world"
print(f'"world" in "{greeting}" is {"world" in greeting}')

# Identity Operators
print("\n--- Identity Operators ---")

# 对于小整数，Python 通常会重用同一个对象。
x = 256
y = 256
print(f'x is y (for 256): {x is y}') # 这通常是 True

# 对于较大的整数，Python 可能会创建单独的对象。
a = 257
b = 257
print(f'a is b (for 257): {a is b}') # 这通常是 False

# 对于像列表（list）这样的可变对象（mutable objects），即使它们的内容相同，它们也是不同的对象。
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(f'list1 == list2: {list1 == list2}') # 检查内容是否相等 (True)
print(f'list1 is list2: {list1 is list2}') # 检查是否是同一个对象 (False)
print(f'list1 is not list2: {list1 is not list2}') # 检查是否是不同的对象 (True)