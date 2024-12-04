from functools import wraps
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist

from django.apps import apps


def product_exists_required(func):
    @wraps(func)
    def wrapper(self, request, *args, **kwargs):
        Product = apps.get_model('checkout', 'Product')
        products = request.data

        if len(products) == 0:
            return JsonResponse({'error': "No products provided"}, status=400)

        for product in products:
            product_name = product.get('product', '')
            product_quantity = product.get('quantity', '')

            if not product_name:
                return JsonResponse({'error': "Product name cannot be empty"}, status=400)

            if product_quantity is None or product_quantity == '':
                return JsonResponse({'error': "Product quantity cannot be empty"}, status=400)

            if not str(product_quantity).isdigit():
                return JsonResponse({'error': "Product quantity must be an integer"}, status=400)

            if int(product_quantity) < 1:
                return JsonResponse({'error': "Product quantity must be greater than 0"}, status=400)

            try:
                product_instance = Product.objects.get(name=product_name)
            except ObjectDoesNotExist:
                return JsonResponse({'error': f"Product '{product_name}' not found"}, status=404)

            try:
                product_quantity = int(product_quantity)
            except ValueError:
                return JsonResponse({'error': "Product quantity must be an integer"}, status=400)

            # Check if the stock is sufficient
            if product_quantity > product_instance.quantity:
                return JsonResponse({'error': f"Insufficient stock for product '{product_name}'"}, status=400)

        return func(self, request, *args, **kwargs)

    return wrapper
