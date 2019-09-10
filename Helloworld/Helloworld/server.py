# wsgiref
from wsgiref.simple_server import make_server
# 符合WSGI标准的一个HTTP处理函数，该函数由WSGI服务器来调用
# environment:一个包含所有HTTP请求信息的dict对象
# start_response:一个发送HTTP响应的函数


def application(environment, start_response):
    # start_response()
    # 发送HTTP响应的Header，注意Header只能发送一次，即只能调用一次start_response()函数。
    # 它接收两个参数，一个是HTTP响应码，一个是一组list表示的HTTP Header，
    # 每个Header用一个包含两个str的tuple表示
    start_response('200 OK', [('Content-Type', 'text/html')])
    # 返回值作为Http响应的body发送给浏览器，需要返回一个bytes
    return [b'<b>Hello, World</b>']


# 创建一个服务器，IP地址为空，端口是8000，处理函数是application
server = make_server('', 8000, application)
print("Serving HTTP on port 8000...")
# 开始监听http请求
server.serve_forever()
