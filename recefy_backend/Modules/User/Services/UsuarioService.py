from django.http import JsonResponse

def usuarioService(request):
    valor = 'jose'
    edad = 15
    
    concat = valor + str(edad) 

    return JsonResponse(
        {
            "mensaje": "dddsjose hola api",
            "concat": concat
        }
    )