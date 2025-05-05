# recefy_backend/routes.py
from django.urls import path
from django.views.decorators.http import require_GET, require_POST
from .views import ping, echo


urlpatterns = [
    path('api/ping/', require_GET(ping), name='api_ping'),
    path('api/echo/', echo, name='api_echo'),
]
7