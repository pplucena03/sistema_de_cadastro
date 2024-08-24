from django.urls import path
from . import views

urlpatterns = [
    path('home/',  views.home, name='home'),
    path('',  views.login_view, name='login'),
    path('cadastro/',  views.cadastro, name='cadastro'),
]