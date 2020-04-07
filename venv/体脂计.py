# 功能分析：
# 1. 输入数据：身高、体得、年龄、性别
# 2. 处理数据：计算体脂计算
# 3. 输出：告诉用户是事正常
#  使用注释，把思绪理
# 输入数据
# personHeight  = float(input('请输入身高（m): ')) # 输入身高
# personWeight  = float(input('请输入体重（kg): '))  # 输入体重
# personAge  = float(input('请输入年龄（Y): '))# 输入年龄
# personSex = float(input('请输入性别（男：1；女：0): '))  # 输入性别
# # 处理数据
# BMI = personWeight / (personHeight * personHeight)
# BodyFatRatio = (1.2 * BMI + 0.23 * personAge - 5.4 - 18.8 * personSex) / 100
#
# if personSex == 1 and  0.15 < BodyFatRatio < 0.18:
#     print('您的体脂率是 %s, 体脂率正常' %BodyFatRatio)
# elif personSex == 0 and  0.25 < BodyFatRatio < 0.28:
#     print('您的体脂率是 %s, 体脂率正常' % BodyFatRatio)
# else:
#     print('您的体脂率是 %s, 体脂率不正常' % BodyFatRatio)

# 输入数据
correct = 1
while correct:
    personHeight  = float(input('请输入身高（m): ')) # 输入身高
    personWeight  = float(input('请输入体重（kg): '))  # 输入体重
    personAge  = float(input('请输入年龄（Y): '))# 输入年龄
    personSex = float(input('请输入性别（男：1；女：0): '))  # 输入性别
    # try:
    #     raise ValueError("输入错误")
    # except:
    if 0 < personHeight < 3 and 0 < personWeight < 300 and 0 < personAge < 100 and (personSex == 1 or personSex == 0):
        # 处理数据
        BMI = personWeight / (personHeight * personHeight)
        BodyFatRatio = (1.2 * BMI + 0.23 * personAge - 5.4 - 18.8 * personSex) / 100

        if personSex == 1: # 判断男士
            if 0.15 < BodyFatRatio < 0.18:
                print('先生，您好，您的体脂率是 %s, 恭喜您，非常健康，请继续保持。' %BodyFatRatio)
            elif 0.18 < BodyFatRatio:
                print('先生，您好，您的体脂率是 %s, 请注意，您偏胖。' %BodyFatRatio)
            else:
                print('先生，您好，您的体脂率是 %s, 请注意，您偏瘦。' % BodyFatRatio)
        else:  # 判断女士
            if 0.25 < BodyFatRatio < 0.28:
                print('女士，您好，您的体脂率是 %s, 恭喜您，非常健康，请继续保持。' % BodyFatRatio)
            elif 0.28 < BodyFatRatio:
                print('女士，您好，您的体脂率是 %s, 请注意，您偏胖。' % BodyFatRatio)
            else:
                print('女士，您好，您的体脂率是 %s, 请注意，您偏瘦。' % BodyFatRatio)
        correct = 0
    else:
        print('您的输入有误，请重新输入')