#creat a list of fruits
# 创建一个包含一些水果的列表
fruits = ["apple", "banana", "cherry"]

# 访问列表中的元素
print(fruits[0])  # 输出: apple
print(fruits[1])  # 输出: banana

# 修改列表中的元素
fruits[1] = "blueberry"
print(fruits)  # 输出: ['apple', 'blueberry', 'cherry']

# 添加元素到列表
fruits.append("orange")
print(fruits)  # 输出: ['apple', 'blueberry', 'cherry', 'orange']

# 删除列表中的元素
fruits.remove("cherry")
print(fruits)  # 输出: ['apple', 'blueberry', 'orange']

# 删除并返回最后一个水果
last_fruit = fruits.pop()
print(last_fruit)  # 输出: orange
print(fruits)  # 输出: ['apple', 'blueberry']


#creating a dictionary
