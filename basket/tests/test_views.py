from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from store.models import Category, Product


class TestBasketView(TestCase):
    def setUp(self):
        Category.objects.create(name='django', slug='django')
        User.objects.create(username='admin')
        Product.objects.create(category_id=1, title='django beginner',
                               created_by_id=1, slug='django-beginner', price='20.00', image='django')
        Product.objects.create(category_id=1, title='django 2',
                               created_by_id=1, slug='django-2', price='10.00', image='django')
        Product.objects.create(category_id=1, title='django 3',
                               created_by_id=1, slug='django-3', price='30.00', image='django')
        self.client.post(
            reverse('basket:basket_add'), {"product_id": 1, "product_qty": 1, "action": "add"}, xhr=True)
        self.client.post(
            reverse('basket:basket_add'), {"product_id": 2, "product_qty": 2, "action": "add"}, xhr=True)
    
    def test_basket_url(self):
        """
        Test homepage response status
        """
        response = self.client.get(reverse('basket:basket_summary'))
        self.assertEqual(response.status_code,200)

    def test_basket_add(self):
        """
        Test adding items to the basket
        """
        response = self.client.post(
            reverse('basket:basket_add'), {"product_id": 3, "product_qty": 1, "action": "add"}, xhr=True)
        self.assertEqual(response.json(),{"qty":4})
        response = self.client.post(
            reverse('basket:basket_add'), {"product_id": 2, "product_qty": 1, "action": "add"}, xhr=True)
        self.assertEqual(response.json(), {'qty': 3})

    def test_basket_delete(self):
        """
        Test deleting items from the basket
        """
        response = self.client.post(
            reverse('basket:basket_delete'), {"product_id": 2, "action": "delete"}, xhr=True)
        self.assertEqual(response.json(), {'totalQty': 1, 'subtotal': '20.00'})

    def test_basket_update(self):
        """
        Test updating items from the basket
        """
        response = self.client.post(
            reverse('basket:basket_update'), {"product_id": 2, "product_qty": 1, "action": "update"}, xhr=True)
        self.assertEqual(response.json(), {'totalQty': 2, 'subtotal': '30.00'})