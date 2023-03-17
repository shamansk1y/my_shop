from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('sub/<int:product_id>/', views.cart_sub, name='cart_sub'),
    path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
]
