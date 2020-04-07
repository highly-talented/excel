#集合：
# for XX  in xxxx:
#     pass
# while xx:
#     pass
# 程序题：将“社会我杨哥，人狠话不多”反向打印出来
# notice = "社会我杨哥，人狠话不多"
# noticeNew = ""
# for name in notice:
#    noticeNew = name + noticeNew
# print(noticeNew)

# 程序题：打印1-100间的偶数
for i in range(1,101):
    if i % 2 == 0: # 判断是否是偶数
        print(i,end="\n")
print('以上是1-100间的偶数')

# break: 结束循环， coutinue：跳出本次循环
# break例子
# for i in range(1,10):
#     if i == 6:
#         break
#     print(i)
# # continue 例子
# for i in range(1,10):
#     if i == 6:
#         continue
#     print(i)