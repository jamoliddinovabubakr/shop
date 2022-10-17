from django.urls import path
from .views import index, create_product, edit_product, buy_product, delete_product

urlpatterns = [
    path('', index, name='home'),
    path('createproduct', create_product, name='create_product'),
    path('editproduct/<int:product_id>/', edit_product, name='edit_product'),
    path('buyproduct/<int:product_id>/', buy_product, name='product'),
    path('delete/<int:product_id>/', delete_product, name='delete'),
]
