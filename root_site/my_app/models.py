from django.db import models
from django.conf import settings
from pytils.translit import slugify

class Language(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=2, unique=True)

    def __str__(self):
        return self.name


class Storage(models.Model):
    title = models.CharField(max_length=100, unique=True)
    title_small = models.CharField(max_length=100, unique=True)
    text = models.TextField()
    lang = models.ForeignKey(Language, on_delete=models.CASCADE)
    audio = models.FilePathField(path=settings.MEDIA_ROOT / 'audio')
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=100, unique=True, db_index=True)

    def save(self, *args, **kwargs):
        self.title_small = self.title.lower()
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title