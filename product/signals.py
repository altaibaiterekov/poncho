# from django.db.models.signals import pre_save
# from django.dispatch import receiver
# from django.core.exceptions import ValidationError
#
# from product.models import ProductImage
#
#
# @receiver(pre_save, sender=ProductImage)
# def limit_product_images(sender, instance, **kwargs):
#     max_images_per_product = 8
#
#     if instance.product.images.count() >= max_images_per_product:
#         raise ValidationError(f"Невозможно добавить больше изображений для продукта '{instance.product.title}'")
