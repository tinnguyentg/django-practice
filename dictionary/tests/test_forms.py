from django.test import TestCase

from dictionary.forms import DictionaryCreation
from dictionary.models import Dictionary


class TestDictionaryCreationForm(TestCase):
    def test_form(self):
        form = DictionaryCreation(data={"word": "hello", "source": "en"})
        self.assertTrue(form.is_valid())

    def test_form_invalid_source(self):
        form = DictionaryCreation(data={"word": "hello", "source": "vi"})
        self.assertFalse(form.is_valid())

    def test_form_invalid_word(self):
        word = "w" * (Dictionary._meta.get_field("word").max_length + 1)
        form = DictionaryCreation(data={"word": word, "source": "en-us"})
        self.assertFalse(form.is_valid())
