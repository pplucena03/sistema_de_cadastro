from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import formCadastro, formLogin

def login_view(request): 
    if request.method == "POST":
        form = formLogin(request.POST)

        if form.is_valid():
            user = form.cleaned_data['user']
            login(request, user)
            messages.success(request, 'Sucesso!')
            return redirect('home/')
        
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
    return render(request, 'account/cadastro.html', {'form': form})