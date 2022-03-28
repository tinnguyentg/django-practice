from django.db import models
from django.utils.text import slugify


class Dictionary(models.Model):
    slug = models.SlugField(max_length=255)
    word = models.CharField(max_length=255)
    is_headword = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, **kwargs):
        self.word = self.word.lower()
        self.slug = slugify(self.word)
        return super().save(**kwargs)
