from django.shortcuts import render

from django.contrib.auth import views as auth_views
from registration.forms import RegistrationForm


def login(request):
    registration_form = RegistrationForm()
    context = {
        'registration_form': registration_form,
        'login': True,
    }
    return auth_views.login(request, extra_context=context)


def home(request):
    context = {

    }
    return render(request, 'profiles/home.html', context)
