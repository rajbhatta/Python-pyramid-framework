## Working with Python Package ##

### 1. setup.py ###
```python
from setuptools import  setup
requires =[
    'pyramid',
    'pyramid_jinja2',
    'waitress'
]
setup(name='tutorial',
      install_requires=requires,
      entry_points={
          'paste.app_factory': [
              'main = tutorial:main'
          ],
      })
```

### 2. development.ini ###
```python
[app:main]
use = egg:tutorial

[server:main]
use = egg:waitress#main
listen = localhost:6543
```

### 3. tutorial/__init__.py ###
```python
from pyramid.config import Configurator
from pyramid.response import Response


def hello_world(request):
    return Response('<body><h1>Hello World!</h1></body>')


def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.add_route('hello', '/')
    config.add_view(hello_world, route_name='hello')
    return config.make_wsgi_app()

```

### Running the app ###
```python
pip install -e .
pserve development.ini
```

<b> Note: when starting monitor for PID ..... is appeared on IDE, type and call</b> http://localhost:6543/

### Reference ###
- https://docs.pylonsproject.org/projects/pyramid/en/latest/quick_tutorial/ini.html