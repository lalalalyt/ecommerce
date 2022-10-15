from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

from .basket import Basket
from store.models import Product


def basket_summary(request):
    return render(request, 'basket/summary.html')


def basket_add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'add':
        product_id = int(request.POST.get('product_id'))
        product_qty=int(request.POST.get('product_qty'))
        product = get_object_or_404(Product, id=product_id)
        basket.add(product=product,qty=product_qty)
        basket_qty=basket.__len__()
        response = JsonResponse({'qty':basket_qty})
        return response

def basket_delete(request):
    basket = Basket(request)
    if request.POST.get('action') == 'delete':
        product_id = request.POST.get('product_id')
        basket.delete(product_id=product_id)
        totalQty=basket.__len__()
        subtotal=basket.get_total_price()
        return JsonResponse({'totalQty':totalQty,'subtotal':subtotal})

def basket_update(request):
    basket = Basket(request)
    if request.POST.get('action') == 'update':
        product_id = request.POST.get('product_id')
        product_qty = request.POST.get('product_qty')
        basket.update(product_id=product_id,qty=product_qty)
        totalQty=basket.__len__()
        subtotal=basket.get_total_price()
        return JsonResponse({'totalQty':totalQty,'subtotal':subtotal})
