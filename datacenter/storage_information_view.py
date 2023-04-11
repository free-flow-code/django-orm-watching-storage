from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime


def get_duration(entered_at):
    time_now = localtime(timezone=None)
    delta = time_now - entered_at
    hours, remainder = divmod(delta.total_seconds(), 3600)
    minutes, seconds = divmod(remainder, 60)
    return hours, minutes, seconds


def format_duration(hours, minutes, seconds):
    return f'{int(hours)}:{int(minutes)}:{int(seconds)}'


def storage_information_view(request):
    in_storage_users = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []
    for user in in_storage_users:
        timezone_entered_time = localtime(value=user.entered_at, timezone=None)
        hours, minutes, seconds = get_duration(timezone_entered_time)
        details_visit['who_entered'] = user.passcard
        details_visit['entered_at'] = timezone_entered_time
        details_visit['duration'] = format_duration(hours, minutes, seconds)
        non_closed_visits.append(details_visit)

    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
