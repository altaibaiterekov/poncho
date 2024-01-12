from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.response import Response

from product.models import Product, ProductImage
from product.permissions import IsOwner, IsOwnerOrAdmin
from product.serializers import ProductSerializer, ProductImageSerializer, ProductListSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list':
            return ProductListSerializer
        return ProductSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [IsAuthenticated()]
        elif self.action == 'destroy':
            return [IsOwnerOrAdmin()]
        elif self.action in ('partial_update', 'update'):
            return [IsOwner()]
        return [AllowAny()]


# class ProductImageViewSet(viewsets.ModelViewSet):
#     queryset = ProductImage.objects.all()
#     serializer_class = ProductImageSerializer
#
#     def perform_create(self, serializer):
#         product_id = self.request.data.get('product')  # Получаем ID продукта из запроса
#         if product_id:
#             product = Product.objects.get(pk=product_id)
#             max_images_per_product = 8
#
#             if product.images.count() >= max_images_per_product:
#                 return Response({'error': f'Невозможно добавить больше изображений для продукта {product.title}'},
#                                 status=status.HTTP_400_BAD_REQUEST)
#
#         serializer.save()

