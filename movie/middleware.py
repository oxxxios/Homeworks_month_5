import requests
from django.http import HttpResponse

# Previous imports and timing middleware should remain unchanged


def stackoverflow(get_response):
    def middleware(request):
        # Этот метод ничего не делает, все, что мы хотим,
        # это обработка исключений
        return get_response(request)

    def process_exception(request, exception):
        url = 'https://api.stackexchange.com/2.2/search'
        params = {
            'site': 'stackoverflow',
            'order': 'desc',
            'sort': 'votes',
            'pagesize': 3,
            'tagged': 'python;django',
            'intitle': str(exception),
        }
        response = requests.get(url, params=params)
        html = ''
        for question in response.json()['items']:
            html += '<h2><a href="{link}">{title}</a></h2>'.format(**question)
        return HttpResponse(html)

    middleware.process_exception = process_exception

    return middleware