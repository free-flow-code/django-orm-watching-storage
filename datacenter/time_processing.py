from django.utils.timezone import localtime
import datetime


def get_duration(visit):
    seconds_in_hour = 3600
    seconds_in_minute = 60
    if not visit.leaved_at:
        time_now = localtime(timezone=None)
        entered_time = localtime(value=visit.entered_at, timezone=None)
        delta = time_now - entered_time
    else:
        delta = visit.leaved_at - visit.entered_at

    hours, remainder = divmod(delta.total_seconds(), seconds_in_hour)
    mins, secs = divmod(remainder, seconds_in_minute)
    return hours, mins, secs


def format_duration(hours, mins, secs):
    time_string = f'{int(hours)},{int(mins)},{int(secs)}'
    date_formatter = '%H,%M,%S'
    date_string = datetime.datetime.strptime(time_string, date_formatter)
    return date_string.strftime('%H:%M:%S')
