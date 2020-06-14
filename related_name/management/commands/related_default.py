from django.core.management import BaseCommand

from related_name.factories import ColorFactory, AppleFactory
from related_name.models import Color


class Command(BaseCommand):
    def handle(self, *args, **options):
        Color.objects.all().delete()

        red = ColorFactory(name='赤')
        yellow = ColorFactory(name='黄')

        AppleFactory(name='フジ', color=red)
        AppleFactory(name='秋映', color=red)
        AppleFactory(name='シナノゴールド', color=yellow)
        AppleFactory(name='もりのかがやき', color=yellow)

        colors = Color.objects.all()
        for color in colors:
            for apple in color.apple_set.all():
                print(f'[{color.name}] {apple.name}')

        print('=== normal x filter ===')
        colors = Color.objects.filter(apple__name='フジ')
        for color in colors:
            for apple in color.apple_set.all():
                print(f'[{color.name}] {apple.name}')

        print('=== prefetch_related ===')
        colors = Color.objects.prefetch_related('apple_set')
        for color in colors:
            for apple in color.apple_set.all():
                print(f'[{color.name}] {apple.name}')

