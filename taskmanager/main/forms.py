from .models import IdentificationUser
from django.forms import ModelForm, TextInput


class UserForm(ModelForm):
    class Meta:
        model = IdentificationUser
        fields = ["first_name", "last_name"]
        widgets = {
            "first_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введи своє імя'
            }),
            "last_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введи своє прізвище'
            })
        }
