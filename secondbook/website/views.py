from django.shortcuts import render

from profiles.views import home
from books.models import Book


def index(request):

    if request.user.is_authenticated():
        return home(request)
    book_list = Book.objects.all()[:12]
    context = {
        'book_list': book_list
    }
    return render(request, 'index.html', context)
