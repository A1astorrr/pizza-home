from django.urls import path

from goods import views

app_name = "goods"  # для подгрузки файлов из папки main

urlpatterns = [
    path('', views.menu, name='menu'),
    path('product/<slug:product_slug>/', views.product, name='product'),

    
]