from getCron.models import lotto_data


class lottoObj:
    def __init__(self, round_id, prize1, prize2, prize3, prize4, prize5, prize6, bonus):
        self.round = round_id
        self.prize1 = prize1
        self.prize2 = prize2
        self.prize3 = prize3
        self.prize4 = prize4
        self.prize5 = prize5
        self.prize6 = prize6
        self.bonus = bonus
