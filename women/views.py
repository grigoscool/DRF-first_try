from django.shortcuts import render
from rest_framework import generics

from .models import Women
from .serializer import WomenSerializer


class WomenApiView(generics.ListAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
