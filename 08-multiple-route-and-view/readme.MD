## 4. Working with multiple view and routing ##

## 1. Create app.py ##
```python
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.view import view_config

@view_config(route_name='home_page', renderer ='home.jinja2')
def home(request):
    name=request.params.get('name')
    return dict(name=name)

@view_config(route_name='hello', renderer ='hello_world.jinja2')
def hello_world(request):
    return dict(site_name='MyApp')

@view_config(route_name='hello', request_param='name', renderer ='hello_name.jinja2')
def hello_name(request):
    return dict()

if __name__ == '__main__':
    config=Configurator()
    config.include('pyramid_jinja2')
    config.add_route('hello','/')
    config.add_route('home_page', '/')
    config.scan()
    app=config.make_wsgi_app()
    server=make_server('0.0.0.0',6543,app)
    print('Server is started at http://127.0.0.1:6543')
    server.serve_forever()
```

## 2. View hello_name.jinja2 ##
```html
<p>Hello <strong>{{ name }}</strong></p>
```

## 3. View hello_world.jinja2 ##
```html
<h1>Hello World</h1>
<p>Nothing appeared in the URL for ?name.</p>
```

## 4. View home.jinja2 ##
```html
<a href="hello_name.jinja2">/hello</a>
<a href="hello_world.jinja2">/hello?name=jane</a>
```