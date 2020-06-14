from django.core.management import BaseCommand

from related_name.factories import ColorFactory, AppleNoReverseWithPlusFactory
from related_name.models import Color


class Command(BaseCommand):
    def handle(self, *args, **options):
        Color.objects.all().delete()

        red = ColorFactory(name='赤')
        yellow = ColorFactory(name='黄')

        AppleNoReverseWithPlusFactory(name='フジ', color=red)
        AppleNoReverseWithPlusFactory(name='秋映', color=red)
        AppleNoReverseWithPlusFactory(name='シナノゴールド', color=yellow)
        AppleNoReverseWithPlusFactory(name='もりのかがやき', color=yellow)

        colors = Color.objects.all()
        for color in colors:
            print(dir(color))
            # => [..., 'apple_set',  ..., 'my_apple_color', ..., 'related_name_appledefaultrelatedname_list', ...]

            # 以下の行でエラー
            # AttributeError: 'Color' object has no attribute 'applenoreversewithplus'
            # for apple in color.applenoreversewithplus.all():
            #     print(f'[{color.name}] {apple.name}')

