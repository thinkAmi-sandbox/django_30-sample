import factory

from related_name.models import Color, Apple, AppleDefaultRelatedName, AppleWith2Color, \
    AppleWith3Color, Fruit, Potato, AppleWithRelatedName, AppleNoReverseWithPlus, \
    AppleNoReverseWithEndPlus


class ColorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Color


class AppleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Apple


class AppleWithRelatedNameFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = AppleWithRelatedName


class AppleDefaultRelatedNameFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = AppleDefaultRelatedName


class AppleNoReverseWithPlusFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = AppleNoReverseWithPlus


class AppleNoReverseWithEndPlusFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = AppleNoReverseWithEndPlus


class AppleWith2ColorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = AppleWith2Color


class FruitFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Fruit


class PotatoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Potato


class AppleWith3ColorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = AppleWith3Color
