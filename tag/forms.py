from django import forms

class DocumentForm(forms.Form):
    name = forms.CharField()
    comment = forms.CharField(widget=forms.Textarea)