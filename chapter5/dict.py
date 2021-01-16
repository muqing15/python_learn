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

alice_1 = {}
alice_1["color"] = "red"
alice_1["points"] = 10
# print(alice_1)

# 修改value
print("the color of alice is: " + alice_0["color"])
alice_0["color"] = "yellow"
print("the color of alice is: " + alice_0["color"])

# 创建一个value为字典的字段
# alices = {}
# alices["alice_0"] = alice_0
# alices["alice_1"] = alice_1
# for alice_name in alices:
#     print("the info of", alice_name, "is", alices[alice_name])