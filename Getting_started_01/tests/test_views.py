from Getting_started_01.views.default import my_view
from Getting_started_01.views.notfound import notfound_view


def test_my_view(app_request):
    info = my_view(app_request)
    assert app_request.response.status_int == 200
    assert info['project'] == 'Getting_started_01'

def test_notfound_view(app_request):
    info = notfound_view(app_request)
    assert app_request.response.status_int == 404
    assert info == {}
