# -*- coding:utf-8 -*-
import re
from datetime import datetime,timedelta,timezone
now=datetime.now()
print(now)
print(type(now))
dt=datetime(2015,4,19,12,20)
print(dt)
print(dt.timestamp())
t=1429417300.0
print(datetime.fromtimestamp(t))
print(now.strftime('%a,%b %d %H:%M'))
utc_dt=datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)
bj_dt=utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)
tokyo_dt=utc_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt)
tokyo_dt2=bj_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt2)

# 假设你获取了用户输入的日期和时间如2015-1-21 9:01:30，
# 以及一个时区信息如UTC+5:00，均是str，
# 请编写一个函数将其转换为timestamp：

def to_timestamp(dt_str, tz_str):

	# 获取时间，忽略时区
    times=datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')

    # 获取时区
    utc_inf=re.match(r'^(\w{3})([+|-]\d+):(\d+)',tz_str).group(2)
    zone=int(utc_inf)

    # 时差转换，以东八区为基准
    times3=times+timedelta(hours=(8-zone))
    
    print(times3)#显示转换到东八区的时间
    return times3.timestamp()#返回timestamp格式
   
# 测试:
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')