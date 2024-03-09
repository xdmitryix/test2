from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'Категория: {self.name}'


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    steps = models.TextField()
    time = models.DecimalField(max_digits=3, decimal_places=2)
    image = models.ImageField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category_recipe = models.ForeignKey(Category, on_delete=models.CASCADE)
    time_date_add = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Название рецепта: {self.name}'
