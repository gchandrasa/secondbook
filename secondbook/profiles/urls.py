from django.conf.urls import patterns, url


urlpatterns = patterns('profiles.views',
    url(r'^login/$', 'login', name='auth_login'),
)
