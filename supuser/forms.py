from django import forms
from ckeditor.widgets import CKEditorWidget
from lernen.models import Artikel, Kapitel


class ArtikelForm(forms.Form):
    title = forms.CharField()
    unterschrift = forms.CharField(required=False)
    field1 = forms.ModelChoiceField(queryset=Kapitel.objects.all(), empty_label="(Nothing)")
    message = forms.CharField()
    content = forms.CharField(widget=CKEditorWidget())
