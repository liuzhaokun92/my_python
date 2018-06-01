# -*- coding: utf-8 -*-

# 请尝试写一个验证Email地址的正则表达式。
# 版本一应该可以验证出类似的Email：
# someone@gmail.com
# bill.gates@microsoft.com
import re
def is_valid_email(addr):
	f=re.compile(r'[a-zA-Z.]+@[a-zA-Z]+.com')
	if f.match(addr):
		return True
	else:
		return False


# 版本二可以提取出带名字的Email地址：
# <Tom Paris> tom@voyager.org => Tom Paris
# bob@example.com => bob
def name_of_email(addr):
	f=re.compile(r'<?(\w*\s*\w*)>?\s*\w*@\w*(\.\w*)$')
	if f.match(addr):
		return f.match(addr).group(1)
	else:
		return None

# 测试:
assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')

# 测试:
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')    

import time,threading

local_school=threading.local()
def process_student():
	std=local_school.student
	print('Hello, %s（in %s)'%(std,threading.current_thread().name))
def process_thread(name):
	local_school.student=name
	process_student()
t3=threading.Thread(target=process_thread,args=('Alice',),name='Thread-A')
t4=threading.Thread(target=process_thread,args=('Bob',),name='Thread-B')
t3.start()
t4.start()
t3.join()
t4.join()



def loop():
	print('thread %s is running' %threading.current_thread().name)
	n=0
	while n<5:
		n=n+1
		print('thread %s >>>%s'%(threading.current_thread().name,n))
		time.sleep(1)
	print('thread %s ended.' %threading.current_thread().name)
print('thread %s is running...'%threading.current_thread().name)
t=threading.Thread(target=loop,name='LoopThread')
t.start()
t.join()
print('thread %s ended.'%threading.current_thread().name)

balance=0
def change_it(n):
	global balance
	balance=balance+n
	balance=balance-n
def run_thread(n):
	for i in range(1000000):
		change_it(n)
t1=threading.Thread(target=run_thread,args=(5,))
t2=threading.Thread(target=run_thread,args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)