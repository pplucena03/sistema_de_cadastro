from django.shortcuts import render, redirect
from .models import usuarios

# Create your views here.

def home(request):
    return render(request, 'home/index.html')

def login(request):
    return render(request, 'account/login.html')

def cadastro(request):
    if request.method == 'POST':
        name = request.POST.get('nome')
        print(name)
        email = request.POST.get('email')
        print(email)
        senha = request.POST.get('senha')
        print(senha)
        aniversario = request.POST.get('aniversario')
        
        new_data = usuarios(username=name, email=email, password=senha, date_of_birth=aniversario)
        new_data.save()
        
        return redirect('home/index.html')  

    return render(request, 'account/cadastro.html')

def user(request, name):
    name = request.POST.get('nome')
    return render(request, 'user/userpage.html', {'name': name})