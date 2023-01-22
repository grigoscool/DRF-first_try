from django.urls import path

from .views import WomenApiList
urlpatterns = [
    path('api/v1/womenlist/', WomenApiList.as_view(), name='womenlist'),
    path('api/v1/womenlist/<int:pk>/', WomenApiList.as_view(), name='womenlistpk'),
]