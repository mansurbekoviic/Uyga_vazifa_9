from django import forms
from .models import Category, Dish
from django.core.validators import MinValueValidator
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Profile
from django.contrib.auth.forms import AuthenticationForm

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'avatar', 'address']

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        fields = ['username', 'password']

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone_number', 'password1', 'password2']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']

class DishForm(forms.ModelForm):
    price = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0.01)], 
    )

    class Meta:
        model = Dish
        fields = ['name', 'category', 'description', 'price']
