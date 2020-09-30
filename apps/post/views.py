from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, TemplateView
from apps.post.models import Post,Comentario, Categoria
from django.urls import reverse_lazy, reverse
from apps.post.forms import PostForm, ComentarioForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from django.http import HttpResponseRedirect
from django.db.models import Q
from apps.usuarios.models import Usuario

import re

# Create your views here.

def LikeView(request, pk):
	post = get_object_or_404(Post, id=request.POST.get('post_id'))
	liked = False
	if post.likes.filter(id=request.user.id).exists():
		post.likes.remove(request.user)
		liked = False
	else:
		post.likes.add(request.user)
		liked = True
	
	return HttpResponseRedirect(reverse('MostrarPost', args=[str(pk)]))

#----------------------------------------------------- POST --------------------------------------------------------------------------

class PostAgregar(LoginRequiredMixin, CreateView):
	model = Post
	form_class = PostForm
	template_name = 'post/post_form.html'
	success_url = reverse_lazy('PosteosRecientes')

	login_url = settings.LOGIN_URL

	def form_valid(self, form):
		form.instance.usuario = self.request.user

		if form.instance.portada.name:
			ext = form.instance.portada.name.split(".")[-1]
			form.instance.portada.name = form.instance.titulo+'.'+ext
		return super().form_valid(form)



class PostEditar(LoginRequiredMixin, UpdateView):
	model = Post
	fields = [
			'titulo',
			'portada',	
			'contenido',
		]
	template_name = 'post/editar_post.html'
	success_url = reverse_lazy('PosteosRecientes')

	login_url = settings.LOGIN_URL

	def form_valid(self, form):
		form.instance.usuario = self.request.user

		if form.instance.portada.name:
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

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(**kwargs)

		stuff = get_object_or_404(Post,id=self.kwargs['pk'])
		total_likes = stuff.total_likes()

		liked = False
		if stuff.likes.filter(id=self.request.user.id).exists():
			liked = True

		context['total_likes'] = total_likes
		context['liked'] = liked


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


class PostEliminar(LoginRequiredMixin, DeleteView):
	model = Post
	success_url = reverse_lazy('PosteosRecientes')

def Buscador(request):
	return render(request,'buscar.html')
	


def BuscarPost(request):
	queryset = request.GET.get("buscar")
	posts = None
	if queryset:
		u = Usuario.objects.filter(username__icontains=queryset)
		posts = Post.objects.filter(
			Q(titulo__icontains= queryset) |
			Q(usuario__in = u)
			).distinct()
	return render(request,'buscar.html', {'posts':posts})

#----------------------------------------------------- COMENTARIO --------------------------------------------------------------------------

class ComentarioAgregar(LoginRequiredMixin, CreateView):
	model = Comentario
	form_class = ComentarioForm
	template_name = 'post/comment_form.html'
	success_url = reverse_lazy('PosteosRecientes')

	login_url = settings.LOGIN_URL

	def form_valid(self, form):
		x = form.save(commit = False)
		x.post_id = self.kwargs['pk']
		x.usuario = self.request.user
		x.save()
		return redirect(self.success_url)


