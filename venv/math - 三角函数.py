# # import math
# # a = math.sin(1 / 6 * math.pi)
# # print(a)
# # b = math.cos(1 / 3 * math.pi)
# # print(b)
# #
# a = 'abcadefg'
# print(a[4:2:-1])
# print(a[::-1])
# print(a.find("a",1,4))
# print(a.index("a",0,4))
# print(a.count('a'))
#
# a = 'abc DDdefg 四年我 和他'
# print(a.title())
# print(a.capitalize())
# print(a.lower())
# print(a.upper())
# c = 'abc-DDdefg-四年我-和他'
# print(c.split("-",2))
# print(c.startswith("bc",2,4))
#
# nums = range(10)
# idx = nums.index(5)
#
# print(idx)

# 可迭代对象
a = [1,"d",3,3]
# 迭代器
a = ["a","c","e","d"]
at = iter(a)
print(next(at))
print(next(at))
print(next(at))
print(next(at))
result = sorted(a,reverse = True)
print(result)