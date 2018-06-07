from PIL import Image,ImageFilter
im=Image.open('E:\\workspace\\Python\\test.jpg')
w,h=im.size
print('Original image size:%s x %s '%(w,h))
im.thumbnail((w//2,h//2))
print('Resize image to:%s x %s '%(w//2,h//2))
# im.save('thumbnail.jpg','jpeg')
im2=im.filter(ImageFilter.BLUR)
# im2.save('blur.jpg','jpeg')
from PIL import Image,ImageFilter,ImageFont,ImageDraw
import random
def rndChar():
	return chr(random.randint(65,90))
def rndColor():
	return (random.randint(64,255),random.randint(64,255),random.randint(64,255))
def rndColor2():
	return (random.randint(32,127),random.randint(32,127),random.randint(32,127))
width=60*4
height=60
image=Image.new('RGB',(width,height),(255,255,255))
font=ImageFont.truetype('C:\\Windows\\Fonts\\Arial.ttf',36)
draw=ImageDraw.Draw(image)
for x in range(width):
	for y in range(height):
		draw.point((x,y),fill=rndColor())
for t in range(4):
	draw.text((60*t+10,10),rndChar(),font=font,fill=rndColor2())
image=image.filter(ImageFilter.BLUR)
# image.save('code.jpg','jpeg')

import requests
r=requests.get('https://www.douban.com/')
print(r.status_code)
# print(r.text)
r=requests.get('https://www.douban.com/search',params={'q':'python','cat':'1001'})
print(r.url)
print(r.encoding)
print(r.content)

import psutil
print('#CPU逻辑数量')
print(psutil.cpu_count())   #CPU逻辑数量
print('#CPU物理核心数')
print(psutil.cpu_count(logical=False))  #CPU物理核心数

print('#获取物理内存和交换内存信息')#获取物理内存和交换内存信息
print(psutil.virtual_memory())
print(psutil.swap_memory())

#获取磁盘信息
print('# 磁盘分区信息')
print(psutil.disk_partitions())# 磁盘分区信息
print('# 磁盘使用情况')
print(psutil.disk_usage('/')) # 磁盘使用情况
print('# 磁盘IO')
print(psutil.disk_io_counters())# 磁盘IO

#获取网络信息
print('# 获取网络读写字节／包的个数')
print(psutil.net_io_counters())# 获取网络读写字节／包的个数
print('# 获取网络接口信息')
print(psutil.net_if_addrs())# 获取网络接口信息
print('# 获取网络接口状态')
print(psutil.net_if_stats())# 获取网络接口状态
print('# 获取当前网络连接信息')
print(psutil.net_connections())# 获取网络接口状态