import json

# 读取 JSON 文件
with open('students.json', 'r') as file:
    data = json.load(file)

# 访问学生列表
students = data["students"]

# 遍历学生列表
for student in students:
    print(f"ID: {student['id']}")
    print(f"Name: {student['name']}")
    print(f"Age: {student['age']}")
    print(f"Grades: {student['grades']}")
    print()  # 空行分隔每个学生的信息