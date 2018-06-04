from collections import namedtuple
Point=namedtuple('Point',['x','y'])
p=Point(1,2)
print(p.x)
print(p.y)


from collections import deque
q=deque(['a','b','c'])
q.append('x')
q.appendleft('y')
print(q)

from collections import defaultdict
dd=defaultdict(lambda:'N/A')
dd['key1']='abc'
print(dd['key1'])
print(dd['key2'])

from collections import OrderedDict
od=OrderedDict([('a',1),('c',3),('b',2)])
print(od)
class LastUpdatedOderedDict(OrderedDict):
	def __init__(self,capacity):
		super(LastUpdatedOderedDict,self).__init__()
		self._capacity=capacity
	def __setitem__(self,key,value):
		containsKey=1 if key in self else 0
		if len(self)-containsKey>=self._capacity:
			last=self.popitem(last=False)
			print('remove:',last)
		if containsKey:
			del self[key]
			print('set:',(key,value))
		else:
			print('add:',(key,value))
		OrderedDict.__setitem__(self,key,value)
from collections import Counter
c=Counter()
for ch in 'programming':
	c[ch]=c[ch]+1
print(c)

import base64
print(base64.b64encode(b'binary\x00string'))

# 请写一个能处理去掉=的base64解码函数
def safe_base64_decode(s):
    if len(s)%4==0:
    	return base64.b64decode(s)
    else:
    	while len(s)%4!=0:
    		s=s+b'='
    	return base64.b64decode(s)

# 测试:
assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('ok')
