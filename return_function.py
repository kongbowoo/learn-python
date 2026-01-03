def add_numbers(a, b):
    """这个函数将两个数字相加并返回它们的和。"""
    sum_result = a + b
    return sum_result

# 调用函数并存储返回的值
total = add_numbers(5, 3)

# 打印返回的值
print(f"The sum is: {total}")

# 在另一个操作中使用返回的值
another_total = add_numbers(10, 20) * 2
print(f"Another calculated value: {another_total}")

def get_user_info():
    """这个函数以元组的形式返回用户信息。"""
    name = "labex"
    age = 25
    city = "Virtual City"
    return name, age, city

# 调用函数并将返回的元组解包（unpack）到单独的变量中
user_name, user_age, user_city = get_user_info()

# 打印解包后的值
print(f"Name: {user_name}, Age: {user_age}, City: {user_city}")