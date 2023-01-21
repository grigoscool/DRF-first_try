from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Women
from .serializer import WomenSerializer


class WomenApiView(APIView):
    def get(self, request):
        content = Women.objects.all().values()
        return Response({'title': list(content)})

    def post(self, request):
        post_new = Women.objects.create(
            title=request.data['title'],
            cat_id=request.data['cat_id'],
        )
        print(model_to_dict(post_new))
        return Response({'title': model_to_dict(post_new)})
# class WomenApiView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
