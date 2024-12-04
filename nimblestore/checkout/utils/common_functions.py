from django.apps import apps


def calculate_total(products):
    """
    Calculate total
    """
    Product = apps.get_model('checkout', 'Product')
    total = 0
    for product in products['products']:
        _product = Product.objects.get(name=product['product'])
        total += _product.price * int(product['quantity'])
    return total
