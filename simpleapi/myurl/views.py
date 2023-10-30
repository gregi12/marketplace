from rest_framework import generics
from .models import Url
from .serializers import UrlSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets

@api_view(['POST'])
class UrlView(viewsets.ViewSet):
    queryset = Url.objects.all()
    serializer_class = UrlSerializer
    url = serializer_class.data
    Response(data={'url':url})
