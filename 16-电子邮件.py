# from email import encoders
# from email.header import Header
# from email.mime.text import MIMEText
# from email.utils import parseaddr, formataddr

# import smtplib

# def _format_addr(s):
#     name, addr = parseaddr(s)
#     return formataddr((Header(name, 'utf-8').encode(), addr))

# from_addr = input('From: ')
# password = input('Password: ')
# to_addr = input('To: ')
# smtp_server = input('SMTP server: ')

# msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
# msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
# msg['To'] = _format_addr('管理员 <%s>' % to_addr)
# msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()

# server = smtplib.SMTP(smtp_server, 25)
# server.set_debuglevel(1)
# server.login(from_addr, password)
# server.sendmail(from_addr, [to_addr], msg.as_string())
# server.quit()

import poplib

# 输入邮件地址, 口令和POP3服务器地址:
email = input('Email: ')
password = input('Password: ')
pop3_server = input('POP3 server: ')

# 连接到POP3服务器:
server = poplib.POP3_SSL(pop3_server,port=995)
# 可以打开或关闭调试信息:
server.set_debuglevel(1)
# 可选:打印POP3服务器的欢迎文字:
print(server.getwelcome().decode('utf-8'))

# 身份认证:
server.user(email)
server.pass_(password)

# stat()返回邮件数量和占用空间:
print('Messages: %s. Size: %s' % server.stat())
# list()返回所有邮件的编号:
resp, mails, octets = server.list()
# 可以查看返回的列表类似[b'1 82923', b'2 2184', ...]
print(mails)

# 获取最新一封邮件, 注意索引号从1开始:
index = len(mails)
resp, lines, octets = server.retr(index)

# lines存储了邮件的原始文本的每一行,
# 可以获得整个邮件的原始文本:
msg_content = b'\r\n'.join(lines).decode('utf-8')
# 稍后解析出邮件:
msg = Parser().parsestr(msg_content)

# 可以根据邮件索引号直接从服务器删除邮件:
# server.dele(index)
# 关闭连接:
server.quit()


# from array import array
# aa= b'\xb5\xc7\xc2\xbc\xca\xa7\xb0\xdc\xa3\xac\xc7\xeb\xca\xb9\xd3\xc3\xb0\xb2\xc8\xab\xc1\xac\xbd\xd3\xa3\xa8\xc8\xe7ssl\xa3\xa9\xa3\xac\xcf\xea\xcf\xb8\xcb\xb5\xc3\xf7\xc7\xeb\xb2\xe9\xbf\xb4'
# b=array('b',aa)
# c=b.tostring()
# d=c[::2]
# e=d.decode('')
# print(e)