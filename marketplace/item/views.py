from django.shortcuts import render, get_list_or_404
from .models import Item
from rest_framework import viewsets
from .serializer import ItemSerializer
# Create your views here.

def detail(request,pk):
    item = get_list_or_404(Item, pk=pk)
    return render(request, "item/detail.html" ,{
        'item':item,
    })

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer