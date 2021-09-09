# Pyramid getting started #

## 2. How to use decorate @view_config in Pyramid ##
- @view_config(route_name='hello_world')
- config.scan()

## 2. Create app.py ##
```python
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.view import view_config


@view_config(route_name='hello_world')
def hello(request):
    return Response("Hello Pyramid !!")

if __name__ == '__main__':
    config=Configurator()
    config.add_route('hello_world','/')
    config.scan()
    app=config.make_wsgi_app()
    server=make_server('0.0.0.0',6543,app)
    print('Server is started at http://127.0.0.1:6543')
    server.serve_forever()
```

## 3. run pyramid ##
```python
python app.py
```
