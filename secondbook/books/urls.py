from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('books.views',
    url(r'^(?P<username>[\w]+)/(?P<slug>[-\w]+)$', 'detail', name='detail'),
)
