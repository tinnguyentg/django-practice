from django import forms

from .models import Dictionary


class DictionaryCreation(forms.ModelForm):
    class Meta:
        model = Dictionary
        fields = ["word"]
