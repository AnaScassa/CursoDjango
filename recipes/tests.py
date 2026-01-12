from django.test import TestCase
from django.urls import reverse, resolve

class RecipeURLsTest(TestCase):
    def test_the_pytest_is_ok(self):
        assert 1 == 1, 'Just a test to check if pytest is working correctly.'  

    def test_category_url_is_corret(self):
        url = reverse('recipes:category', kwargs={'category_id': 1})
        self.assertEqual(url, 'recipes/category/1/')