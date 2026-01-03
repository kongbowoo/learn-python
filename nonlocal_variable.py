def outer_function():
    outer_variable = "I am in the outer function"

    def inner_function():
        # 声明我们正在修改来自包围作用域（enclosing scope）的变量
        nonlocal outer_variable
        outer_variable = "I have been modified by the inner function"
        print(f"Inside inner_function(): {outer_variable}")

    print(f"Before calling inner_function(): {outer_variable}")
    inner_function()
    print(f"After calling inner_function(): {outer_variable}")

# 调用外部函数
outer_function()

def outer_function_local_test():
    outer_variable = "I am in the outer function (local test)"

    def inner_function_local_test():
        # 此赋值创建了一个新的局部变量
        outer_variable = "I am a local variable in inner_function"
        print(f"\nInside inner_function_local_test(): {outer_variable}")

    print(f"\nBefore calling inner_function_local_test(): {outer_variable}")
    inner_function_local_test()
    print(f"After calling inner_function_local_test(): {outer_variable}")

# 调用外部函数进行局部测试
outer_function_local_test()