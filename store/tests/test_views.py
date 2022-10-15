from importlib import import_module
from unittest import skip

from django.conf import settings
from django.contrib.auth.models import User
from django.http import HttpRequest
from django.test import Client, TestCase
from django.urls import reverse

from store.models import Category, Product
from store.views import product_all


@skip("demonstrating skipping")
class TestSkip(TestCase):
    def test_skip_exmaple(self):
        pass


class TestViewResponse(TestCase):
    def setUp(self):
        self.client = Client()
        Category.objects.create(name='django', slug='django')
        User.objects.create(username='admin')
        Product.objects.create(category_id=1, title='django beginner',
                               created_by_id=1, slug='django-beginner', price='20.00', image='django')

    def test_url_allowed_hosts(self):
        '''
        Test allowed hosts
        '''
        response = self.client.get('/', HTTP_HOST='noaddress.com')
        self.assertEqual(response.status_code, 400)
        response = self.client.get('/', HTTP_HOST='yourdomain.com')
        self.assertEqual(response.status_code, 200)

    def test_homepage_url(self):
        '''
        Test homepage response status
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

    def test_category_list_url(self):
        '''
        Test category response status
        '''
        response = self.client.get(
            reverse('store:category_list', args=['django']))
        self.assertEqual(response.status_code, 200)

    def test_homepage_html(self):
        '''
        Example: code validation, search HTML for text
        '''
        request = HttpRequest()
        engine = import_module(settings.SESSION_ENGINE)
        request.session = engine.SessionStore()
        response = product_all(request)
        html = response.content.decode()
        self.assertEqual(response.status_code, 200)
        self.assertIn('<title> Secret Garden </title>', html)
        self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))
