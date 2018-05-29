#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# err_reraise.py
def foo(s):
    n = int(s)
    if n==0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise

bar()
# metaclass是创建类，所以必须从`type`类型派生：
class ListMetaclass(type):
    def __new__(cls,name,bases,attrs):
        attrs['add']=lambda self,value:self.append(value)
        return type.__new__(cls,name,bases,attrs)
#指示使用ListMetaclass来定制类
class MyList(list,metaclass=ListMetaclass):
    pass

L=MyList()
L.add(1)
L.add(2)
L.add(3)
L.add('END')
print(L)

from enum import Enum, unique
# 把Student的gender属性改造为枚举类型，可以避免使用字符串：
Gender=Enum('Gender',('Male','Female'))
 
class Student(object):
    def __init__(self,name,gender):
    	self.name=name;
    	self.gender=gender

bart = Student('Bart', Gender.Male)
if bart.gender==Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')

# class Student(object):

#     def __init__(self):
#         self.name = 'Michael'

#     def __getattr__(self, attr):
#         if attr=='score':
#             return 99
#         if attr=='age':
#             return lambda: 25
#         raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)

# s = Student()
# print(s.name)
# print(s.score)
# print(s.age())
# # AttributeError: 'Student' object has no attribute 'grade'
# # print(s.grade)


# class Fib(object):

#     def __getitem__(self, n):
#         if isinstance(n, int):
#             a, b = 1, 1
#             for x in range(n):
#                 a, b = b, a + b
#             return a
#         if isinstance(n, slice):
#             start = n.start
#             stop = n.stop
#             if start is None:
#                 start = 0
#             a, b = 1, 1
#             L = []
#             for x in range(stop):
#                 if x >= start:
#                     L.append(a)
#                 a, b = b, a + b
#             return L

# f = Fib()
# print(f[0])
# print(f[5])
# print(f[100])
# print(f[0:5])
# print(f[:10])



# class Fib(object):

#     def __init__(self):
#         self.a, self.b = 0, 1 # 初始化两个计数器a，b

#     def __iter__(self):
#         return self # 实例本身就是迭代对象，故返回自己

#     def __next__(self):
#         self.a, self.b = self.b, self.a + self.b # 计算下一个值
#         if self.a > 100: # 退出循环的条件
#             raise StopIteration();
#         return self.a # 返回下一个值

# for n in Fib():
#     print(n,)



# class Student(object):

#     def __init__(self, name):
#         self.name = name

#     def __str__(self):
#         return 'Student object (name: %s)' % self.name

#     __repr__ = __str__

# print(Student('Michael'))

# class Screen(object):
#     def __init__(self):
#     	self._width=None;
#     	self._height=None;

#     @property
#     def width(self):        #定义属性名
#     	return self._width;
#     @width.setter           #这里的setter好像是不能改
#     def width(self,width):  #注意：定义的属性名和前面的相同
#     	self._width=width;

#     @property
#     def height(self):           
#     	return self._height;
#     @height.setter            #这里的setter好像是不能改
#     def height(self,height):  #注意：定义的属性名和前面的相同
#     	self._height=height;

#     @property
#     def resolution(self):
#     	return self._width*self._height;


# # 测试:请利用@property给一个Screen对象加上width和height属性，
# # 以及一个只读属性resolution：
# s=Screen()
# s.width=1024
# s.height=768
# print('resolution =', s.resolution)
# if s.resolution == 786432:
#     print('测试通过!')
# else:
#     print('测试失败!')