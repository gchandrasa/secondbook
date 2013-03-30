from django.shortcuts import render, get_object_or_404

from .models import Book


def detail(request, username, slug):
    book = get_object_or_404(Book, user__username=username, slug=slug)
    context = {
        'book': book
    }
    return render(request, "books/detail.html", context)
