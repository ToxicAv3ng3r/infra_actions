from django.http import HttpResponse


def index(request):
    data = 'У меня получилось!'
    return HttpResponse(data, status=200)


def second_page(request):
    return HttpResponse('А это вторая страница!', status=200)
