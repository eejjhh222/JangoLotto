from django.db import models
from .module.crolling_lotto import *


# Create your models here.
class lotto_data(models.Model):
    round = models.IntegerField(default=0)
    prize1 = models.IntegerField(default=0)
    prize2 = models.IntegerField(default=0)
    prize3 = models.IntegerField(default=0)
    prize4 = models.IntegerField(default=0)
    prize5 = models.IntegerField(default=0)
    prize6 = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    drawing_day = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return "str : %d %d %d %d %d %d %d %d" \
               %(self.round, self.prize1, self.prize2, self.prize3, self.prize4, self.prize5, self.prize6, self.bonus)

    def get_lotto_num(self, round_id):
        res = looto_process(int(round_id))
        print(res)

    def get_round(self):
        return self.round

    def get_prize1(self):
        return self.prize1

    def get_prize2(self):
        return self.prize2

    def get_prize3(self):
        return self.prize3

    def get_prize4(self):
        return self.prize4

    def get_prize5(self):
        return self.prize5

    def get_prize6(self):
        return self.prize6

    def get_bonus(self):
        return self.bonus

    def get_drawing_day(self):
        return self.drawing_day
