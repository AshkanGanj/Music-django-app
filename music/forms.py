from django import forms
from .models import Profile, User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email'
        ]


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'image',
            'location',
            'birth_date'
        ]
