from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Dish
from .forms import CategoryForm, DishForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm, CustomUserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import DishForm, CategoryForm
from django.views import View
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomAuthenticationForm
import random

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile_view')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile_view')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def profile_view(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_view')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'profile.html', {'form': form})

def home(request):
    return render(request, 'home.html') 

def all_dishes(request):
    dishes = Dish.objects.all()
    return render(request, 'all_dishes.html', {'dishes': dishes})

def dish_detail(request, pk):
    dish = get_object_or_404(Dish, pk=pk)
    return render(request, 'dish_detail.html', {'dish': dish})

def category_dishes(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    dishes = category.dishes.all()
    return render(request, 'category_dishes.html', {'category': category, 'dishes': dishes})

def manage_dish(request, pk=None):
    dish = get_object_or_404(Dish, pk=pk) if pk else None
    if request.method == 'POST':
        form = DishForm(request.POST, instance=dish)
        if form.is_valid():
            form.save()
            return redirect('all_dishes')
    else:
        form = DishForm(instance=dish)
    return render(request, 'manage_dish.html', {'form': form})

def manage_category(request, pk=None):
    category = get_object_or_404(Category, pk=pk) if pk else None
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('all_dishes')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'manage_category.html', {'form': form})

def delete_dish(request, pk):
    dish = get_object_or_404(Dish, pk=pk)
    dish.delete()
    return redirect('all_dishes')

def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('all_dishes')

def search_dishes(request):
    query = request.GET.get('q', '')
    dishes = Dish.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
    return render(request, 'search_results.html', {'dishes': dishes, 'query': query})


from django.views.generic import ListView, DetailView
from .models import Dish, Category

class DishListView(ListView):
    model = Dish
    template_name = 'dish_list.html'
    context_object_name = 'dishes'
    paginate_by = 5
   
    def get_queryset(self):
        return Dish.objects.select_related('category')

class CategoryListView(ListView):
    model = Category
    template_name = 'category_list.html'
    context_object_name = 'categories'
    paginate_by = 10

class DishDetailView(DetailView):
    model = Dish
    template_name = 'dish_detail.html'
    context_object_name = 'dish'
   
    def get_queryset(self):
        return Dish.objects.select_related('category')

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category_detail.html'
    context_object_name = 'category'

class DishCreateView(CreateView):
    model = Dish
    form_class = DishForm
    template_name = 'dish_form.html'
    success_url = reverse_lazy('dish_list')

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category_form.html'
    success_url = reverse_lazy('category_list')

class DishUpdateView(UpdateView):
    model = Dish
    form_class = DishForm
    template_name = 'dish_form.html'
    success_url = reverse_lazy('dish_list')

class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category_form.html'
    success_url = reverse_lazy('category_list')


class DishDeleteView(DeleteView):
    model = Dish
    template_name = 'dish_confirm_delete.html'
    success_url = reverse_lazy('dish_list')

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'category_confirm_delete.html'
    success_url = reverse_lazy('category_list')


class RegisterView(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile_view')
        return render(request, 'register.html', {'form': form})

class LoginView(View):
    def get(self, request):
        form = CustomAuthenticationForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile_view')
        return render(request, 'login.html', {'form': form})


class HomeView(View):
    def get(self, request):
        categories = Category.objects.all()
        products = list(Dish.objects.all())
        random_products = random.sample(products, min(len(products), 8))  

        context = {
            'categories': categories,
            'random_products': random_products,
        }
        return render(request, 'home.html', context)