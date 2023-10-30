from rest_framework import routers
from django.urls import path, include
from .views import ItemViewSet

router = routers.DefaultRouter()
router.register(r'items', ItemViewSet)


urlpatterns = [
    path('api/',include(router.urls)),
    path('api-auth/',include('rest_framework.urls',namespace='rest_framework')),
]