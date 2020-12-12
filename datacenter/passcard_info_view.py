from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from .models import format_duration

def passcard_info_view(request, passcode):
    this_passcard_visits = []
    passcard = Passcard.objects.filter(passcode=passcode)[0]
    visits = Visit.objects.filter(passcard=passcard)
    for visit in visits:
        if visit.leaved_at is None:
            continue

        duration = format_duration(Visit.get_duration(visit))
        this_passcard_visits.append(
            {
                "entered_at": visit.entered_at,
                "duration": duration,
                "is_strange": Visit.is_visit_long(visit)
            }
        )

    context = {
        "passcard": passcard,
        "this_passcard_visits": this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
