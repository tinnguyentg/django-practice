from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Dictionary(models.Model):
    class SourceLang(models.TextChoices):
        ENGLISH = "en", "en"
        AMERICAN_ENGLISH = "en-us", "en-us"

    slug = models.SlugField(max_length=255)
    word = models.CharField(max_length=255)
    source = models.CharField(
        max_length=50, choices=SourceLang.choices, default=SourceLang.AMERICAN_ENGLISH
    )
    is_headword = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, **kwargs):
        self.word = self.word.lower()
        self.slug = slugify(self.word)
        return super().save(**kwargs)

    def get_absolute_url(self):
        return reverse("dictionary:detail", args=(self.source, self.slug))
