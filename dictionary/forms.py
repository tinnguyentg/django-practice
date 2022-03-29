from django import forms

from .models import Dictionary


class DictionaryCreation(forms.ModelForm):
    class Meta:
        model = Dictionary
        fields = ["source", "word"]
        widgets = {
            "word": forms.TextInput(
                attrs={"placeholder": "word", "class": "rounded-r sm:rounded-r-none font-semibold"}
            ),
            "source": forms.Select(attrs={"class": "rounded-l font-semibold"}),
        }
