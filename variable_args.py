# 使用 *args 对可变数量的数字求和
def calculate_sum(*numbers):
    print(f"Arguments received as a tuple: {numbers}")
    total = sum(numbers)
    print(f"Sum: {total}\n")

# 使用 **kwargs 捕获额外的个人资料信息
def person_profile(name, age, **other_info):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Other Info: {other_info}\n")

# 调用函数
calculate_sum(1, 2, 3)
calculate_sum(10, 20, 30, 40, 50)

person_profile('Wang Wu', 26, gender="Male", job="Writer")
person_profile('Zhao Liu', 28, city="Beijing", status="Active")