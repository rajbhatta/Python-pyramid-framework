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
