from pyramid.view import view_config


@view_config(route_name='home', renderer='Install_Package_02:templates/mytemplate.jinja2')
def my_view(request):
    return {'project': 'Install_Package_02'}
