from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Product, Category


class Command(BaseCommand):
    help = "Add products to the database"

    def handle(self, *args, **kwargs):
        # Удаляем существующие записи
        Product.objects.all().delete()
        Category.objects.all().delete()

        call_command("loaddata", "catalog_fixture.json")
        self.stdout.write(self.style.SUCCESS("Successfully loaded data from fixture"))

        category, _ = Category.objects.get_or_create(name="Спорт")

        products = [
            {
                "name": "Футбольный мяч",
                "description": "Мяч для игры в футбол",
                "price": 7000,
                "category": category,
            },
            {
                "name": "Бутсы футбольные Nike",
                "description": "Легкие, обеспечивают идеальное сцепление с газоном ",
                "price": 10000,
                "category": category,
            },
            {
                "name": "Коньки хоккейные CCM",
                "description": "Коньки для игры в хоккей, имеют дополнительную защиту голеностопа",
                "price": 15000,
                "category": category,
            },
        ]

        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f"Successfully added student: {product.name}")
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f"Student already exists: {product.name}")
                )
