from functools import reduce
#def add(x,y,f):
#	return f(x)+f(y)
#print (add(-5,6,abs));

#def a(x):
#	return x*x
#r=map(a,[1,2,3,4,5,6,7,8,9]);
# list(r)
Digits={'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,'.':-1}
def str2float(s):
	def char2num(s):
		return Digits[s]
	def to_float(f,s):
		nonlocal point;
		if s==-1:
			point=1;
			return f;
		if point==0:
			return f*10+s;
		else:
			point=point*10;
			return f+s/point;
	number=map(char2num,s);
	point=0;
	return reduce(to_float,number,0.0)

# def str2float(s):
#     nums = map(lambda ch: CHAR_TO_FLOAT[ch], s)
#     point = 0
#     def to_float(f, n):
#         nonlocal point
#         if n == -1:
#             point = 1
#             return f
#         if point == 0:
#             return f * 10 + n
#         else:
#             point = point * 10
#             return f + n / point
#     return reduce(to_float, nums, 0.0)


def prod(L):
	def cheng(x,y):
		return x*y
	return (reduce(cheng,L))
	

def normalize(name):
	return (name.capitalize())
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

# 请编写一个prod()函数，可以接受一个list并利用reduce()求积：
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

# 利用map和reduce编写一个str2float函数，
# 把字符串'123.456'转换成浮点数123.456：
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')