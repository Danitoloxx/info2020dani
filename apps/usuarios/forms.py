from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordResetForm
from .models import Usuario

class RegistroUsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'provincia',
            'ciudad',
            'universidad',
            'password1',
            'password2',
        ]

class EditarUsuarioForm(UserChangeForm):
    class Meta:
        model = Usuario
        fields = [
            'email',
            'imagen',
            'first_name',
            'last_name',
            'provincia',
            'ciudad',
            'universidad'
        ]