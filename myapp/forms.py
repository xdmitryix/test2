from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import Recipe, Category


class UserForm(forms.Form):
    login = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(min_length=8)


class RegistrationForm(forms.Form):
    login = forms.CharField(max_length=100, )
    email = forms.EmailField()
    password1 = forms.CharField(widget=forms.PasswordInput(), min_length=8, max_length=100)
    password2 = forms.CharField(widget=forms.PasswordInput(), min_length=8, max_length=100)



class SignUpForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(), min_length=8, max_length=100)
    password2 = forms.CharField(widget=forms.PasswordInput(), min_length=8, max_length=100)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 != password2:
            raise forms.ValidationError("Пароли не совпадают")
        return password2


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'description', 'steps', 'time', 'image', 'category_recipe']


class Recipes_showForm(forms.Form):
    category = forms.ModelChoiceField(queryset=Category.objects.all())


class RecipeFormRedact(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'description', 'steps', 'time', 'image', 'category_recipe']



