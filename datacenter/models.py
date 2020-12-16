from django.db import models
from django.utils.timezone import localtime, make_aware
import datetime


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, models.CASCADE, )
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return "{user} entered at {entered} {leaved}".format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved="leaved at " + str(self.leaved_at)
            if self.leaved_at else "not leaved")

    def get_duration(visit):

        delta = make_aware(
            datetime.datetime.now()) - localtime(value=visit.entered_at)
        seconds = delta.total_seconds()

        return seconds

    def get_seconds_stay(visit):
        if visit.leaved_at is None:
            delta = make_aware(
                datetime.datetime.now()) - localtime(value=visit.entered_at)
        else:
            delta = localtime(value=visit.leaved_at) - localtime(
                value=visit.entered_at)
        seconds = delta.total_seconds()

        return seconds

    @classmethod
    def compare_visit(self, visit, minutes=60):
        seconds = self.get_seconds_stay(visit)
        minut = int(seconds // 60)
        return minut > minutes

    def get_hours_minutes(duration):
        hours = int(duration // 3600)
        minutes = int((duration % 3600) // 60)
        return f"{hours}ч {minutes}мин"
