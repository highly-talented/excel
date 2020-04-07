import random
corret = random.randint(1,100)
print(corret)
count = 0
while True:
    count += 1
    guess = int(input('请猜一个数字： '))
    if guess > corret:  # 处理数字
        print('你猜大了')
    elif guess == corret:
        break
    else:
        print('你猜小了')

print('恭喜您，猜了%d次，数字是%d，您猜对了'%(count,guess))
