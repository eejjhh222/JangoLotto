# Create your views here.
from django.shortcuts import get_object_or_404, render
from django import forms
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .module.crolling_lotto import *
from getCron.models import lotto_data
from django.urls import reverse


class prizeNumberForm(forms.Form):
    round = forms.IntegerField(widget=forms.HiddenInput())
    prize1 = forms.IntegerField(widget=forms.HiddenInput())
    prize2 = forms.IntegerField(widget=forms.HiddenInput())
    prize3 = forms.IntegerField(widget=forms.HiddenInput())
    prize4 = forms.IntegerField(widget=forms.HiddenInput())
    prize5 = forms.IntegerField(widget=forms.HiddenInput())
    prize6 = forms.IntegerField(widget=forms.HiddenInput())
    bonus = forms.IntegerField(widget=forms.HiddenInput())


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

    def set_round(self, round_id, prize1, prize2, prize3, prize4, prize5, prize6, bonus):
        self.round = round_id
        self.prize1 = prize1
        self.prize2 = prize2
        self.prize3 = prize3
        self.prize4 = prize4
        self.prize5 = prize5
        self.prize6 = prize6
        self.bonus = bonus


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def lotto_number(request):
    return render(request, 'lottoNumber_form.html')


# def get_number(request, round_id):
def get_number(request):
    round_id = int(request.GET['round_id'])
#     lotto_data = get_object_or_404(lotto_data, pk=round)
#     round_id = int(round)
    round_id = int(round_id)
    res = looto_process(round_id)

    if res == "error":
        return HttpResponse('error')
    else:
        prize_list = res[round_id]

        '''print('round : %d' % round_id)
        print('prize1 : ' + prize_list[0])
        print('prize2 : ' + prize_list[1])
        print('prize3 : ' + prize_list[2])
        print('prize4 : ' + prize_list[3])
        print('prize5 : ' + prize_list[4])
        print('prize6 : ' + prize_list[5])
        print('bonus : ' + prize_list[6][0])
        '''

        bonus = prize_list[6][0]
        del(prize_list[6])

        data = {
            'round': round_id
            , 'prize1': prize_list[0]
            , 'prize2': prize_list[1]
            , 'prize3': prize_list[2]
            , 'prize4': prize_list[3]
            , 'prize5': prize_list[4]
            , 'prize6': prize_list[5]
            , 'bonus': bonus
        }
        form = prizeNumberForm(data)

        context = {
            'round': round_id
            , 'form': form
            , 'prize_list': prize_list
            , 'bonus': bonus
        }

        return render(request, 'lottoNumber_view.html', context)


def save_number(request):
    round_id = int(request.POST['round'])

    if lotto_data.objects.filter(round=round_id).exists():
        pass
    else:
        prize1 = int(request.POST['prize1'])
        prize2 = int(request.POST['prize2'])
        prize3 = int(request.POST['prize3'])
        prize4 = int(request.POST['prize4'])
        prize5 = int(request.POST['prize5'])
        prize6 = int(request.POST['prize6'])
        bonus = int(request.POST['bonus'])
        # lottodata = lottoObj(round_id, prize1, prize2, prize3, prize4, prize5, prize6, bonus)
        # print(lottodata.round)
        ld = lotto_data(round=round_id
                        , prize1=prize1
                        , prize2=prize2
                        , prize3=prize3
                        , prize4=prize4
                        , prize5=prize5
                        , prize6=prize6
                        , bonus=bonus
                        )
        ld.save()

    return HttpResponseRedirect(reverse('getCron:list_number'))

    # selected_choice = lotto_data.choice_set.get(sround=round_id)
    return HttpResponse("save round")
'''
    try:
        selected_choice = lottodata.choice_set.get(sround=round_id)
        print(selected_choice)
    except (KeyError, lottodata.DoesNotExist):
        selected_choice.round = round_id
        selected_choice.prize1 = int(request.POST['prize1'])
        selected_choice.prize2 = int(request.POST['prize2'])
        selected_choice.prize3 = int(request.POST['prize3'])
        selected_choice.prize4 = int(request.POST['prize4'])
        selected_choice.prize5 = int(request.POST['prize5'])
        selected_choice.prize6 = int(request.POST['prize6'])
        selected_choice.bonus = int(request.POST['bonus'])
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponse("save round")
        # return HttpResponseRedirect(reverse('getCron:list_number'))
    else:
        # Redisplay the question voting form.
        return HttpResponse("exist round")
'''


def list_number(request):
    try:
        lotto_list_all = lotto_data.objects.all()
    except (KeyError, lotto_data.DoesNotExist):
        # Redisplay the question voting form.
        return HttpResponse("empty list")
    else:

        lotto_list = []
        for lotto in lotto_list_all:
            lotto_list.append({
                'round': lotto.get_round()
                ,'prize1': lotto.get_prize1()
                ,'prize2': lotto.get_prize2()
                ,'prize3': lotto.get_prize3()
                ,'prize4': lotto.get_prize4()
                ,'prize5': lotto.get_prize5()
                ,'prize6': lotto.get_prize6()
                ,'bonus': lotto.get_bonus()
            })

        context = {
            'lotto_list': lotto_list
        }
        return render(request, 'lottoNumber_list.html', context)
