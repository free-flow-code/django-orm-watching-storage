from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from datacenter.storage_information_view import get_duration
from datacenter.storage_information_view import format_duration


def get_passcard_visits(passcard):
    all_visits = Visit.objects.filter(passcard=passcard)
    minutes = 60
    this_passcard_visits = []
    for visit in all_visits:
        details_visit = {}
        details_visit['entered_at'] = visit.entered_at
        details_visit['duration'] = format_duration(*get_duration(visit))
        details_visit['is_strange'] = Visit.is_long(visit, minutes)
        this_passcard_visits.append(details_visit)
    return this_passcard_visits


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)
    this_passcard_visits = get_passcard_visits(passcard)
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
