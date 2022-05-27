from django import forms
from django.forms import Form, ModelForm

from .models import Record


class RecordForm(ModelForm):
    class Meta:
        model = Record

        fields = ('title', 'content')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'title'}),
            'content': forms.Textarea(
                attrs={'class': 'form-control', 'cols': '30', 'rows': '10', 'placeholder': 'content'}
            )
        }
