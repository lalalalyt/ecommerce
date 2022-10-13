from django.shortcuts import get_object_or_404, render

from .models import Category, Product


def product_all(request):
    products = Product.objects.filter(is_active=True)
    return render(request, 'store/home.html', {'products': products})


def product_detail(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    return render(request, 'store/products/productDetail.html', {'product': product})


def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'store/products/category.html', {'category': category, 'products': products})
