# 简单计算器
c = "N"
while  c == "N":
    a = input('请输入一个数字： ')
    b = input('请再输入一个数字： ')
    if not (a.isdigit() and b.isdigit()):
        print('请输入数字')
        continue
    sum = a + b
    print('两个数字之各为 %s' %sum)
    c = input('是否退出(Y/N): ')
print('您已退出计算')