# 99 乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print("%d * %d = %d  "%(i,j,i*j),end="",)
#     print(end = "\n")

# 水仙花案例：
sxh = input("请输入一个数：")
sum = 0
for i in sxh:
    print(i)
    sum = sum + int(i)**3
if sum == int(sxh):
    print('%d 是水仙数'% int(sxh))
else:
    print('%d 不是水仙数' % int(sxh))

