from django.core.management import BaseCommand

from related_name.factories import ColorFactory, AppleWith3ColorFactory
from related_name.models import Color


class Command(BaseCommand):
    def handle(self, *args, **options):
        Color.objects.all().delete()

        red = ColorFactory(name='赤')
        yellow = ColorFactory(name='黄')
        pink = ColorFactory(name='ピンク')
        green = ColorFactory(name='緑')
        gold = ColorFactory(name='金')

        AppleWith3ColorFactory(name='フジ', bud_color=pink, leaf_color=green, fruit_color=red)
        AppleWith3ColorFactory(name='秋映', bud_color=pink, leaf_color=green, fruit_color=red)
        AppleWith3ColorFactory(name='シナノゴールド', bud_color=pink, leaf_color=green, fruit_color=yellow)
        AppleWith3ColorFactory(name='もりのかがやき', bud_color=pink, leaf_color=green, fruit_color=yellow)
        AppleWith3ColorFactory(name='ピンクレディ', bud_color=pink, leaf_color=green, fruit_color=pink)
        AppleWith3ColorFactory(name='金のりんご', bud_color=gold, leaf_color=gold, fruit_color=gold)

        # default_related_name
        print('=== default_related_name ===')
        default_colors = Color.objects.filter(default_colors__name='フジ')
        for color in default_colors:
            for apple in color.default_colors.all():
                print(f'[{color.name}] {apple.name}')

        # related_name
        print('=== related_name ===')
        leaf_colors = Color.objects.filter(leaf_colors__name='フジ')
        for color in leaf_colors:
            for apple in color.leaf_colors.all():
                print(f'[{color.name}] {apple.name}')

        # related_query_name
        print('=== related_query_name ===')
        # Bad
        # fruit_colors = Color.objects.filter(fruit_colors__name='フジ')
        # => django.core.exceptions.FieldError: Cannot resolve keyword 'leaf_colors' into field.
        #    Choices are: apple, bud_colors, default_colors, fruits, id, my_buds, my_color, my_leaf_colors, name

        # Good
        # filter
        my_fruit_colors = Color.objects.filter(my_fruit_colors__name='フジ')
        for color in my_fruit_colors:
            for apple in color.fruit_colors.all():
                print(f'[{color.name}] {apple.name}')

        # order_by
        print('=== order_by asc ===')
        order_by_name = Color.objects.order_by('my_fruit_colors__name')
        for color in order_by_name:
            print(color.name)

        print('=== order_by desc ===')
        order_by_name = Color.objects.order_by('-my_fruit_colors__name')
        for color in order_by_name:
            print(color.name)
