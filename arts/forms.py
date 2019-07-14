from django import forms
from django.contrib.auth.models import User

from .models import Art

class ArtForm(forms.ModelForm):

    class Meta:
        model = Art
        fields = ['title', 'description','area','picture']

