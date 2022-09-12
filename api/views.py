from django.shortcuts import render
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from rest_framework.views import APIView
from .models import usuario
import json
from corsheaders.signals import check_request_enabled
# Create your views here.


class get_usuario(APIView):
    def get(self, request, *args, **kwargs):
        print(request.body)
        v_username = request.data['username']
        usuarios = list(usuario.objects.filter(username=v_username).values())
        if len(usuarios)>0:
            usuariox = usuarios[0]
            datos={"error":"0", "usuarios":usuariox}
        else:
            datos={'error':"1","msj":"not found"}
        return JsonResponse(datos)

