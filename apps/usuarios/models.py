from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError


# Create your models here.

def validar_extension(valor):
	if not valor.name.endswith(settings.ALLOWED_IMG):
		raise ValidationError("Ese formato de imagen no esta permitido.")

class Provincia(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.nombre)

class Usuario(AbstractUser):
    universidad = models.CharField(max_length=50, null=True)
    ciudad = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='perfil/',null=True, blank=True, default=None, validators=[validar_extension])

    provincia = models.ForeignKey(Provincia, null=False, blank=False, on_delete=models.CASCADE)




