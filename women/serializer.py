from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Women


class WomenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Women
        fields = '__all__'


