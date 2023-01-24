from django.urls import path, include, re_path
from rest_framework import routers

from .views import WomenViewSet

router = routers.SimpleRouter()
router.register(r'women', WomenViewSet, basename='women')

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    # path('api/v1/womenlist/', WomenViewSet.as_view({'get': 'list'}), name='womenlist'),
    # path('api/v1/womenlist/<int:pk>/', WomenViewSet.as_view({'get': 'list', 'put': 'update'}), name='womenlistpk'),

    # path('api/v1/womenlist/<int:pk>/', WomenApiUpdate.as_view(), name='womenlistpk'),
    # path('api/v1/womendetailview/<int:pk>/', WomenApiDetailView.as_view(), name='womenlistpk'),

]
