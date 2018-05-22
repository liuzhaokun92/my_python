def triangles():
	n = 0
	L = [1]
	while True:
	    yield L
	    L=[1]+[L[i]+L[i+1] for i in range(n)]+[1]
	    n=n+1
	return
#	Y=[1];
#	yield Y;
#	if len(Y)=1:
#		Y=Y.append(1);
#
#	for x in x<=len(Y)
#		Y2=Y[x]+Y[x-1]
#		Y.append(Y2)
#	yield Y2

def findMinAndMax(L):
	if len(L)==0:
		return (None,None)
	else:
		max=L[0];min=L[0];
		for n in L:
			if max<n:
				max=n;
			if min>n:
				min=n;
		return (min,max)

def trim(s):
	if len(s)==0:
		return s
	#if s[:1]==' ':
	#	return trim(s[1:]);
	#elif s[-1:]==' ':
	#	return trim(s[:-1])
	#else:
	#	return s
	elif s[0]==' ':
			a=s[1:];
			return trim(a)
	elif s[-1]==' ':
			n=len(s);
			a=s[:n-1];
			return trim(a)
	return s


L=list(range(100))
L[:10];
L[11:20]
# 测试切片，利用切片操作，实现一个trim()函数，
# 去除字符串首尾的空格，注意不要调用str的strip()方法：
if trim('hello  ') != 'hello':
    print('a测试失败!')
elif trim('  hello') != 'hello':
    print('a测试失败!')
elif trim('  hello  ') != 'hello':
    print('a测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('a测试失败!')
elif trim('') != '':
    print('a测试失败!')
elif trim('    ') != '':
    print('a测试失败!')
else:
    print('a测试成功!')
# 请使用迭代查找一个list中最小和最大值，并返回一个tuple：
if findMinAndMax([]) != (None, None):
    print('b测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('b测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('b测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('b测试失败!')
else:
    print('b测试成功!')
print([x*x for x in range(1,11)]);
print([x*x for x in range(1,11) if x%2==0]);
print([m+n for m in 'ABC' for n in 'XYZ']);
# -*- coding: utf-8 -*-
L1 = ['Hello', 'World', 18, 'Apple', None]
L2=[s.lower() for s in L1 if isinstance(s,str)]
# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('c测试通过!')
else:
    print('c测试失败!')
    # 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')

 #!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Iterable, Iterator

def g():
    yield 1
    yield 2
    yield 3

print('Iterable? [1, 2, 3]:', isinstance([1, 2, 3], Iterable))
print('Iterable? \'abc\':', isinstance('abc', Iterable))
print('Iterable? 123:', isinstance(123, Iterable))
print('Iterable? g():', isinstance(g(), Iterable))

print('Iterator? [1, 2, 3]:', isinstance([1, 2, 3], Iterator))
print('Iterator? iter([1, 2, 3]):', isinstance(iter([1, 2, 3]), Iterator))
print('Iterator? \'abc\':', isinstance('abc', Iterator))
print('Iterator? 123:', isinstance(123, Iterator))
print('Iterator? g():', isinstance(g(), Iterator))

# iter list:
print('for x in [1, 2, 3, 4, 5]:')
for x in [1, 2, 3, 4, 5]:
    print(x)

print('for x in iter([1, 2, 3, 4, 5]):')
for x in iter([1, 2, 3, 4, 5]):
    print(x)

print('next():')
it = iter([1, 2, 3, 4, 5])
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

d = {'a': 1, 'b': 2, 'c': 3}

# iter each key:
print('iter key:', d)
for k in d.keys():
    print('key:', k)

# iter each value:
print('iter value:', d)
for v in d.values():
    print('value:', v)

# iter both key and value:
print('iter item:', d)
for k, v in d.items():
    print('item:', k, v)

# iter list with index:
print('iter enumerate([\'A\', \'B\', \'C\']')
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

# iter complex list:
print('iter [(1, 1), (2, 4), (3, 9)]:')
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)