user_0 = {
    "username": "efermi",
    "first": "enrico",
    "last": "fermi",
}

# 遍历字典中的所有项
for key, value in user_0.items():
    print(key, ":", value)
print("-------------------------")

# 遍历字典中的key值
for key in user_0.keys():
    print(key)
print("-------------------------")

# 遍历字典中的value值
for value in user_0.values():
    print(value)
print("-------------------------")