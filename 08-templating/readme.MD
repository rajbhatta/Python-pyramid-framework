## 3. Working with templating in Pyramid ##
```python
pip install pyramid_jinja2
- renderer ='hello.jinja2'
- return dictionary
- config.include('pyramid_jinja2')
```

## 2. Create app.py ##
```python
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.view import view_config


@view_config(route_name='hello_world', renderer ='hello.jinja2')
def hello(request):
    return dict(name='World!')

if __name__ == '__main__':
    config=Configurator()
    config.include('pyramid_jinja2')
    config.add_route('hello_world','/')
    config.scan()
    app=config.make_wsgi_app()
    server=make_server('0.0.0.0',6543,app)
    print('Server is started at http://127.0.0.1:6543')
    server.serve_forever()
```

## 3. View hello.jinja.2 ##
```html
<p>Hello <strong>{{ name }}</strong></p>
```

## 4. Run pyramid ##
```python
python app.py
```