from django import forms

class InputForm(forms.Form):
    link = forms.CharField()