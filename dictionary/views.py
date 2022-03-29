from typing import Any, Dict

from django.db import models
from django.http import Http404
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.text import slugify
from django.views import generic

from .forms import DictionaryCreation
from .models import Dictionary
from .oxford import Entries, Lemmas


class Index(generic.CreateView):
    form_class = DictionaryCreation
    template_name = "dictionary/index.html"

    def post(self, request, **kwargs):

        word = request.POST.get("word", "")
        slug = slugify(word)
        source = request.POST.get("source", "en-us")
        if word and Dictionary.objects.filter(slug=slug, source=source).exists():
            return redirect(reverse("dictionary:detail", args=(source, slug)))

        return super().post(request, **kwargs)

    def get_queryset(self) -> models.query.QuerySet[Dictionary]:
        return Dictionary.objects.all().order_by("-created_at")

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["words"] = self.get_queryset()
        return context


class Detail(generic.DetailView):
    model = Dictionary
    template_name = "dictionary/detail.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        word = context["object"].word.lower()
        source = context["object"].source.lower()
        oxford_entries = Entries(word, source)
        oxford_entries_result = oxford_entries.result()

        if oxford_entries_result.get("msg"):
            context["oxford_error"] = oxford_entries_result
        elif oxford_entries_result.get("error"):
            context["object"].is_headword = False
            context["object"].save()
            oxford_lemmas = Lemmas(word, source)
            context["oxford_lemmas"] = oxford_lemmas.result()
        else:
            context["oxford_entries"] = oxford_entries_result

        return context

    def get_queryset(self) -> models.query.QuerySet[Dictionary]:
        source = self.kwargs["source"]
        slug = self.kwargs["slug"]
        return Dictionary.objects.filter(source=source, slug=slug)

    def get_object(self) -> Dictionary:
        object = None
        try:
            object = self.get_queryset().get()
        except Dictionary.DoesNotExist:
            word = self.request.GET.get("word")
            source = self.kwargs["source"]
            if bool(int(self.request.GET.get("forceInsert", "0"))) and word:
                object = Dictionary(source=source, word=word)
                object.save()

        if not object:
            raise Http404
        return object
