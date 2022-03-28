from django import forms

from .models import Dictionary


class DictionaryCreation(forms.ModelForm):
    class Meta:
        model = Dictionary
        fields = ["word"]
        widgets = {
            "word": forms.TextInput(attrs={"placeholder": "word", "class": "rounded-l font-semibold"})
        }
