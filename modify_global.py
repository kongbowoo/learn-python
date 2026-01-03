# 全局变量
counter = 0

def increment_counter():
    # 声明我们打算修改全局 counter
    global counter
    counter += 1
    print(f"Inside function: counter is {counter}")

# 打印初始值
print(f"Before calling function: counter is {counter}")

# 调用函数以修改全局变量
increment_counter()

# 打印函数调用后的值
print(f"After calling function: counter is {counter}")

def increment_counter_local():
    # 此赋值创建了一个名为 'counter' 的新局部变量
    counter = 100
    print(f"\nInside function (local): counter is {counter}")

# 在测试前打印全局 counter 的值
print(f"Before calling function (local test): counter is {counter}")

# 调用函数
increment_counter_local()

# 全局 counter 的值不受影响
print(f"After calling function (local test): counter is {counter}")