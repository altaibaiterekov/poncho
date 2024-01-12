from random import randint

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Product(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    preview = models.ImageField(upload_to='previews/', null=True, blank=True, default='previews/default_preview.jpg')
    owner = models.ForeignKey(User, related_name='products', on_delete=models.RESTRICT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True)

    @staticmethod
    def generate_name():
        return 'image' + str(randint(100000, 999999))

    def save(self, *args, **kwargs):
        self.name = self.generate_name()
        return super(ProductImage, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.name} -> {self.product}'
