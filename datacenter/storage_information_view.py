from django.shortcuts import render
from django.utils.timezone import localtime
from datacenter.models import Visit


def storage_information_view(request):
    non_closed_visits = []
    visits = Visit.objects.filter(leaved_at=None)
    for visit in visits:
        duration_seconds = visit.get_duration()
        duration = Visit.get_hours_minutes(duration_seconds)
        non_closed_visits.append(
            {
                "who_entered": visit.passcard.owner_name,
                "entered_at": localtime(value=visit.entered_at),
                "duration": duration,
            }
        )

    context = {
        "non_closed_visits": non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
