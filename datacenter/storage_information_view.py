from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render

from .utils import format_duration

def storage_information_view(request):
    non_closed_visits = []
    serialized_visits = Visit.objects.filter(leaved_at=None)
    for visit in serialized_visits:
        duration = format_duration(visit.get_duration())
        non_closed_visits.append(
            {
                "who_entered": visit.passcard.owner_name,
                "entered_at": visit.entered_at,
                "duration": duration
            }
        )

    context = {
        "non_closed_visits": non_closed_visits,
    }
    return render(request, 'storage_information.html', context)