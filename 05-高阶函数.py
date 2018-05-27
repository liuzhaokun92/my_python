from functools import reduce
import time, functools



def metric(fn):
	def wrapper(*args,**kw):
		print('%s executed in %s ms' % (fn.__name__,time.clock()))
		return fn(*args,**kw)
	return wrapper

@metric
def fast(x, y):
    time.sleep(3)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(5)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')



def createCounter():
	i=[0]
	def counter():
		i[0]=i[0]+1
		return i[0]
	return counter

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0]
def by_score(t):
    return -t[1]

#回数是指从左向右读和从右向左读都是一样的数，
#例如12321，909。请利用filter()筛选出回数：
def is_palindrome(n):
	m=str(n);l=len(m)
	for x in range(l):
		if m[x]!=m[l-x-1]:
			return False
	return True

Digits={'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, 
	'5': 5, '6': 6, '7': 7, '8': 8, '9': 9,'.':-1}
def str2float(s):
	def char2num(s):
		return Digits[s]
	def to_float(f,s):
		nonlocal point;
		if s==-1:     #检测到小数点，
			point=1;  #更改计算方向，
			return f;
		if point==0:  	#point=0，认为是在左边，十倍变大
			return f*10+s;	
		else:		  # point=1，十倍变小
			point=point*10;
			return f+s/point;
	number=map(char2num,s);
	point=0;    #point 是表示个位数在小数点在左边还是在右边，
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


# 测试:回数是指从左向右读和从右向左读都是一样的数，
# 例如12321，909。请利用filter()筛选出回数：
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')
L2 = sorted(L, key=by_name)
print(L2)
L2 = sorted(L, key=by_score)
print(L2)

# 测试:利用闭包返回一个计数器函数，每次调用它返回递增整数：
counterA=createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')
LL=list(filter(lambda x: x%2==1,range(1,20)))
print(LL)

int2=functools.partial(int,base=2)
print ('1000000=',int2('1000000'))
print ('1010101=',int2('1010101'))