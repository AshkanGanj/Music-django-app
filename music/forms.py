from django import forms


class profile(forms.Form):
    name = forms.CharField()
    image = forms.ImageField()