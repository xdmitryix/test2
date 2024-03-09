from django.contrib import admin
from .models import Category, Recipe


class CategoryAdmin(admin.ModelAdmin):
    """Список категорий"""
    list_display = ['name']
    ordering = ['name']
    list_filter = ['name']
    search_fields = ['name']


class RecipeAdmin(admin.ModelAdmin):
    """Список Рецептов"""
    list_display = ['name', 'author', 'category_recipe', 'time_date_add']
    ordering = ['name', 'author', 'category_recipe', 'time_date_add']
    list_filter = ['name', 'author', 'category_recipe', 'time_date_add']
    search_fields = ['name']



admin.site.register(Category, CategoryAdmin)
admin.site.register(Recipe, RecipeAdmin)

