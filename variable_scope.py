# 全局变量
global_variable = "I am a global variable"

def my_function():
    # 局部变量
    local_variable = "I am a local variable"
    print(f"Inside the function:")
    print(f"  Accessing global_variable: {global_variable}")
    print(f"  Accessing local_variable: {local_variable}")

# 调用函数
my_function()

# 尝试在函数外部访问变量
print(f"\nOutside the function:")
print(f"  Accessing global_variable: {global_variable}")

# 尝试在这里访问 local_variable 会导致 NameError
# print(f"  Accessing local_variable: {local_variable}")

# 全局变量
my_variable = "I am the global version"

def another_function():
    # 这个局部变量遮蔽了全局变量
    my_variable = "I am the local version"
    print(f"\nInside another_function(): {my_variable}")

# 调用函数
another_function()

# 全局变量保持不变
print(f"Outside another_function(): {my_variable}")