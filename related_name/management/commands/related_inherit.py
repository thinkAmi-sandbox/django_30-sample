from django.core.management import BaseCommand

from related_name.factories import ColorFactory, FruitFactory, PotatoFactory
from related_name.models import Color


class Command(BaseCommand):
    def handle(self, *args, **options):
        Color.objects.all().delete()

        pink = ColorFactory(name='ピンク')
        purple = ColorFactory(name='紫')

        FruitFactory(name='フジ', bud_color=pink)
        FruitFactory(name='秋映', bud_color=pink)
        PotatoFactory(name='男爵', bud_color=purple)
        PotatoFactory(name='メークイン', bud_color=purple)

        print('=== fruit ===')
        fruits_color = Color.objects.prefetch_related('fruit_bud_colors')
        for color in fruits_color:
            for fruit in color.fruit_bud_colors.all():
                print(f'[{color.name}] {fruit.name}')

        print('=== potato ===')
        potato_colors = Color.objects.prefetch_related('potato_bud_colors')
        for color in potato_colors:
            for potato in color.potato_bud_colors.all():
                print(f'[{color.name}] {potato.name}')
