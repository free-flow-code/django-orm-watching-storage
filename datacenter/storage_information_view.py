from datacenter.models import Visit
from datacenter.time_processing import get_duration
from datacenter.time_processing import format_duration
from django.shortcuts import render
from django.utils.timezone import localtime
from django.shortcuts import get_list_or_404


def storage_information_view(request):
    in_storage_users = get_list_or_404(Visit, leaved_at=None)
    minutes = 60
    non_closed_visits = []
    for user in in_storage_users:
        entered_time = localtime(value=user.entered_at, timezone=None)
        details_visit = {
            'who_entered': user.passcard,
            'entered_at': entered_time,
            'duration': format_duration(*get_duration(user)),
            'is_strange': user.is_long(minutes)
        }
        non_closed_visits.append(details_visit)

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
