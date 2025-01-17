from django.urls import path
from .views import (
    DishListView, DishDetailView, DishCreateView, DishUpdateView, DishDeleteView,
    CategoryListView, CategoryDetailView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView,
    RegisterView, LoginView, HomeView
)
from django.conf import settings
from django.urls import include


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('dishes/', DishListView.as_view(), name='dish_list'),
    path('dishes/<int:pk>/', DishDetailView.as_view(), name='dish_detail'),
    path('dishes/create/', DishCreateView.as_view(), name='dish_create'),
    path('dishes/<int:pk>/update/', DishUpdateView.as_view(), name='dish_update'),
    path('dishes/<int:pk>/delete/', DishDeleteView.as_view(), name='dish_delete'),

    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('categories/create/', CategoryCreateView.as_view(), name='category_create'),
    path('categories/<int:pk>/update/', CategoryUpdateView.as_view(), name='category_update'),
    path('categories/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category_delete'),

    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
]

if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls')),
    ]
