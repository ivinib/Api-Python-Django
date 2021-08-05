import json
import re
from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.decorators import api_view

from dados.models import Dado
from dados.serializers import DadoSerializer

@api_view(['GET', 'POST'])
def dados_list(request):
    if request.method == 'GET':
        dados = Dado.objects.all()
        dados_serializer = DadoSerializer(dados, many=True)
        return JsonResponse(dados_serializer.data, safe=False)

    elif request.method == 'POST':
        dado_data = JSONParser().parse(request)
        dado_serializer = DadoSerializer(data=dado_data)
        if dado_serializer.is_valid():
            dado_serializer.save()
            return JsonResponse(dado_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(dado_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def dado_detail(request,pk):
    try:
        dado = Dado.objects.get(pk=pk)
        if request.method == 'GET':
            dado_serializer = DadoSerializer(dado)
            return JsonResponse(dado_serializer.data)
        elif request.method == 'PUT':
            dado_data = JSONParser().parse(request)
            dado_serializer = DadoSerializer(dado, data=dado_data)
            if dado_serializer.is_valid():
                dado_serializer.save()
                return JsonResponse(dado_serializer.data)
            return JsonResponse(dado_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            dado.delete()
            return JsonResponse({'message': 'O Dado foi deletado com sucesso'}, status=status.HTTP_204_NO_CONTENT)
    except Dado.DoesNotExist:
        return JsonResponse({'message': 'O dado não existe'}, status = status.HTTP_404_NOT_FOUND)