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