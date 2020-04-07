import pandas as pd
from datetime import date,timedelta
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams["font.sans-serif"]=["SimHei"] #用来正常显示中文标签
plt.rcParams["axes.unicode_minus"]=False #用来正常显示负号
'''
第一课时
'''
# df = pd.DataFrame({'ID':[1,2,3],'Name':['Tim','Victor','Tom']})
# df = df.set_index('ID')
# df.to_excel(r"C:\Users\yangxiu\Desktop\workhome\output.xlsx")
# print('完成')

'''
第二课时
'''
# people = pd.read_excel(r"C:\Users\yangxiu\Desktop\workhome\workinhome.xlsx",header=1,index_col='ID')
# people.columns = ['XX','xx','XX'] # 增加列名
# people = people.set_index['id']
# print(people.shape) # 多少行多少列
# print(people.columns)  # 每列名称
# print(people.head(3))
# print(people.tail(3))

'''
第三课时
'''
#
# s1 = pd.Series([1,2,3],index = [1,2,3],name = '序列')
# s2 = pd.Series([10,20,30],index = [1,2,3],name = '成本')
# s3 = pd.Series([100,200,300],index = [2,3,4],name = '销售额')
# s4 = pd.Series([20,30,40],index = [2,3,4],name = '利润')
# df = pd.DataFrame({s1.name:s1,s2.name:s2,s3.name:s3,s4.name:s4})
# df.to_excel(r"C:\Users\yangxiu\Desktop\workhome\output5.xlsx")
# print(df)
# print(s1)
# print(s2)
# print(s3)
'''
'''
# s3 = pd.Series([100,200,300],index = ['x','y','z'])
# L1 = [110,200,300]
# L2 = ['x','y','z']
# s2 = pd.Series(L1,index = L2)
# d = {'x': 100,'y':200,'Z':300}
# print(d.keys(),d.values())
# print(d['x'])
# s1 = pd.Series(d)
# print(s1)
# print(s2)
# print(s2)

'''
第4课时 自动填充
'''

# book = pd.read_excel(r"C:\Users\yangxiu\Desktop\workhome\output5.xlsx",header=2, usecols="D:I",dtype={'序列':str,'结论':str,'日期':str})
# def endTime(d,md):
#     yd = md // 12
#     m = d.month + md % 12
#     if m != 12:
#         yd += m // 12
#         m = m % 12
#     return date(d.year + yd,m,d.day)
#
# starttime = date(2018,1,1)
# for i in book.index:
#     # book['序列'].at[i] = i + 1
#     book.at[i,'序列'] = i + 1
#     # book['结论'].at[i] = "好" if i % 2 == 0 else '不好'
#     book.at[i,'结论'] = "好" if i % 2 == 0 else '不好'
#     # book['日期'].at[i] = starttime + timedelta(days=i)
#     # book['日期'].at[i] = date(starttime.year + i,starttime.month,starttime.day)
#     # book['日期'].at[i] = endTime(starttime,i)
#     book.at[i,'日期'] = endTime(starttime, i)
# book.set_index('序列',inplace= True)
# book.to_excel(r"C:\Users\yangxiu\Desktop\workhome\output11.xlsx")
#
# print(book)


'''
第5课时 函数计算
'''
# book = pd.read_excel(r"C:\Users\yangxiu\Desktop\workhome\output11.xlsx")
# # book['利润'] = book['销售额'] - book['成本']
# # for i in book.index:
# #     book['利润'].at[i]= book['销售额'].at[i] - book['成本'].at[i]
# book['利润'] = book['利润'].apply(lambda x:x-2)
# print(book)

'''
第5课时 数据排序
'''
# book = pd.read_excel(r"C:\Users\yangxiu\Desktop\workhome\output11.xlsx",index_col='序列')
# book.sort_values(by = ['结论','销售额'],inplace=True,ascending=['True','Flase'])
# print(book)

'''
第6课时 数据筛选
'''
# def age_200_to_300(a):
#     return 5001 < a <5008
# def levea(s):
#     return  200< s <1000
# book = pd.read_excel(r"C:\Users\yangxiu\Desktop\workhome\output11.xlsx")
# book = book.loc[book['销售额'].apply(age_200_to_300)].loc[book['成本'].apply(levea)]
# print(book)

'''
柱状图
'''
students = pd.read_excel(r"C:\Users\yangxiu\Desktop\workhome\output11.xlsx",dtype={'序列':str,'成本':str,'日期':str})
students.sort_values(by = '成本',inplace=True, ascending= True)
students.plot.bar( x = '序列', y = "成本", color = "orange",title = '喜欢你')
# plt.bar(students['序列'],students['成本'], color = "orange")
plt.tight_layout()
plt.xticks(students['序列'], rotation = '360')
plt.xlabel('序号')
plt.ylabel('成本')
plt.title("喜欢",fontsize = 16,color = 'blue')
plt.show()
print(students)

'''
分组柱状图
'''
# students = pd.read_excel(r'C:\Users\yangxiu\Desktop\workhome\output11.xlsx')
# students.sort_values(by = '销售额',inplace = True , ascending = False)
# students.plot.bar( x = '序列', y = ['销售额','利润'])
# # plt.tight_layout()
# plt.title('销售利润表',fontsize = 16,color = 'red',fontweight = 'bold')
# plt.xlabel('序列',fontweight = 'bold')
# plt.ylabel('金额', fontweight = 'bold')
# ax = plt.gca()
# ax.set_xticklabels(students['序列'], rotation = 60 ,ha = "right")
# f = plt.gcf()
# f.subplots_adjust(left = 0.2,top = 0.8, bottom = 0.3)
# plt.show()
# print(students)

'''
叠加柱状图
'''
# students = pd.read_excel(r'C:\Users\yangxiu\Desktop\workhome\output11.xlsx')
# students['合计'] = students['成本'] + students['销售额'] + students['利润']
# students.sort_values(by = '合计', inplace=True ,ascending = False)
# # students.sort_values(by = '销售额',inplace = True , ascending = False)
# # students.plot.bar( x = '序列', y = ['销售额','利润',"成本"], stacked = True)
# students.plot.barh( x = '序列', y = ['销售额','利润',"成本"], stacked = True)
# # plt.tight_layout()
# plt.title('销售利润表',fontsize = 16,color = 'red',fontweight = 'bold')
# plt.xlabel('金额',fontweight = 'bold')
# plt.ylabel('员工', fontweight = 'bold')
# ax = plt.gca()
# # ax.set_xticklabels(students['序列'], rotation = 60 ,ha = "right")
# f = plt.gcf()
# f.subplots_adjust(left = 0.2,top = 0.8, bottom = 0.3)
# plt.show()
# print(students)

'''
饼图
'''
# students = pd.read_excel(r'C:\Users\yangxiu\Desktop\workhome\output11.xlsx',index_col='序列')
# students["销售额"].sort_values(ascending= True).plot.pie(fontsize = 8,startangle = -270, counterclock = True)
# plt.ylabel('销售量',fontsize = 8 , fontweight = 'bold')
# plt.show()

'''
折线趋势图
'''
# students = pd.read_excel(r'C:\Users\yangxiu\Desktop\workhome\output11.xlsx',index_col='月份')
# # students.plot.area(y = ["成本","销售额","利润","净利"])
# students.plot.bar(y = ["成本","销售额","利润","净利"],stacked = True)
# plt.title('折线趋势图', fontsize = 16, color = 'blue',fontweight = "bold")
# plt.xlabel('员工')
# plt.ylabel('金额')
# # plt.xticks(students.index,fontsize = 8)
# plt.show()

'''
散点图
'''
# pd.options.display.max_columns = 8
# homes = pd.read_excel(r"C:\Users\yangxiu\Desktop\workhome\workinhome.xlsx")
# # homes.plot.scatter(x = '1.  你当前的主要岗位是？',y = '提交时间')
# homes.order_number.plot.hist(bins=50)
# plt.xticks(fontsize = 8,rotation = 90)
# plt.show()
# print(homes.head(3))

'''
密度图
'''
# pd.options.display.max_columns = 8
# homes = pd.read_excel(r"C:\Users\yangxiu\Desktop\workhome\workinhome.xlsx")
# homes.order_number.plot.kde()
# plt.xticks(range(0,max(homes.order_number),200),fontsize = 18, rotation = 90)
# plt.show()

'''
合并查询vlookup
'''
# sales = pd.read_excel(r'C:\Users\yangxiu\Desktop\workhome\output11.xlsx',sheet_name="Sheet1",index_col = "序列")
# # price = pd.read_excel(r'C:\Users\yangxiu\Desktop\workhome\output11.xlsx',sheet_name="Sheet2",index_col = "序列")
# # # table = sales.merge(price,how ="left", on = '序列',left_on = '序列',right_on = '序列').fillna(0)
# # # table = sales.merge(price,how ="left", on = '序列').fillna(0)
# # # table = sales.merge(price,how ="left").fillna(0)
# # table = sales.join(price, how ="left", on = '序列').fillna(0)
# # table.奖金 = table.奖金.astype(int)
# # print(table)

'''
数据校验
'''
# def reward_check(table):
#     try:
#         assert 0 <= table.奖金 <=1000
#     except:
#         print("%s \t %s has a invalid number" %(table.序列, table.奖金))
#

# def reward_check(table):
#     if  not 0 <= table.奖金 <=1000:
#         print("%s \t %s has a invalid number" % (table.序列, table.奖金))
# sales = pd.read_excel(r'C:\Users\yangxiu\Desktop\workhome\output11.xlsx',sheet_name="Sheet1")
# price = pd.read_excel(r'C:\Users\yangxiu\Desktop\workhome\output11.xlsx',sheet_name="Sheet2")
# table = sales.merge(price,how ="left", on = '序列').fillna(0)
# table.奖金 = table.奖金.astype(int)
# table.apply(reward_check,axis = 1)


'''
把一列分成两列
'''
# development = pd.read_excel(r"C:\Users\yangxiu\Desktop\workhome\workinhome.xlsx",sheet_name = "date")
# df = development.development_tool.str.split('，',n = 5,expand = True)
# # development["development_tool-1"] = df[0]
# development.to_excel(r"C:\Users\yangxiu\Desktop\workhome\workinhome.xlsx",sheet_name= "development_tool-1" )
# print(development.head(3))

'''
统计 函数
'''
# df = pd.read_excel(r'C:\Users\yangxiu\Desktop\workhome\output11.xlsx',sheet_name="Sheet1",index_col="序列")
# # row_sum = df['成本'] + df['销售额'] + df['利润']
# # # row_mean = row_sum / 3
# row_sum = df[["成本","销售额","利润"]].sum(axis = 1)
# row_mean = df[["成本","销售额","利润"]].mean(axis = 1)
# df['total'] = row_sum
# df['average'] = row_mean
# col_sum = df[["成本","销售额","利润","total","average"]].sum(axis = 0)
# col_mean = df[["成本","销售额","利润","total","average"]].mean(axis = 0)
# col_sum['月份2'] = "合计"
# df = df.append(col_sum,ignore_index= True)
# col_mean['月份2'] = "平均"
# df = df.append(col_mean,ignore_index= True)
#
# print(df)

'''
定位、消除重复数据 
'''
# df = pd.read_excel(r'C:\Users\yangxiu\Desktop\workhome\output12.xlsx',sheet_name="Sheet1")
# dupe = df.duplicated(subset='序列')
# dupe = dupe[dupe]
# df_duplicate = df.iloc[dupe.index]
# # df.drop_duplicates(subset='序列', keep = 'first',inplace=True) # 消除重新数据
#
# print(df_duplicate)

'''
行、列转换 
'''
# pd.options.display.max_columns = 3
# df = pd.read_excel(r'C:\Users\yangxiu\Desktop\workhome\output12.xlsx',sheet_name="Sheet1")
# table = df.transpose()
# print(table)

'''
读取CSV、TSV、TXT中的数据
'''
#
# students1 = pd.read_csv(r'C:\Users\yangxiu\Desktop\workhome\11.csv', index_col = 'id')
# students1 = pd.read_csv(r'C:\Users\yangxiu\Desktop\workhome\11.tsv', sep='\t' ,index_col='id')
# students1 = pd.read_csv(r'C:\Users\yangxiu\Desktop\workhome\11.txt', sep='|',index_col='id')

'''
透视表、分级、聚合
'''
# pd.options.display.max_columns = 999
# df = pd.read_excel(r'C:\Users\yangxiu\Desktop\workhome\output12.xlsx', sheet_name="Sheet1")
# pt1 = df.pivot_table(index="序列", columns="月份2", values="净利", aggfunc=np.sum)
# print(pt1)

'''
条件格式 
'''
# def low_score_read(s):
#     color = 'red' if s < 5000 else "black"
#     return f'color = {color}'
# students = pd.read_excel(r'C:\Users\yangxiu\Desktop\workhome\output12.xlsx', sheet_name="Sheet1")
# students.style.applymap(low_score_read, subset = {'销售额','利润','净利'})
# students.to_excel(r'C:\Users\yangxiu\Desktop\workhome\output13.xlsx')
# print(students)
