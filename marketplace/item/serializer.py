from .models import Item

from rest_framework import serializers

class ItemSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:

        model = Item
        fields = ['category','name','description','image','price','is_sold','created_by','created_at']
