# 初始化
# 1、有值的字典
alice_0 = {"color": "green", "points": 5}
# 2、空字典
alice_1 = {}

# 获取字典的值
print(alice_0["color"])

# 添加键值对
alice_0["x_position"] = 0
alice_0["y_position"] = 1

# 修改字典中的值
alice_0["x_position"] = 1
print(alice_0["x_position"])

# 删除键值对
del alice_0["x_position"]
del alice_0["y_position"]
print(alice_0)

# 使用字典代替对象
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}

print("Sarah's favorite language is " +
      favorite_languages["sarah"].title()
      + ".")