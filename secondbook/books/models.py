from django.db import models
from django.template.defaultfilters import slugify
from django.conf import settings


class Book(models.Model):
    isbn = models.CharField("ISBN", max_length=30, blank=True)
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    authors = models.CharField(max_length=255, blank=True)
    publisher = models.CharField(max_length=255, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    price = models.PositiveIntegerField()
    picture = models.ImageField(upload_to='pictures', blank=True)
    year = models.PositiveIntegerField(blank=True, null=True)
    page = models.PositiveIntegerField('Number of pages', blank=True, null=True)

    location = models.CharField(max_length=255, blank=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    class Meta:
        unique_together = (('user', 'slug'))

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super(Book, self).save(*args, **kwargs)
