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
	portada = models.ImageField(upload_to='post/', null=True, blank=True,validators=[validar_extension])
	fecha_creacion = models.DateTimeField(auto_now=True)	
	fecha_modificacion = models.DateTimeField(auto_now_add=True)
	contenido = models.TextField()
	likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='likesPost')

	categoria = models.ForeignKey(Categoria, null=False, blank=False, on_delete=models.CASCADE)
	usuario = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, blank=False, on_delete=models.CASCADE)

	def __str__(self):
		return '%s - %s - %s' % (self.titulo, self.categoria, self.usuario)

	def total_likes(self):
		return self.likes.count()



class Comentario(models.Model):
	id = models.AutoField(primary_key=True)
	fecha_creacion = models.DateTimeField(auto_now=True)
	contenido = models.TextField()

	usuario = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, blank=False, on_delete=models.CASCADE)
	post = models.ForeignKey(Post, null=True, blank=False, on_delete=models.CASCADE, related_name='commentsPost')

	def __str__(self):
		return '%s - %s' % (self.post.titulo, self.usuario)
