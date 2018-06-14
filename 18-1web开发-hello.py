#需要重新命名为hello.py
#否则无法运行
def application(environ,start_response):
	start_response('200 OK',[('Content-Type','text/html')])
	body='<h1>Hello, %s</h1>'%(environ['PATH_INFO'][1:]or 'web')
	return [body.encode('utf-8')]