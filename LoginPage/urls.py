from django.contrib import admin
from django.urls import path
from app_cad_usuario import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',  views.home, name='home'),
    path('',  views.login, name='login'),
    path('cadastro/',  views.cadastro, name='cadastro'),
    path('user/<str:name>', views.user, name='userpage'),
]