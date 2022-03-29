from urllib.parse import urlencode

from django.test import TestCase
from django.urls import reverse
from django.utils.text import slugify

from dictionary.models import Dictionary


class TestIndexView(TestCase):
    def test_view_success(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_view_success_using_view_name(self):
        response = self.client.get(reverse("dictionary:index"))
        self.assertEqual(response.status_code, 200)

    def test_template_used(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "dictionary/index.html")

    def test_post(self):
        data = {"word": "hello", "source": "en-us"}
        response = self.client.post("/", data=data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Dictionary.objects.count(), 1)


class TestDetailView(TestCase):
    def setUp(self) -> None:
        self.word = "hello"
        Dictionary.objects.create(word=self.word)

    def test_view_success(self):
        url = reverse("dictionary:detail", args=("en-us", slugify(self.word)))
        response = self.client.get(url)

        self.assertTemplateUsed(response, "dictionary/detail.html")
        self.assertEqual(response.status_code, 200)

    def test_force_insert(self):
        not_exist_word = "test"
        total = Dictionary.objects.count()

        url = reverse("dictionary:detail", args=("en-us", slugify(not_exist_word)))
        params = {"forceInsert": "1", "word": not_exist_word}

        response = self.client.get(url + "?" + urlencode(params))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Dictionary.objects.count(), total + 1)
