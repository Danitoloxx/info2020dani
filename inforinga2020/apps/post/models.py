from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError

# Create your models here.
def validar_extension(valor):
	if not valor.name.endswith(settings.ALLOWED_IMG):
		raise ValidationError("Ese formato de imagen no esta permitido.")

class Categoria(models.Model):
	id = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=50)

	def __str__(self):
		return '{}'.format(self.nombre)

class Post(models.Model):
	id = models.AutoField(primary_key=True)
	titulo = models.CharField(max_length=100)
	portada = models.ImageField(upload_to='post/', default='post/no-portada.jpg', validators=[validar_extension])
	fecha_creacion = models.DateTimeField(auto_now=True)	
	fecha_modificacion = models.DateTimeField(auto_now_add=True)
	contenido = models.TextField()

	categoria = models.ForeignKey(Categoria, null=False, blank=False, on_delete=models.CASCADE)
	usuario = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, blank=False, on_delete=models.CASCADE)

class Comentario(models.Model):
	id = models.AutoField(primary_key=True)
	fecha_creacion = models.DateTimeField(auto_now=True)
	contenido = models.TextField()

	usuario = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, blank=False, on_delete=models.CASCADE)
	post = models.ForeignKey(Post, null=False, blank=False, on_delete=models.CASCADE)