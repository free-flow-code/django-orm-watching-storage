from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime
from django.shortcuts import get_list_or_404
import datetime


def get_duration(visit):
    if not visit.leaved_at:
        time_now = localtime(timezone=None)
        entered_time = localtime(value=visit.entered_at, timezone=None)
        delta = time_now - entered_time
    else:
        delta = visit.leaved_at - visit.entered_at

    hours, remainder = divmod(delta.total_seconds(), 3600)
    mins, secs = divmod(remainder, 60)
    return hours, mins, secs


def format_duration(hours, mins, secs):
    time_string = f'{int(hours)}{int(mins)}{int(secs)}'
    date_formatter = '%H%M%S'
    date_string = datetime.datetime.strptime(time_string, date_formatter)
    return date_string.strftime('%H:%M:%S')


def storage_information_view(request):
    in_storage_users = get_list_or_404(Visit, leaved_at=None)
    minutes = 60
    non_closed_visits = []
    for user in in_storage_users:
        entered_time = localtime(value=user.entered_at, timezone=None)
        details_visit = {}
        details_visit['who_entered'] = user.passcard
        details_visit['entered_at'] = entered_time
        details_visit['duration'] = format_duration(*get_duration(user))
        details_visit['is_strange'] = Visit.is_long(user, minutes)
        non_closed_visits.append(details_visit)
        print(details_visit)

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
