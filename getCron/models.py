from django.db import models


# Create your models here.
class lotto_data(models.Model):
    round = models.IntegerField(default=0)
    prize1 = models.IntegerField(default=0)
    prize2 = models.IntegerField(default=0)
    prize3 = models.IntegerField(default=0)
    prize4 = models.IntegerField(default=0)
    prize5 = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    drawing_day = models.DateTimeField()

