#
# class Person:
#     __slots__ = []
#     age = 19
#     height = 77
#     count = 1
# # p = Person()
# # p.age = 18
# # print(p.age)
# # print(p.__dict__)
# p = Person()
# # 给类增加属性
# Person.sex = 1
# # 修改类属性
# Person.age=20
# del Person.age
# print(Person.age,Person.sex)

"""
# 实例方法p.eat()、类方法 Person.eat()、静态方法  Person.eat()
# 实例方法

"""
# class Person:
#     age = 10
#     def shiliefangfa(self):
#         print(self)
#         print(self.age)
#         print(self.number)
#     @classmethod
#     def leifangfa(cls):
#         print(cls.age)
#         print(cls.number)
#     @staticmethod
#     def jingtaifashi():
#         print(Person.age)
#         print(Person.number)
#
# p = Person()
# p.number = 9
# Person.number = 9
# print(p.shiliefangfa())
# print(p.leifangfa())
# print(p.jingtaifashi())
#
# a = 10
# b = 'ABC'
# print(a.__class__)
# print(int.__dict__)
# print(b.__class__)
# print(int.__class__)
# print(type(1))


"""
# 怎么通过原类创建

"""
# __metalclass__ = type
# class Animal:
#     pass
# class Person(metaclass=type): # 方法一
#     __metalclass__ = type # 方法2
#     pass
# class Person1(Animal): # 方法3
#     pass

"""
# 类的私有化属性：保证数据的安全性 X 公有属性  _X 受保护的属性 __私有化属性
# 模块内部

"""
# class Animal:
#     __x = 10
#     def test(self):
#         print(Animal.__x)
#         print(self.__x)
#     pass   # 类的内部
# class Dog(Animal):
#     def test2(self):
#         print(Dog.__x)
#         print(self.__x)
#     pass #  子类的内部
#
# a = Animal()
# a.test()
# print(Animal._Animal__x)
#
# # b = Dog()
# # b.test2()
# # print(Dog.__x)
#
# _c = 666

"""
私有属的应用场景： 值有变化的可能设置为实例属性，而不是设置为类属性
"""
# class Person:
#     # 主要作用，当我们创建好一个实例对象后，会自动的调用 这个广场，来初始化这个对象
#     def __init__(self):
#         self.__age = 18
#         pass
#     def setAge(self,value):
#         if isinstance(value,int) and value in range(0,200):
#             self.__age = value
#         else:
#             print('您的输入有错，请重新输入数字')
#     def getAge(self):
#         return self.__age
#
#
# p1 = Person()
# while True:
#     p1.setAge(int(input("请输入数字：")))
# print(p1.getAge())
# # print(p1.age)
# print(Person.__dict__)
# print(p1.__class__)
# print(Person.__class__)



"""
只读属性
"""

class Person:
    def __init__(self):
        self.__age = 18
    # 主要作用，可以以使用属性的方式，来使用这个方法
    @property
    def getAge(self):
        return self.__age
p = Person()
# print(p.getAge())
print(p.getAge)
