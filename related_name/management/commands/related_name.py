from django.core.management import BaseCommand

from related_name.factories import ColorFactory, AppleWithRelatedNameFactory
from related_name.models import Color


class Command(BaseCommand):
    def handle(self, *args, **options):
        Color.objects.all().delete()

        red = ColorFactory(name='赤')
        yellow = ColorFactory(name='黄')

        AppleWithRelatedNameFactory(name='フジ', color=red)
        AppleWithRelatedNameFactory(name='秋映', color=red)
        AppleWithRelatedNameFactory(name='シナノゴールド', color=yellow)
        AppleWithRelatedNameFactory(name='もりのかがやき', color=yellow)

        print('=== normal x all ===')
        colors = Color.objects.all()
        for color in colors:
            for apple in color.my_apple_color.all():
                print(f'[{color.name}] {apple.name}')

        print('=== normal x filter ===')
        colors = Color.objects.filter(my_apple_color__name='フジ')
        for color in colors:
            for apple in color.my_apple_color.all():
                print(f'[{color.name}] {apple.name}')

        print('=== prefetch_related ===')
        colors = Color.objects.prefetch_related('my_apple_color')
        for color in colors:
            for apple in color.my_apple_color.all():
                print(f'[{color.name}] {apple.name}')

