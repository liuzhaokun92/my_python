from wsgiref.simple_server import make_server
from hello import application
#将'18-1web开发-hello.py'重新命名为'hello.py'
httpd=make_server('',8000,application)
print('Server HTTP on port 8000...')
httpd.serve_forever()