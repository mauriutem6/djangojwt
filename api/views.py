from django.shortcuts import render
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from rest_framework.views import APIView
from .models import usuario
import json
from corsheaders.signals import check_request_enabled
import shutil
from django.db.models.signals import pre_delete
from django.dispatch import receiver
# Create your views here.


class get_usuario(APIView):
    @method_decorator(csrf_exempt)
    def post(self, request):
        #print("invoca get")
        print(request.body)
        jd = json.loads(request.body)
        vid = jd['id']
        print("---")
        print(vid+vid)
        #v_username = request.data['username']
        usuarios = list(usuario.objects.filter(id=vid).values())
        if len(usuarios) > 0:
            usuariox = usuarios[0]
            datos = {"error": "0", "usuarios": usuariox}
        else:
            datos = {'error': "1", "msj": "not found"}
        return JsonResponse(datos)

    def put(self, request):
        #print("invoca get")
        print(request.body)
        jd = json.loads(request.body)
        vid = jd['id']
        vusername_ = jd['username']
        vemail = jd['email']
        vdireccion_calle = jd['direccion_calle']
        vdireccion_numero = jd['direccion_numero']

        if (vid > 0):
            print("update*****************************")

            # insert into probar
            p = usuario(
                id=vid,
                username=vusername_,
                email=vemail,
                direccion_calle=vdireccion_calle,
                direccion_numero=vdireccion_numero
            )
            p.save()
        else:
            idx = usuario.objects.latest('id').id + 1
            obj_instance = usuario.objects.create(
                id=idx,
                username=vusername_,
                email=vemail,
                direccion_calle=vdireccion_calle,
                direccion_numero=vdireccion_numero
            )
            print("insert*****************************")
        datos = {'error': "0", "msj": "success"}
        return JsonResponse(datos)

    @receiver(pre_delete)
    def delete(self, request, *args, **kwargs):
        #otro = self.kwargs['otro']

        #instance = kwargs.get('instance')
        #id    = instance.id
        print(self.kwargs)
        datos = {'error': "0", "msj": "delete success"}
        return JsonResponse(datos)


class get_usuarios(APIView):
    def get(self, request):
        # print(request.body)
        #v_username = request.data['username']
        usuarios = list(usuario.objects.values())
        if len(usuarios) > 0:
            datos = {"message": "success", "usuarios": usuarios}
        else:
            datos = {'message': "usuario not found..."}
        return JsonResponse(datos)
