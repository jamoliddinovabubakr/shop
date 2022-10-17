from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Product
from .forms import AddProductForm, BuyProductForm, EditProductForm

# Create your views here.

menu = [
    {'title': 'All products', 'url_name': 'home'},
    {'title': 'Create product', 'url_name': 'create_product'}
]


def index(request):
    products = Product.objects.all()
    context = {
        'products': products,
        'menu': menu,
        'title': 'Home page'

    }
    return render(request, 'product/index.html', context=context)


def create_product(request):
    if request.method == 'POST':
        form = AddProductForm(request.POST)
        if form.is_valid():
            try:
                Product.objects.create(**form.cleaned_data)
                return redirect('home')
            except:
                form.add_error(None, 'Ошибка добавления поста')
    else:
        form = AddProductForm()

    context = {
        'title': 'Create product',
        'menu': menu,
        'form': form
    }
    return render(request, 'product/createproduct.html', context=context)


def edit_product(request, product_id):
    product = Product.objects.get(pk=product_id)
    if request.method == 'POST':
        form = EditProductForm(request.POST)
        if form.is_valid():
            product.name = request.POST['name']
            product.inStock = int(request.POST['inStock'])
            product.save()
            return redirect('home')
        else:
            form.add_error(None, 'Error name or inStock')
    else:
        form = EditProductForm()

    context = {
        'menu': menu,
        'product': product,
        'form': form
    }
    return render(request, 'product/editproduct.html', context=context)


def buy_product(request, product_id):
    product = Product.objects.get(pk=product_id)
    if request.method == 'POST':
        form = BuyProductForm(request.POST)
        if form.is_valid():
            tmp = product.inStock - int(request.POST['inStock'])
            if tmp > 0:
                product.inStock = tmp
                product.save()
                return redirect('home')
            else:
                form.add_error(None, 'Error Stock')
    else:
        form = BuyProductForm()
    context = {
        'menu': menu,
        'product': product,
        'title': 'Buy create',
        'form': form
    }
    return render(request, 'product/product.html', context=context)


def delete_product(request, product_id):
    member = Product.objects.get(id=product_id)
    member.delete()
    return HttpResponseRedirect(reverse('home'))
