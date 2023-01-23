from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Women
from .serializer import WomenSerializer


class WomenApiList(generics.ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer


class WomenApiUpdate(generics.UpdateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer


class WomenApiDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
# class WomenApiView(APIView):
#     def get(self, request):
#         content = Women.objects.all()
#         return Response({'title': WomenSerializer(content, many=True).data})
#
#     def post(self, request):
#         serializer = WomenSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response({'title': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response("no such post")
#
#         try:
#             post = Women.objects.get(pk=pk)
#         except:
#             return Response("no such post")
#
#         serializer = WomenSerializer(data=request.data, instance=post)
#         serializer.is_valid(raise_exception=True)
#         # метод save автом вызывает методы из сериализатора в зависимости от кол-ва аргументов
#         serializer.save()
#         return Response({'post': serializer.data})
#
