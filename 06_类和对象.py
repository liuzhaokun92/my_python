# -*- coding: utf-8 -*-
class SStudent(object):
    count=0
    def __init__(self, name):
        self.name = name
        SStudent.count=SStudent.count+1;

# 访问限制
# 请把下面的Student对象的gender字段对外隐藏起来，
# 用get_gender()和set_gender()代替，并检查参数有效性：
class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender
    def set_gender(self,gender):
    	self.__gender=gender;
    	return self.__gender
    def get_gender(self):
    	return self.__gender

# 测试:
bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('1测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('1测试失败!')
    else:
        print('1测试成功!')
# 测试:

if SStudent.count != 0:
    print('21测试失败!')
else:
    bart = SStudent('Bart')
    if SStudent.count != 1:
        print('22测试失败!')
    else:
        lisa = SStudent('Bart')
        if SStudent.count != 2:
            print('23测试失败!')
        else:
            print('Students:', SStudent.count)
            print('测试通过!')