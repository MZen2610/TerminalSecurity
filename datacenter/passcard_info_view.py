from django.shortcuts import render

from datacenter.models import Passcard
from datacenter.models import Visit


def passcard_info_view(request, passcode):

    passcard = Passcard.objects.filter(passcode=passcode).get()
    visits = Visit.objects.filter(passcard=passcard)

    this_passcard_visits = []
    for visit in visits:
        seconds_stay = visit.get_seconds_stay()
        duration_visit = Visit.get_hours_minutes(seconds_stay)

        is_strange = Visit.compare_visit(visit=visit)

        this_passcard_visits.append({
            "entered_at": visit.entered_at,
            "duration": duration_visit,
            "is_strange": is_strange
        }, )

    context = {
        "passcard": passcard,
        "this_passcard_visits": this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
