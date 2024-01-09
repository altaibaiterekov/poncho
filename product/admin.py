from django.contrib import admin

from product.models import Product, ProductImage

# Register your models here.


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]


# TODO - check the limits on the number of photos
# TODO - serializers
# TODO - views
# TODO - category ?
# TODO - average rating
