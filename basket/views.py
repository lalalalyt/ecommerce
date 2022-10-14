from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

from .basket import Basket
from store.models import Product


def basket_summary(request):
    return render(request, 'store/basket/summary.html')


def basket_add(request):
    basket = Basket(request)
    if request.method == 'POST':
        product_id = int(request.POST.get('product_id'))
        product_Qty=int(request.POST.get('product_Qty'))
        product = get_object_or_404(Product, id=product_id)
        basket.add(product=product,Qty=product_Qty)
        response = JsonResponse({'qty':product_Qty})
        return response
