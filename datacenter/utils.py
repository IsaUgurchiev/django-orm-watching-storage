import datetime

def get_total_minutes(duration: datetime.timedelta):
    seconds = duration.total_seconds()
    return seconds // 60


def format_duration(duration: datetime.timedelta):
    hours = int(duration.total_seconds() // 3600)
    minutes = int((duration.total_seconds() % 3600) // 60)
    seconds = int(duration.total_seconds() - (hours * 3600) - (minutes * 60))
    if hours > 0:
        return '{:2}ч {:2}мин {:2}сек'.format(int(hours), int(minutes), int(seconds))
    elif minutes > 0:
        return '{:2}мин {:2}сек'.format(int(minutes), int(seconds))
    else:
        return '{:2}сек'.format(int(seconds))