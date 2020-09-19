from django.shortcuts import render

def Home(request):
    return render(request,'index.html')

def Login(request):
    return render(request,'usuarios/login.html')

def Perfil(request):
    args = {'user': request.user}
    return render(request, 'usuarios/perfil.html', args)

