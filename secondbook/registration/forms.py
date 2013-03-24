from django import forms
from django.utils.translation import ugettext_lazy as _

from profiles.models import User


class RegistrationForm(forms.Form):
    """
    Form for registering a new user account.

    """
    required_css_class = 'required'

    username = forms.RegexField(regex=r'^[\w.@+-]+$', max_length=30,
        label=_("Username"),
        error_messages={'invalid': _("This value may contain only letters, numbers and @/./+/-/_ characters.")})
    email = forms.EmailField(label=_("E-mail"))
    password = forms.CharField(widget=forms.PasswordInput,
        label=_("Password"))
    tos = forms.BooleanField(widget=forms.CheckboxInput,
                             label=_(u'I have read and agree to the Terms of Service'),
                             error_messages={'required': _("You must agree to the terms to register")})

    def clean_username(self):
        if User.objects.filter(username__iexact=self.cleaned_data['username']):
            raise forms.ValidationError(_("A user with that username already exists."))
        return self.cleaned_data['username']

    def clean_email(self):
        if User.objects.filter(email__iexact=self.cleaned_data['email']):
            raise forms.ValidationError(_("This email address is already in use. Please supply a different email address."))
        return self.cleaned_data['email']

