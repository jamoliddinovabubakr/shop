from django.contrib import admin
from .models import Product


# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'inStock', 'price')
    list_display_links = ('name',)
    search_fields = ('name',)
    list_filter = ('inStock', 'price')


admin.site.register(Product, ProductAdmin)
