from django import forms
from .models import Photo
from pyuploadcare.dj.forms import ImageField

class PhotoForm(forms.ModelForm):
    photo = ImageField(label='photo')
    class Meta:
        model = Photo
        fields=('title', 'photo')