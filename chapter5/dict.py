# 字典的简单定义和使用
alice_0 = {"color": "green", "points": 5}

# print(alice_0["color"])
# print(alice_0["points"])

new_point = alice_0["points"]
print("you just earned " + str(new_point) + " points.")

# 添加键值对
alice_0["x_position"] = 0
alice_0["y_position"] = 25
print(alice_0)