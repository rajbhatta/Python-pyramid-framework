## Working with Python Package ##

### 1. setup.py ###
```python
from setuptools import  setup
requires =[
    'pyramid',
    'pyramid_jinja2'
]
setup(name='mysite',
      install_requires=requires,
      entry_points="""\
        [paste.app_factory]
        main = mysite:main
        """)
```

### 2. development.ini ###
```python
[app:main]
use=egg:mysite

[server:main]
use=egg:pyramid#wsgiref
host=0.0.0.0
port=6543
```

### 3. __init__.py ###
```python
from pyramid.config import Configurator
from pyramid.view import view_config


@view_config(route_name='list', renderer ='list.jinja2')
def list(request):
    return dict()

def main(global_config, **settings):
    config=Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.add_route('list','/')
    config.scan()
    return config.make_wsgi_app()

```

### 4. list.jinja2 ###
```html
<h4>There is nothing here </h4>
```