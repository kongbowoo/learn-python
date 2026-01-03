def person(name, age):
    print(f"{name} is {age} years old.")

# 这是位置实参和关键字实参的有效混合
person("Wang Wu", age=26)

# 这将导致一个 SyntaxError: positional argument follows keyword argument
# person(age=28, "Zhao Liu")