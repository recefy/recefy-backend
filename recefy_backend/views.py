# recefy_backend/views.py
from django.http import JsonResponse
import json


def ping(request):
    valor = 'jose'
    edad = 15
    
    concat = valor + str(edad) 

    return JsonResponse(
        {
            "mensaje": "dddsjose hola api",
            "concat": concat
        }
    )


