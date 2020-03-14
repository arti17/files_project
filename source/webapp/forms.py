from django import forms

from webapp.models import File


class SearchForm(forms.Form):
    search = forms.CharField(max_length=60, required=False, label='Поиск')


class FullCreateFile(forms.ModelForm):
    class Meta:
        model = File
        exclude = ['author']


class AnonymousCreateFile(forms.ModelForm):
    class Meta:
        model = File
        exclude = ['author', 'access']
