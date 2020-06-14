from django.db import models
from django.utils import timezone


class Color(models.Model):
    name = models.CharField('色', max_length=30, unique=True)


class Apple(models.Model):
    name = models.CharField('品種名', max_length=30, unique=True)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)


class AppleWithRelatedName(models.Model):
    name = models.CharField('品種名', max_length=30, unique=True)
    color = models.ForeignKey(Color, on_delete=models.CASCADE,
                              related_name='my_apple_color')


class AppleDefaultRelatedName(models.Model):
    name = models.CharField('品種名', max_length=30, unique=True)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)

    class Meta:
        default_related_name = '%(app_label)s_%(class)s_list'


class AppleNoReverseWithPlus(models.Model):
    name = models.CharField('品種名', max_length=30, unique=True)
    color = models.ForeignKey(Color, on_delete=models.CASCADE,
                              related_name='+')


class AppleNoReverseWithEndPlus(models.Model):
    name = models.CharField('品種名', max_length=30, unique=True)
    color = models.ForeignKey(Color, on_delete=models.CASCADE,
                              related_name='end_plus+')


class AppleWith2Color(models.Model):
    name = models.CharField('品種名', max_length=30, unique=True)

    # Bad
    # fruit_color = models.ForeignKey(Color, on_delete=models.CASCADE)
    # bud_color = models.ForeignKey(Color, on_delete=models.CASCADE)
    # => migration error
    # related_name.AppleWith2Color.bud_color: (fields.E304) Reverse accessor for
    #   'AppleWith2Color.bud_color' clashes with reverse accessor for 'AppleWith2Color.fruit_color'.
    # HINT: Add or change a related_name argument to the definition for
    #   'AppleWith2Color.bud_color' or 'AppleWith2Color.fruit_color'.

    # Good
    fruit_color = models.ForeignKey(Color, on_delete=models.CASCADE,
                                    related_name='fruits')
    bud_color = models.ForeignKey(Color, on_delete=models.CASCADE,
                                  related_name='buds')


class ModelBase(models.Model):
    # Bad
    # bud_color = models.ForeignKey(Color, on_delete=models.CASCADE,
    #                               related_name='bud_colors')

    # Good
    bud_color = models.ForeignKey(Color, on_delete=models.CASCADE,
                                  related_name='%(class)s_bud_colors')

    class Meta:
        abstract = True


class Fruit(ModelBase):
    name = models.CharField('品種名', max_length=30, unique=True)


class Potato(ModelBase):
    name = models.CharField('品種名', max_length=30, unique=True)


class AppleWith3Color(models.Model):
    name = models.CharField('品種名', max_length=30, unique=True)

    bud_color = models.ForeignKey(Color, on_delete=models.CASCADE)
    leaf_color = models.ForeignKey(Color, on_delete=models.CASCADE,
                                   related_name='leaf_colors')
    fruit_color = models.ForeignKey(Color, on_delete=models.CASCADE,
                                    related_name='fruit_colors',
                                    related_query_name='my_fruit_colors')

    class Meta:
        default_related_name = 'default_colors'
