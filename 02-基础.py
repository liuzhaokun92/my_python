#s1=72
#s2=85
#r=(s2-s1)/s1*100;
#print('%.1f%%' %r)
L=[
	['Apple','Google','Microsoft'],
	['Java','Python','Ruby','PHP'],
	['Adam','Bart','Lisa']
]
print(L[0][0]);
print(L[1][1]);
print(L[2][2])
height=1.75
weight=80.5
bmi=weight/(height*height);
if bmi<=18.5:
	print('过轻')
elif bmi<=25:
	print('正常')
elif bmi<=28:
	print('过重')
elif bmi<=32:
	print('肥胖')
elif bmi>32:
	print('严重肥胖');	
sum=0
for x in range(101):
	sum=sum+x
print(sum)

L=['Adam','Bart','Lisa']
n=0
while n<len(L):
	print('hello,',L[n])
	n=n+1
n1=255;
n2=1000;
print('n1的十六进制输出是',hex(n1))
print('n2的十六进制输出是',hex(n2))

import math
def quadratic(a,b,c):
	if b*b-4*a*c<0:
		return'错误'
	else:
		ans1=(-b+math.sqrt(b**2-4*a*c))/(2*a);
		ans2=(-b-math.sqrt(b**2-4*a*c))/(2*a);
		return ans1,ans2
while True:
	a=input('a：');a=int(a)
	b=input('b：');b=int(b)
	c=input('c：');c=int(c)

	print('ans1,ans2 is ',quadratic(a,b,c))
	break;
