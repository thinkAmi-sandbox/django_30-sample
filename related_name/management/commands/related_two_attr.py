from django.core.management import BaseCommand

from related_name.factories import ColorFactory, AppleWith2ColorFactory
from related_name.models import Color


class Command(BaseCommand):
    def handle(self, *args, **options):
        Color.objects.all().delete()

        red = ColorFactory(name='赤')
        yellow = ColorFactory(name='黄')
        pink = ColorFactory(name='ピンク')

        AppleWith2ColorFactory(name='フジ', fruit_color=red, bud_color=pink)
        AppleWith2ColorFactory(name='秋映', fruit_color=red, bud_color=pink)
        AppleWith2ColorFactory(name='シナノゴールド', fruit_color=yellow, bud_color=pink)
        AppleWith2ColorFactory(name='もりのかがやき', fruit_color=yellow, bud_color=pink)
        AppleWith2ColorFactory(name='ピンクレディ', fruit_color=pink, bud_color=pink)

        colors = Color.objects.prefetch_related('fruits', 'buds')
        for color in colors:
            print('--- start fruit ---')
            for fruit in color.fruits.all():
                print(f'[{color.name}] {fruit.name}')
            else:
                print('--- end fruit ---')

            print('--- start bud ---')
            for bud in color.buds.all():
                print(f'[{color.name}] {bud.name}')

            else:
                print('--- end bud ---')
