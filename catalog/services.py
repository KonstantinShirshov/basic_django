from catalog.models import Product


def get_category_products(category_id):
    return Product.objects.filter(category_id=category_id)
