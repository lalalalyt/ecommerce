from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

from .basket import Basket
from store.models import Product


def basket_summary(request):
    return render(request, 'store/basket/summary.html')


def basket_add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'add':
        product_id = int(request.POST.get('product_id'))
        product_Qty=int(request.POST.get('product_Qty'))
        product = get_object_or_404(Product, id=product_id)
        basket.add(product=product,Qty=product_Qty)
        basket_Qty=basket.__len__()
        response = JsonResponse({'qty':basket_Qty})
        return response

def basket_delete(request):
    basket = Basket(request)
    if request.POST.get('action') == 'delete':
        product_id = request.POST.get('product_id')
        print(request.POST)
        print("........",type(product_id))
        basket.delete(product_id=product_id)
        return JsonResponse({'test':'data'})