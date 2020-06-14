from django.core.management import BaseCommand

from related_name.factories import ColorFactory, AppleDefaultRelatedNameFactory
from related_name.models import Color


class Command(BaseCommand):
    def handle(self, *args, **options):
        Color.objects.all().delete()

        red = ColorFactory(name='赤')
        yellow = ColorFactory(name='黄')

        AppleDefaultRelatedNameFactory(name='フジ', color=red)
        AppleDefaultRelatedNameFactory(name='秋映', color=red)
        AppleDefaultRelatedNameFactory(name='シナノゴールド', color=yellow)
        AppleDefaultRelatedNameFactory(name='もりのかがやき', color=yellow)

        colors = Color.objects.all()
        for color in colors:
            for apple in color.related_name_appledefaultrelatedname_list.all():
                print(f'[{color.name}] {apple.name}')

