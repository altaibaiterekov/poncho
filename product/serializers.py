from rest_framework import serializers
from .models import Product, ProductImage


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')
    images = ProductImageSerializer(many=True, required=False)

    class Meta:
        model = Product
        fields = '__all__'

    def validate_images(self, value):
        MAX_IMAGES = 8
        if len(value) > MAX_IMAGES:
            raise serializers.ValidationError(f'max images = {MAX_IMAGES}')
        return value


class ProductListSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')

    class Meta:
        model = Product
        fields = ('id', 'title', 'preview', 'owner', 'price', )
