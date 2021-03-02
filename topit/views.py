from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from topit.models import Magic
from topit.serializers import MagicSerializer
from rest_framework.decorators import api_view
# Create your views here.


@api_view(['GET', 'POST', 'DELETE'])
def magic_list(request):
    if request.method == 'GET':
        magic = Magic.objects.all()

        title = request.GET.get('title', None)
        if title is not None:
            magic = magic.filter(title__icontains=title)

        magic_serializer = MagicSerializer(magic, many=True)
        return JsonResponse(magic_serializer.data, safe=False)

    elif request.method == 'POST':
        magic_data = JSONParser().parse(request)
        magic_serializer = MagicSerializer(data=magic_data)
        if magic_serializer.is_valid():
            magic_serializer.save()
            return JsonResponse(magic_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(magic_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def magic_detail(request, pk):

    try:
        magic = Magic.objects.get(pk=pk)
    except Magic.DoesNotExist:
        return JsonResponse({'message': 'This listing has vanished'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        magic_serializer = MagicSerializer(magic)
        return JsonResponse(magic_serializer.data)

    elif request.method == 'PUT':
        magic_data = JSONParser().parse(request)
        magic_serializer = MagicSerializer(magic, data=magic_data)
        if magic_serializer.is_valid():
            magic_serializer.save()
            return JsonResponse(magic_serializer.data)
        return JsonResponse(magic_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def magic_list_published(request):
