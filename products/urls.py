
from django.contrib import admin
from django.urls import include, path

from products import views

urlpatterns = [
    path('add-to-cart/', views.add_to_cart, name='add_to_cart'),
    path('view-cart/', views.view_cart, name='view_cart'),
    path('', views.product_list, name="product_list"),
    path('<int:id>/', views.product_detail, name="product_detail"),
    path('categories/', views.category_list, name="category_list"),
]
