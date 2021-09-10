## Dispatching URLS to Views with Routing ##
- Define a route that extracts part of the URL into a Python dictionary.
- Use that dictionary data in a view.

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
    config.add_route('home', '/howdy/{first}/{last}')
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
<h1>${name}</h1>
<p>First: ${first}, Last: ${last}</p>
</body>
</html>
```


### 5. tutorial/views.py ####
```python
from pyramid.view import (
    view_config,
    view_defaults
    )


@view_defaults(renderer='home.pt')
class TutorialViews:
    def __init__(self, request):
        self.request = request

    @view_config(route_name='home')
    def home(self):
        first = self.request.matchdict['first']
        last = self.request.matchdict['last']
        return {
            'name': 'Home View',
            'first': first,
            'last': last
        }
```

### Running the app ###
```python
pip install -e .
pserve development.ini
```

<b> Note: when starting monitor for PID ..... is appeared on IDE, type and call</b> http://localhost:6543/

### Reference ###
- https://docs.pylonsproject.org/projects/pyramid/en/latest/quick_tutorial/routing.html