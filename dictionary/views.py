from typing import Any, Dict

from django.db import models
from django.views import generic

from .forms import DictionaryCreation
from .models import Dictionary


class Index(generic.CreateView):
    form_class = DictionaryCreation
    template_name = "dictionary/index.html"

    def get_queryset(self) -> models.query.QuerySet[Dictionary]:
        return Dictionary.objects.all().order_by("-created_at")

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["words"] = self.get_queryset()
        return context
