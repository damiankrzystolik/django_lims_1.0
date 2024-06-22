from django import forms
from . import models

class CreateClient(forms.ModelForm):
    class Meta:
        model = models.Client
        fields = ['name', 'address', 'slug', 'banner']

class ClientForm(forms.ModelForm):  # wiem, powtarza się
    class Meta:
        model = models.Client
        fields = ['name', 'address', 'author', 'banner']