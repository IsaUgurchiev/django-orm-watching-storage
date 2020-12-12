from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from .models import format_duration

def storage_information_view(request):
    non_closed_visits = []
    visits = Visit.objects.filter(leaved_at=None)
    for visit in visits:
        duration = format_duration(Visit.get_duration(visit, to_now=True))
        non_closed_visits.append(
            {
                "who_entered": visit.passcard.owner_name,
                "entered_at": visit.entered_at,
                "duration": duration
            }
        )

    context = {
        "non_closed_visits": non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)