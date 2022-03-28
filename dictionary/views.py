from typing import Any, Dict

from django.db import models
from django.views import generic

from .forms import DictionaryCreation
from .models import Dictionary
from .oxford import Entries, Lemmas


class Index(generic.CreateView):
    form_class = DictionaryCreation
    template_name = "dictionary/index.html"

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
        oxford_entries = Entries(word)
        oxford_entries_result = oxford_entries.result()

        if oxford_entries_result.get("error"):
            context["object"].is_headword = False
            context["object"].save()
            oxford_lemmas = Lemmas(word)
            context["oxford_lemmas"] = oxford_lemmas.result()
        else:
            context["oxford_entries"] = oxford_entries_result

        return context
