#!/root/myenv1/bin python3.5
# -*- coding: utf-8 -*-

from django import forms
from .models import MyPhoto

class PubPhotoForm(forms.ModelForm):
    class Meta:
        model=MyPhoto
        fields=['title','description','photo']