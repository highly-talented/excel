# # 内存：临时存储数据
# # 磁盘、U盘：永久存储数据
# # 文件三个步骤：打开文件、读写、关闭文件
# # 打开文件 open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
# # f = open(r"C:\python3\the_python大数据\venv\Scripts\b.txt","r")
# # print(f.tell())
# # f.seek(5) # seek(xx,0/1/2) 0 默认 1 当前指针位置 2 末尾
# # print(f.tell())
# # # 读写 r w在开头 = a 在末尾  加b 二进度文字和 + 在目前指针的位置读写
# # content = f.read() # f.read() f.readline()按行读 f.readlines()形成列表
# # # f.write("fsafds")
# # print(content)
# # #  关闭文件
# # f.close()
# # fromFile = open(r"C:\Users\yangxiu\Desktop\微信图片_20200223105358.jpg","rb")
# # fromContent = fromFile.read()
# # print(fromContent)
# # fromFile.close()
# # toFile = open(r"C:\Users\yangxiu\Desktop\微信图片_20200223105359.jpg","wb")
# # toContent = fromContent[0:len(fromContent)]
# # toFile.write(toContent)
# # toFile.close()
#
# # 文件遍历：for i in f 或者 foi i in f.readlines
# # 判断是否可读  f.readable
# # f.flush
import os
# # os.rename(r"C:\python3\the_python大数据\venv\Scripts\b.txt",r"C:\python3\the_python大数据\venv\Scripts\c.txt") # 可以修改文件名和文件夹名
# # os.renames(r"C:\python3\the_python大数据\venv\Scripts\b\c",r"C:\python3\the_python大数据\venv\Scripts\c\d") # 多级的树状的名称修改。
# os.remove()
# os.rmdir()
# os.removedirs()
# os.mkdir()
# os.chdir()
# source_File = open(r"C:\python3\the_python大数据\venv\Scripts\c.txt","r")
# dst_File = open(r"C:\python3\the_python大数据\venv\Scripts\e.txt","w")
# source_content = source_File.read()
# dst_File.write(source_content[0:len(source_content)])
# source_File.close()
# dst_File.close()

# source_File = open(r"C:\Users\yangxiu\Desktop\战疫206杨钰涵.png","rb")
# dst_File = open(r"C:\Users\yangxiu\Desktop\战疫206杨钰涵2.png","ab")
# while True:
#     source_content = source_File.read(1024)
#     if len(source_content) == 0 :
#         break
#     dst_File.write(source_content[0:len(source_content)])
# source_File.close()
# dst_File.close()

import os
import shutil
# os.chdir(r"C:\Users\yangxiu\Desktop\ceshi")
# file_list = os.listdir(r"C:\Users\yangxiu\Desktop\ceshi")
# for list_name in file_list:
#     list_name_local = list_name.rfind('.')
#     index_file_name = list_name[list_name_local+1:]
#     if not os.path.exists(index_file_name):
#         os.mkdir(index_file_name)
#     shutil.move(r"C:\Users\yangxiu\Desktop\ceshi\%s"%list_name,index_file_name)
# newfile_list = os.listdir(r"C:\Users\yangxiu\Desktop\ceshi")
# for newfile_name in newfile_list:
#     print(newfile_name,":")
#     lastfile_name = os.listdir(newfile_name)
#     print("\t",lastfile_name)

import os
import shutil
# def ListName(dir):
#     newfile_list = os.listdir(dir)
#     for newfile_name in newfile_list:
#         lastfile_name = dir + '/' + newfile_name
#         if os.path.isdir(lastfile_name):
#             print(newfile_name,':')
#             ListName(lastfile_name)
#         else:
#             print('\t',newfile_name)
#
# ListName(r"C:\Users\yangxiu\Desktop\ceshi")

import os
import shutil
def ListNameToFile(dir,file):
    newfile_list = os.listdir(dir)
    for newfile_name in newfile_list:
        lastfile_name = dir + '/' + newfile_name
        if os.path.isdir(lastfile_name):
            file.write(newfile_name + '：' + '\n')
            ListNameToFile(lastfile_name,file)
        else:
            file.write("\t" + newfile_name  + '\n')
    file.write('\n')
f = open(r"C:\Users\yangxiu\Desktop\ceshi\1.txt",'a')
ListNameToFile(r"C:\Users\yangxiu\Desktop\ceshi",f)