# 字典

## 1、定义和访问

字典的本质是由任意多个键值对组成，使用大括号包裹。每个键值对用`k:v`表示，之间使用逗号`,`隔开

* 主键是字符串
* 值可以是数字，字符串列表甚至还可以是字典

```python
alice_0 = {"color":"green", "points":5}

# 使用字典名称["key"]的方式访问字典内key所对应的value
print(alice_0["color"])
print(alice_0["points"])
```

## 2、添加

字典是一种动态结构，可以在其中随时添加

