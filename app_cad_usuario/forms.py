from django import forms
from .models import usuarios

class formCadastro(forms.ModelForm):
    class Meta:
        model = usuarios
        fields = ['username', 'email', 'password', 'date_of_birth']

class formLogin(forms.ModelForm):
    class Meta:
        model = usuarios
        fields = ['username', 'email', 'password']