
from django.db import models

class Zodiac(models.Model):

    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)

    def __str__(self):

        return self.name

class Ratio(models.Model):

    zodiac1 = models.ForeignKey(Zodiac, on_delete=models.DO_NOTHING, related_name='zodiac1')
    zodiac2 = models.ForeignKey(Zodiac, on_delete=models.DO_NOTHING, related_name='zodiac2')
    ratio = models.FloatField()

    def __str__(self):

        return f'{self.zodiac1.name} - {self.zodiac2.name} : {self.ratio}'