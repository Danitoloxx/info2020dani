from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView
from apps.post.models import Post
from django.urls import reverse_lazy
from apps.post.forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings

import re


# Create your views here.
class PostAgregar(LoginRequiredMixin, CreateView):
	model = Post
	form_class = PostForm
	template_name = 'post/post_form.html'
	success_url = reverse_lazy('PosteosRecientes')

	login_url = settings.LOGIN_URL

	def form_valid(self, form):
		form.instance.usuario = self.request.user
		ext = form.instance.portada.name.split(".")[-1]
		form.instance.portada.name = form.instance.titulo+'.'+ext
		return super().form_valid(form)

class PostListar(ListView):
	model = Post
	paginate_by = 5
	ordering = ['-fecha_creacion']
	template_name = 'post/post_list.html'

class MostrarPost(DetailView):
	model = Post
	template_name = 'post/mostrar_post.html'

	def get_context_data(self, **kwargs): 
		context = super().get_context_data(**kwargs)

		bbcode = [
			'\[b](.*?)\[/b]',
            '\[i](.*?)\[/i]',
            '\[u](.*?)\[/u]',
            '\[url=(.*?)](.*?)\[/url]',                         
            '\[url](.*?)\[/url]',                             
            '\[center](.*?)\[/center]',
            '\[img](.*?)\[/img]',
            '\n',
		]

		htmlcode = [
			r'<strong>\1</strong>',
            r'<em>\1</em>',
            r'<u>\1</u>',
            r'<a rel="nofollow" target="_blank" class="link-naranja" href="\1">\2</a>',
            r'<a rel="nofollow" target="_blank" class="link-naranja" href="\1">\1</a>',
            r'<div style="text-align:center;">\1</div>',
            r'<img class="img-fluid mb-2 mt-2 rounded" src="\1" />',
            '<br/>',
		]

		i = 0
		for k, v in enumerate(bbcode):
			self.object.contenido = re.sub( v, htmlcode[ k ], self.object.contenido )
			i += 1

		return context
