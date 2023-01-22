from django.urls import path

from .views import WomenApiList, WomenApiUpdate
urlpatterns = [
    path('api/v1/womenlist/', WomenApiList.as_view(), name='womenlist'),
    path('api/v1/womenlist/<int:pk>/', WomenApiUpdate.as_view(), name='womenlistpk'),
]