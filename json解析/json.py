import json

# 从文件中读取json数据
dict = {}
with open('rootpath','r') as f:
    dict = json.load(f)


# 把对象写入json文件
with open("root_path", 'r') as f:
    json.dump(dict, f)

# json字符串转为对象
json_str = ""
dict1 = json.loads(json_str)

# 对象转为json字符串
str = json.dumps(dict1)
