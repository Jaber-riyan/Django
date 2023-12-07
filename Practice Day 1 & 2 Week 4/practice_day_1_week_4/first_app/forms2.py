from django import forms
from . import models


class ModelOfFirst(forms.ModelForm):
    class Meta:
        model = models.ModelExample
        fields = '__all__'