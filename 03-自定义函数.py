def move(n,a,b,c):#汉诺塔函数
	if n==1:
		print(a,'--->',c);
	else:
		move(n-1,a,c,b);#将n-1个从A移动到B
		move(1,a,b,c);#将最后一个从A移动到C
		move(n-1,b,a,c);#将n-1个从B移动到C


def product(x,y=1,*z):
	n=len(z);s=1;i=0;
	if n!=0:
		while i<n:
			s=s*z[i];
			i=i+1;
		return s*x*y
	else:
		return x*y

# 测试
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')
move(3, 'A', 'B', 'C')