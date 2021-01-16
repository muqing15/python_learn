speed = ("slow", "medium", "high")
alice_0 = {"x_position": 0, "y_position": 25, "speed": "medium"}

if alice_0["speed"] == speed[0]:
    x_icrement = 1
elif alice_0["speed"] == speed[1]:
    x_icrement = 2
else:
    x_icrement = 3
alice_0["x_position"] = alice_0["x_position"] + x_icrement
print("the position of alice is:\n\tx: " + str(alice_0["x_position"]) + "\n\ty: " +
      str(alice_0["y_position"]))