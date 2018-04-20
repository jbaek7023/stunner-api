from rest_framework import serializers
from .models import Restaurant
from menu.serializer import MenuSerializer

class RestaurantSerializer(serializers.ModelSerializer):
    menus = MenuSerializer(read_only=True, many=True)

    class Meta:
        model = Restaurant
        fields = ('name', 'id', 'menus', 'cuisine', 'longitude', 'latitude', 'rate', 'image')
