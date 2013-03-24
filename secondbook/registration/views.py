from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm

from profiles.models import User

from .forms import RegistrationForm


def register(request):
    form = AuthenticationForm()
    registration_form = RegistrationForm(request.POST or None)
    if request.method == 'POST':
        if registration_form.is_valid():
            User.objects.create_user(
                registration_form.cleaned_data['username'],
                registration_form.cleaned_data['email'],
                registration_form.cleaned_data['password']
            )
            return redirect(settings.LOGIN_REDIRECT_URL)
    context = {
        'form': form,
        'registration_form': registration_form,
        'registration': True
    }
    return render(request, 'registration/registration_form.html', context)


def activate(request):

    return render(request, 'registration/activate.html')
