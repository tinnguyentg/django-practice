from django.test import TestCase
from django.utils.text import slugify

from dictionary.models import Dictionary


class TestDictionaryModel(TestCase):
    def setUp(self) -> None:
        self.object = Dictionary.objects.create(word="Hello")
        self.total = Dictionary.objects.count()

    def test_create(self):
        word = "Django"
        Dictionary.objects.create(word=word)
        self.assertEqual(Dictionary.objects.count(), self.total + 1)

    def test_edit(self):
        new_word = "World"
        new_slug = slugify(new_word)

        self.object.word = new_word
        self.object.save()
        self.assertEqual(self.object.slug, new_slug)
        self.assertEqual(self.object.word, new_word.lower())

    def test_delete(self):
        self.object.delete()
        self.assertEqual(Dictionary.objects.count(), self.total - 1)
