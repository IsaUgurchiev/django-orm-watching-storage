from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render

from .utils import format_duration

def passcard_info_view(request, passcode):
    this_passcard_visits = []
    passcard = Passcard.objects.get(passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)
    for visit in visits:
        duration = format_duration(visit.get_duration())
        this_passcard_visits.append(
            {
                "entered_at": visit.entered_at,
                "duration": duration,
                "is_strange": visit.is_visit_long()
            }
        )

    context = {
        "passcard": passcard,
        "this_passcard_visits": this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
