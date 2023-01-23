from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Women, Category
from .serializer import WomenSerializer


class WomenViewSet(viewsets.ModelViewSet):
    serializer_class = WomenSerializer

    # переопределяет queryset
    def get_queryset(self):
        pk = self.kwargs['pk']
        if not pk:
            return Women.objects.all()[:3]
        return Women.objects.filter(pk=pk)

    # добаляет нестандартный url к списку url из viewset
    @action(methods=['post', 'get'], detail=True)
    def category(self, request, pk):
        cats = Category.objects.get(pk=pk)
        return Response({'cats': cats.name})

# class WomenApiList(generics.ListCreateAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#
#
# class WomenApiUpdate(generics.UpdateAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#
#
# class WomenApiDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer


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
