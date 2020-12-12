from django.db import models
import django


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
    passcard = models.ForeignKey(Passcard)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return "{user} entered at {entered} {leaved}".format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved="leaved at " + str(self.leaved_at) if self.leaved_at else "not leaved"
        )

    def get_duration(self, to_now=False):
        if to_now is False:
            delta = self.leaved_at - self.entered_at
        else:
            delta = django.utils.timezone.localtime() - django.utils.timezone.localtime(self.entered_at)

        return delta.total_seconds()

    def is_visit_long(self, minutes=60):
        delta = self.leaved_at - self.entered_at
        seconds = delta.total_seconds()
        if seconds > minutes * 60:
            return True

        return False

def format_duration(duration):
    hours = int(duration // 3600)
    minutes = int((duration % 3600) // 60)
    seconds = int(duration - (hours * 3600) - (minutes * 60))
    if hours > 0:
        return '{:2}ч {:2}мин {:2}сек'.format(int(hours), int(minutes), int(seconds))
    elif minutes > 0:
        return '{:2}мин {:2}сек'.format(int(minutes), int(seconds))
    else:
        return '{:2}сек'.format(int(seconds))