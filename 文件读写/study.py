'''
关于读取文件的四种方式
    1. f.read() 读取文件的所有内容 如果内容过大容易崩溃 可以 f.read(1024) 这样
    2. f.readline() 只读取文件的一行。可以用while控制全部读完
        line = f.readline()
        while line:
            line = f.readline()
    3. f.readlines() 一下全部读取完 并生成一个以换行符结尾的 list  可以通过for line in f.readlines() 进行遍历每一行的内容
    4. 直接用 for line in f： 读取遍历每一行的内容 固定 line

'''


from distutils import filelist
import imp
import os
import json
from tokenize import String


json_file = "/home/Gioures/Desktop/study/studuy.json"
json_str = {}

with open(json_file,'r') as f:
    json_str = json.load(f)

root_path = json_str['root']
old_name = json_str['old_name']
new_name = json_str['new_name']

# 返回所有文件路径列表
def findTheFiles():
    print(f"根目录 = {root_path}\n old_name = {old_name}\n new_name = {new_name}\n")
    filelist = []
    for root, dirs, files in os.walk(root_path):
        for dir in dirs:
            print(f'文件夹目录： -- {os.path.join(root,dir)}')
        for file in files:
            print(f'文件目录： -- {os.path.join(root,file)}')
            filelist.append(os.path.join(root,file))
    return filelist

def change(list):
    for file in list:
        content = ''
        with open(file,'r') as f:
            for line in f:
                if old_name in line:
                    line = line.replace(old_name,new_name)
                content += line
        with open(file,'w') as f:
            f.write(content)



if __name__ == '__main__':
    print('这里才是开始')
    list = findTheFiles()
    change(list)

