from django.urls import path

from .views import WomenApiList, WomenApiUpdate, WomenApiDetailView
urlpatterns = [
    path('api/v1/womenlist/', WomenApiList.as_view(), name='womenlist'),
    path('api/v1/womenlist/<int:pk>/', WomenApiUpdate.as_view(), name='womenlistpk'),
    path('api/v1/womendetailview/<int:pk>/', WomenApiDetailView.as_view(), name='womenlistpk'),

]