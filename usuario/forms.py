from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Usuario
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class UsuarioForm(UserCreationForm):

    class Meta:
        model = Usuario
        fields = (
            'username',
            'email',
            'password1'
        )

    def clean_email(self):
        e = self.cleaned_data['email']
        if User.objects.filter(email = e).exists():
            raise ValidationError('esse email já está em uso')
            print('wwwww')
        else:
            return e



class EditUser(UserChangeForm):
    class Meta:
        model = Usuario
        fields = (
            'first_name',
            'last_name',
            'cidade',
            'telefone',
            'cpf' 
        )


class EditSenha(UserChangeForm):
    class Meta:
        model = Usuario
        fields = (
            'username',
            'password',
        )



