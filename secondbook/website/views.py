from django.shortcuts import render

from profiles.views import home


def index(request):

    if request.user.is_authenticated():
        return home(request)
    return render(request, 'index.html')
