import pytest

from rest_framework import status
from rest_framework.test import APIClient

from django.urls import reverse

from checkout.models import Product


pytestmark = pytest.mark.django_db


class TestProductAPI:

    @pytest.fixture(autouse=True)
    def setup_method(self):
        self.api_client = APIClient()
        self.product1 = Product.objects.create(name="Test Product 1", price=10.00, quantity=100)
        self.product2 = Product.objects.create(name="Test Product 2", price=15.00, quantity=200)

    @pytest.fixture
    def create_product(self):
        def _create_product(name, price, quantity):
            return Product.objects.create(name=name, price=price, quantity=quantity)
        return _create_product


    def test_get_products(self):
        url = reverse("checkout:products")
        response = self.api_client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 2

    def test_post_order(self):
        data = [
            {"product": "Test Product 1", "quantity": 1},
            {"product": "Test Product 2", "quantity": 2},
        ]

        url = reverse("checkout:order")
        response = self.api_client.post(url, data, format="json")

        assert response.status_code == status.HTTP_200_OK
        assert 'total' in response.content.decode('utf-8')
        assert str(40.00) in response.content.decode('utf-8')


    def test_post_order_empty_data(self):
        data = []
        url = reverse("checkout:order")
        response = self.api_client.post(url, data, format="json")

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert 'No products provided' in response.content.decode('utf-8')

    def test_post_order_no_data(self):
        url = reverse("checkout:order")
        response = self.api_client.post(url, format="json")

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert 'No products provided' in response.content.decode('utf-8')

    def test_post_order_no_product_name(self):
        data = [
            {"product": "", "quantity": 1},
        ]
        expected_error = "Product name cannot be empty"
        url = reverse("checkout:order")

        response = self.api_client.post(url, data, format="json")
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert 'error' in response.content.decode('utf-8')
        assert expected_error in response.json()['error']

    def test_post_order_no_product_quantity(self):
        data = [
            {"product": "Test Product 1", "quantity": ""},
        ]
        expected_error = "Product quantity cannot be empty"
        url = reverse("checkout:order")
        response = self.api_client.post(url, data, format="json")
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert 'error' in response.content.decode('utf-8')
        assert expected_error in response.json()['error']


    def test_post_product_not_found(self):
        data = [
            {"product": "Test Product 3", "quantity": 1},
        ]
        expected_error = f"Product '{data[0]['product']}' not found"

        url = reverse("checkout:order")
        response = self.api_client.post(url, data, format="json")

        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert 'error' in response.content.decode('utf-8')
        assert expected_error in response.json()['error']

    def test_post_product_quantity_not_enough(self):
        data = [
            {"product": "Test Product 1", "quantity": 101},
        ]
        expected_error = f"Insufficient stock for product '{data[0]['product']}'"

        url = reverse("checkout:order")
        response = self.api_client.post(url, data, format="json")

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert 'error' in response.content.decode('utf-8')
        assert expected_error in response.json()['error']

    def test_post_product_quantity_not_integer(self):
        data = [
            {"product": "Test Product 1", "quantity": "a"},
        ]
        expected_error = f"Product quantity must be an integer"

        url = reverse("checkout:order")
        response = self.api_client.post(url, data, format="json")

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert 'error' in response.content.decode('utf-8')
        assert expected_error in response.json()['error']
