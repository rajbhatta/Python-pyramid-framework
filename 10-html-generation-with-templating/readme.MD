## HTML generation with template ##

### 1. setup.py ###
```python
from setuptools import  setup
requires =[
    'pyramid',
    'pyramid_jinja2',
    'pyramid_chameleon',
    'waitress'
]

setup(
    name='tutorial',
    install_requires=requires,
    entry_points={
        'paste.app_factory': [
            'main = tutorial:main'
        ],
    },
)
```

### 2. development.ini ###
```python
[app:main]
use = egg:tutorial
pyramid.reload_templates = true

[server:main]
use = egg:waitress#main
listen = localhost:6543
```

### 3. tutorial/__init__.py ###
```python
from pyramid.config import Configurator


def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.add_route('home', '/')
    config.add_route('hello', '/howdy')
    config.scan('.views')
    return config.make_wsgi_app()

```

### 4. tutorial/home.pt ####
```python
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Quick Tutorial: ${name}</title>
</head>
<body>
<h1>Hi ${name}</h1>
</body>
</html>
```


### 5. tutorial/views.py ####
```python
from pyramid.view import view_config


# First view, available at http://localhost:6543/
@view_config(route_name='home', renderer='home.pt')
def home(request):
    return {'name': 'Home View'}


# /howdy
@view_config(route_name='hello', renderer='home.pt')
def hello(request):
    return {'name': 'Hello View'}
```

### Running the app ###
```python
pip install -e .
pserve development.ini
```

<b> Note: when starting monitor for PID ..... is appeared on IDE, type and call</b> http://localhost:6543/

### Reference ###
- https://docs.pylonsproject.org/projects/pyramid/en/latest/quick_tutorial/templating.html