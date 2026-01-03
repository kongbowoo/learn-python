def school_info(name, /, standard_param, *, city):
    print(f'Positional-Only (name): {name}')
    print(f'Standard (standard_param): {standard_param}')
    print(f'Keyword-Only (city): {city}')
    print('---')

# 在此函数中：
# - `name` 必须按位置传递。
# - `standard_param` 可以按位置或关键字传递。
# - `city` 必须按关键字传递。

# 有效的调用
school_info("Peking University", "PKU", city="Beijing")
school_info("Tsinghua University", standard_param="THU", city="Beijing")

# 无效的调用示例（已注释以防止错误）
# school_info(name="Zhejiang University", "ZJU", city="Hangzhou")  # TypeError: name is positional-only
# school_info("Fudan University", "FDU", "Shanghai")               # TypeError: city is keyword-only