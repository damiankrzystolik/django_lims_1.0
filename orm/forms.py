from django import forms
from . import models

class CreateClient(forms.ModelForm):
    class Meta:
        model = models.Client
        fields = ['name', 'address', 'slug', 'banner']