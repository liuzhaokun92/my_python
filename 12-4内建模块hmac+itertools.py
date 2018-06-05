import hmac
message=b'hello, world!'
key=b'secret'
h=hmac.new(key,message,digestmod='MD5')
print(h.hexdigest())

# -*- coding: utf-8 -*-
import hmac, random

def hmac_md5(key, s):
    return hmac.new(key.encode('utf-8'), s.encode('utf-8'), 'MD5').hexdigest()

class User(object):
    def __init__(self, username, password):
        self.username = username
        self.key = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = hmac_md5(self.key, password)
db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}
def login(username, password):
    user = db[username]
    return user.password == hmac_md5(user.key, password)


# 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')

import itertools
# natuals=itertools.count(1)
# for n in natuals:
# 	print(n)
# aa=[1,2,3,4]
# cs=itertools.cycle(aa)
# for c in cs:
# 	print(c)
ns=itertools.repeat('A',3)
for n in ns:
	print(n)
natuals=itertools.count(-10)
ns2=itertools.takewhile(lambda x : x<=15,natuals)
print(list(ns2))
for c in itertools.chain('ABCD','1234'):
	print(c)
for key,group in itertools.groupby('AAABBBCCDDDAA'):
	print(key,list(group))
for key,group in itertools.groupby('AaABbBcCDddaa',lambda c:c.upper()):
	print(key,list(group))

# -*- coding: utf-8 -*-
# import itertools

def pi(N):
    # ' 计算pi的值 '
    # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
    # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
    # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
    # step 4: 求和:
    odd=itertools.count(1,2);
    su=0;c=1;
    odd_list=list(itertools.takewhile(lambda x:x<2*N,odd))

    for a in odd_list :
    	su=su+4/a*c;
    	c=c*-1
    return su 
# 测试:
print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')