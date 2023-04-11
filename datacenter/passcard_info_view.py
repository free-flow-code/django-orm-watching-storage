from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def get_passcard_visits(passcard):
    all_visits = Visit.objects.filter(passcard=passcard)
    return all_visits[::-1]


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.all()[0]
    # Программируем здесь

    this_passcard_visits = get_passcard_visits(passcard)
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
