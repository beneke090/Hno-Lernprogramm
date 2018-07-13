from django import forms
from ckeditor.widgets import CKEditorWidget


class ArtikelForm(forms.Form):
    subject = forms.CharField()
    email = forms.EmailField(required=False)
    message = forms.CharField()
    content = forms.CharField(widget=CKEditorWidget())
