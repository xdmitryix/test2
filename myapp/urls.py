from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('registration_user/', views.registration_user, name='registration_user'),
    path('registration_user/registration_success/', views.registration_success, name='registration_success'),
    path('recipes_category/', views.recipes_category, name='recipes_category'),
    path('my_recipes/', views.my_recipes, name='my_recipes'),
    path('recipe_add/', views.recipe_add, name='recipe_add'),
    path('recipe_add_success/', views.recipe_add_success, name='recipe_add_success'),
    path('recipe_redact/<int:recipe_id>/', views.recipe_redact, name='recipe_redact'),
    path('recipe_redact_success/', views.recipe_redact_success, name='recipe_redact_success'),
    path('recipe/<int:recipe_id>/', views.recipe_show, name='recipe_show'),
]