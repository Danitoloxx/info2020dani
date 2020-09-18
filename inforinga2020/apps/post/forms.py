from django import forms
from apps.post.models import Post
from django.conf import settings

class PostForm(forms.ModelForm):

	class Meta:
		model = Post

		fields = [
			'titulo',
			'portada',	
			'contenido',
			'categoria',
		]

		labels = {
			'titulo': 'Ingrese el Titulo',
		}
