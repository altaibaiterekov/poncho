from django.contrib.auth import get_user_model
from django.db import models
from product.models import Product

User = get_user_model()


class Review(models.Model):
    RATING_CHOICES = (
        (1, 'Очень плохо'),
        (2, 'Плохо'),
        (3, 'Нормально'),
        (4, 'Хорошо'),
        (5, 'Отлично'),
        (6, 'Очень хорошо'),
        (7, 'Превосходно'),
        (8, 'Замечательно'),
        (9, 'Идеально'),
        (10, 'Превосходно')
    )
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
    body = models.TextField()
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['author', 'product']

