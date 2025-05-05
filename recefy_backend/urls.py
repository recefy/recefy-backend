# recefy_backend/routes.py
from django.urls import path
from recefy_backend.Modules.User.Services.UsuarioService import usuarioService

urlpatterns = [
    path('api/jose/', usuarioService, name='usuarioService')
]
