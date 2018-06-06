# from urllib import request
# with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
# 	data=f.read()
# 	print('Status:',f.status,f.reason)
# 	for k,v in f.getheaders():
# 		print('%s:%s'%(k,v))
# 	print('Data:',data.decode('utf-8')) 
# 	
# from urllib import request
# req=request.Request('http://www.douban.com')
# req.add_header('User-Agent','Mozilla/6.0(iPhone;CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26(KHTML,like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# with request.urlopen(req)as f:
# 	print('Status:',f.status,f.reason)
# 	for k,v in f.getheaders():
# 		print('%s:%s '%(k,v))
# 	print('Data:',f.read().decode('utf-8'))
# -*- coding: utf-8 -*-
from urllib import request
import json
def fetch_data(url):
    with request.urlopen(url) as f:
    	data=f.read()
    return json.loads(data)

# 测试
URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json'
data = fetch_data(URL)
# print(data)
assert data['query']['results']['channel']['location']['city'] == 'Beijing'
print('ok')
from html.parser import HTMLParser
from html.entities import name2codepoint
class MyHTMLParser(HTMLParser):
	def handle_starttag(self,tag,attrs):
		print('<%s>' %tag)
	def handle_endtag(self,tag):
		print('</%s>'%tag)
	def handle_startendtag(self,tag,attrs):
		print('<%s/>'%tag)
	def handle_data(self,data):
		print(data)
	def handle_comment(self,data):
		print('<!-->',data,'-->')
	def handle_entityref(self,name):
		print('&%s:'% name)
	def handle_charref(self,name):
		print('&#%s:'%name)
parser=MyHTMLParser()
parser.feed('''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>''')