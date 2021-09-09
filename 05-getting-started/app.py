from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

def hello(request):
    return Response("Hello Pyramid !!")

if __name__ == '__main__':
    config=Configurator()
    config.add_route('hello_world','/')
    config.add_view(hello, route_name='hello_world')
    app=config.make_wsgi_app()
    server=make_server('0.0.0.0',6543,app)
    print('Server is started at http://127.0.0.1:6543')
    server.serve_forever()