## Working with Pyramid Package and waitress ##

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

### 2. requirements.txt ###
```html
waitress
```

#### Install waitress to virtual environment using dependencies defined in requirements  ####
````html
pip install -e . -r requirements.txt
````

### 3. development.ini to reload view without reloading app server ###
```python
[app:main]
use=egg:mysite
pyramid.reload_template=true

[server:main]
use=egg:waitress#main
host=0.0.0.0
port=6543
```

### 4. movie view_config from __init__.py ###
```python
from pyramid.config import Configurator
from pyramid.view import view_config

def main(global_config, **settings):
    config=Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.add_route('list','/')
    config.scan()
    return config.make_wsgi_app()

```

### 5. view.py ###
```python
from pyramid.view import view_config

@view_config(route_name='list',
             renderer='templates/list.jinja2')
def list(request):
    return dict()
```

### 4. list.jinja2 ###
```html
<h4>There is nothing here </h4>
```

### 5. server the development.ini with --reload feature ###
```python
pserve development.ini -- reload
```