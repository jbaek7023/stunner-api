from rest_framework import serializers
from .models import Restaurant
from menu.serializer import MenuSerializer

class RestaurantSerializer(serializers.ModelSerializer):
    menus = MenuSerializer(read_only=True, many=True)
    img = serializers.SerializerMethodField()
    class Meta:
        model = Restaurant
        fields = ('name', 'id', 'menus', 'cuisine', 'longitude', 'latitude', 'rate', 'img', 'link',)

    def get_img(self, obj):
        print(obj)
        print(obj.image)
        if obj.image:
            request = self.context.get('request')
            return request.build_absolute_uri(obj.image.url)
        return None