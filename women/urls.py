from django.urls import path

from .views import WomenApiView
urlpatterns = [
    path('api/v1/womenlist/', WomenApiView.as_view(), name='womenlist'),
]