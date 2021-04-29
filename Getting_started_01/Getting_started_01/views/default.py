from pyramid.view import view_config


@view_config(route_name='home', renderer='Getting_started_01:templates/mytemplate.jinja2')
def my_view(request):
    return {'project': 'Getting_started_01'}
