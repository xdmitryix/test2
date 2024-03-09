from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, get_object_or_404
from .forms import UserForm, RegistrationForm
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from .forms import SignUpForm, RecipeForm, Recipes_showForm, RecipeFormRedact
from .models import Category, Recipe
from random import sample
from django.template.defaultfilters import mark_safe
from django.utils.html import mark_safe
from django.contrib.auth.decorators import login_required





def index(request: HttpRequest):
    recipes = list(Recipe.objects.all())
    if len(recipes) < 5:
        return render(request, 'myapp/index.html', {'recipes': recipes})
    recipes_rnd = sample(recipes, 5)
    return render(request, 'myapp/index.html', {'recipes': recipes_rnd})


def user_login(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['login']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
    else:
        form = UserForm()
    return render(request, 'myapp/login.html', {'form': form})



def registration_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data.get('username')
            user_mail = form.cleaned_data.get('email')
            user_pass = form.cleaned_data.get('password1')
            user = User.objects.create_user(username=user_name, email=user_mail, password=user_pass)
            user.save()
            return redirect('/registration_user/registration_success/')
    else:
        form = SignUpForm()
    return render(request, 'myapp/registration_user.html', {'form': form})


def registration_success(request):
    return render(request, 'myapp/registration_success.html')



def recipes_category(request):
    if request.method == 'POST':
        form = Recipes_showForm(request.POST)
        if form.is_valid():
            category = form.cleaned_data['category']
            recipes = Recipe.objects.filter(category_recipe=category)
    else:
        form = Recipes_showForm()
        recipes = Recipe.objects.all()

    return render(request, 'myapp/recipes_category.html', {'form': form, 'recipes': recipes})


@login_required
def recipe_add(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            image = form.cleaned_data.get('image')
            if image:
                fs = FileSystemStorage()
                fs.save(image.name, image)
            recipe.save()
            return redirect('/recipe_add_success')
    else:
        form = RecipeForm()
    return render(request, 'myapp/recipe_add.html', {'form': form})


@login_required
def recipe_add_success(request):
    return render(request, 'myapp/recipe_add_success.html')


def recipe_show(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    return render(request, 'myapp/recipe_show.html', {'recipe': recipe})


@login_required
def my_recipes(request):
    recipes = Recipe.objects.filter(author=request.user)
    return render(request, 'myapp/my_recipes.html', {'recipes': recipes})


@login_required
def recipe_redact(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    if request.method == 'POST':
        form = RecipeFormRedact(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            image = form.cleaned_data.get('image')
            if image:
                fs = FileSystemStorage()
                fs.save(image.name, image)
            else:
                recipe.image = recipe.image
            recipe.save()
            return redirect('/recipe_redact_success')
    else:
        form = RecipeFormRedact(instance=recipe)
    return render(request, 'myapp/recipe_add.html', {'form': form})


@login_required
def recipe_redact_success(request):
    return render(request, 'myapp/recipe_redact_success.html')