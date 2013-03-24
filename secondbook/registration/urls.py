from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('registration.views',
    url(r'^signup/$', 'register', name='register'),
)
