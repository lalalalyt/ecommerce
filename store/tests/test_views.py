from unittest import skip

from django.contrib.auth.models import User
from django.http import HttpRequest
from django.test import Client, RequestFactory, TestCase
from django.urls import reverse

from store.models import Category, Product
from store.views import all_products, product_detail


class TestViewResponse(TestCase):
    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()
        Category.objects.create(name='django', slug='django')
        User.objects.create(username='admin')
        Product.objects.create(category_id=1, title='django beginner',
                               created_by_id=1, slug='django-beginner', price='20.00', image='django')

    def test_url_allowed_hosts(self):
        '''
        Test allowed hosts
        '''
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_product_detail_url(self):
        '''
        Test product response status
        '''
        response = self.client.get(
            reverse('store:product_detail', args=['django-beginner']))
        self.assertEqual(response.status_code, 200)

    def test_category_detail_url(self):
        '''
        Test category response status
        '''
        response = self.client.get(
            reverse('store:category_list', args=['django']))
        self.assertEqual(response.status_code, 200)

    def test_homepage_html(self):
        request = HttpRequest()
        response = all_products(request)
        html = response.content.decode()
        self.assertEqual(response.status_code, 200)
        self.assertIn('<title> Home </title>', html)
        self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))

    def test_view_function(self):
        request = self.factory.get('product/django-beginner')
        response = product_detail(request, 'django-beginner')
        html = response.content.decode()
        self.assertEqual(response.status_code, 200)
        self.assertIn('django beginner', html)
        self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))
