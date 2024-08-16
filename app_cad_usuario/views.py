from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password
from .models import usuarios
from .forms import formCadastro, formLogin

# Create your views here.
def login(request):
    if request.method == "POST":
        form = formLogin(request.GET)
        if form.is_valid():
            username = form.data['username']
            email = form.data['email']
            password = form.data['password']
            try:
                user = usuarios.objects.get(username=username, password=password)
                if check_password(password, user.password):
                    login(request, user)
                    return redirect('home')
            except:
                form.add_error(None, "Usuário ou senha incorretos")
    else:
        form = formLogin()

    
    return render(request, 'account/login.html', {'form': form})

def home(request):
    return render(request, 'home/home.html')

def cadastro(request):
    # Django Forms
    form = formCadastro(request.POST)
    if form.is_valid():
        form.save()
        user = form.data['username']
        email = form.data['email']
    return render(request, 'account/cadastro.html', {'form': form})