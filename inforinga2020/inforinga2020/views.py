from django.shortcuts import render

def Home(request):
    return render(request,'index.html')

def Login(request):
    return render(request,'usuarios/login.html')
