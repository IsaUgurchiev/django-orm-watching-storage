from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.http import Http404

from .utils import format_duration

def passcard_info_view(request, passcode):
    try:
        passcard = Passcard.objects.get(passcode=passcode)
    except Passcard.DoesNotExist:
        raise Http404('Passcard not found')

    this_passcard_visits = []
    serialized_visits = Visit.objects.filter(passcard=passcard)
    for visit in serialized_visits:
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


