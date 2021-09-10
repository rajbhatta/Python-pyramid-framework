## Objectives ##
- Group related views into a view class.
- Centralize configuration with class-level @view_defaults.
- Dispatch one route/URL to multiple views based on request data.
- Share states and logic between views and templates via the view class.

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
    config.add_route('hello', '/howdy/{first}/{last}')
    config.scan('.views')
    return config.make_wsgi_app()

```

### 4. tutorial/home.pt ####
```python
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Quick Tutorial: ${view.view_name} - ${page_title}</title>
</head>
<body>
<h1>${view.view_name} - ${page_title}</h1>

<p>Go to the <a href="${request.route_url('hello', first='jane',
        last='doe')}">form</a>.</p>
</body>
</html>
```


### 5. tutorial/views.py ####
```python
from pyramid.view import (
    view_config,
    view_defaults
    )


@view_defaults(route_name='hello')
class TutorialViews:
    def __init__(self, request):
        self.request = request
        self.view_name = 'TutorialViews'

    @property
    def full_name(self):
        first = self.request.matchdict['first']
        last = self.request.matchdict['last']
        return first + ' ' + last

    @view_config(route_name='home', renderer='home.pt')
    def home(self):
        return {'page_title': 'Home View'}

    # Retrieving /howdy/first/last the first time
    @view_config(renderer='hello.pt')
    def hello(self):
        return {'page_title': 'Hello View'}

    # Posting to /howdy/first/last via the "Edit" submit button
    @view_config(request_method='POST', renderer='edit.pt')
    def edit(self):
        new_name = self.request.params['new_name']
        return {'page_title': 'Edit View', 'new_name': new_name}

    # Posting to /howdy/first/last via the "Delete" submit button
    @view_config(request_method='POST', request_param='form.delete',
                 renderer='delete.pt')
    def delete(self):
        print ('Deleted')
        return {'page_title': 'Delete View'}
```

### 6. tutorial/delete.pt ###
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Quick Tutorial: ${page_title}</title>
</head>
<body>
<h1>${view.view_name} - ${page_title}</h1>
</body>
</html>
```

### 7. tutorial/edit.pt ###
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Quick Tutorial: ${view.view_name} - ${page_title}</title>
</head>
<body>
<h1>${view.view_name} - ${page_title}</h1>
<p>You submitted <code>${new_name}</code></p>
</body>
</html>
```

### 8. tutorial/hello.pt ###
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Quick Tutorial: ${view.view_name} - ${page_title}</title>
</head>
<body>
<h1>${view.view_name} - ${page_title}</h1>
<p>Welcome, ${view.full_name}</p>
<form method="POST"
      action="${request.current_route_url()}">
    <input name="new_name"/>
    <input type="submit" name="form.edit" value="Save"/>
    <input type="submit" name="form.delete" value="Delete"/>
</form>
</body>
</html>
```

### Running the app ###
```python
pip install -e .
pserve development.ini
```

<b> Note: when starting monitor for PID ..... is appeared on IDE, type and call</b> http://localhost:6543/

### ULRs to invoke ###
```html
http://localhost:6543/
```

### Reference ###
- https://docs.pylonsproject.org/projects/pyramid/en/latest/quick_tutorial/more_view_classes.html