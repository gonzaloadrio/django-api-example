from django.contrib.postgres.fields import JSONField
from django.db import models


# Create your models here.

class Building(models.Model):
    s_id = models.IntegerField(unique=True, verbose_name='Situm ID')
    name = models.TextField(verbose_name='Name')
    description = models.TextField(verbose_name='Description')
    location = JSONField(verbose_name='Location (lat, lng)', default=list)
    position = JSONField(verbose_name='Position (x, y)', default=list)

    def __str__(self):
        return 'ID: {0} - Situm ID: {1} - Name: {2}'.format(self.id, self.s_id, self.name)


class Floor(models.Model):
    s_id = models.IntegerField(unique=True, verbose_name='Situm ID')
    name = models.TextField(verbose_name='Name')
    description = models.TextField(verbose_name='Description')
    building = models.ForeignKey(Building, on_delete=models.CASCADE, db_column='building_s_id', to_field='s_id',
                                 related_name='floors', verbose_name='Building')
    image = models.ImageField(null=True, default=None, verbose_name='Image')

    def __str__(self):
        return 'ID: {0} - Situm ID: {1} - Name: {2}'.format(self.id, self.s_id, self.name)
