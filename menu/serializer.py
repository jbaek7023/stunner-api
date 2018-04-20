from rest_framework import serializers
from .models import Menu


class MenuSerializer(serializers.ModelSerializer):
    img = serializers.SerializerMethodField()

    class Meta:
        model = Menu
        fields = (
            'id',
            'price',
            'description',
            'review_count',
            'current_rate',
            'img',
            'name',
            'link',
        )

    def get_img(self, obj):
        print(obj)
        print(obj.image)
        if obj.image:
            request = self.context.get('request')
            return request.build_absolute_uri(obj.image.url)
        return None