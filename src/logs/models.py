from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.db import models
from django.dispatch import receiver

from teamboard.models import Team


class LogEntry(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    ip = models.GenericIPAddressField(null=True)


class AuditEntry(LogEntry):
    action = models.CharField(max_length=64)
    username = models.CharField(max_length=256, null=True)

    def __str__(self):
        return '{0} - {1} - {2}'.format(self.action, self.username, self.ip)


@receiver(user_logged_in)
def user_logged_in_callback(sender, request, user, **kwargs):
    ip = request.META.get('REMOTE_ADDR')
    AuditEntry.objects.create(action='user_logged_in', ip=ip, username=user.username)


@receiver(user_logged_out)
def user_logged_out_callback(sender, request, user, **kwargs):
    ip = request.META.get('REMOTE_ADDR')
    AuditEntry.objects.create(action='user_logged_out', ip=ip, username=user.username)


@receiver(user_login_failed)
def user_login_failed_callback(sender, credentials, **kwargs):
    AuditEntry.objects.create(action='user_login_failed', username=credentials.get('username', None))


class FlagAttemptEntry(LogEntry):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team')
    flag = models.CharField(max_length=100, null=False, blank=False)
    valid = models.BooleanField(default=False, null=False, blank=False)
    sharing = models.BooleanField(default=False, null=False, blank=False)  # if flag belongs to another team
    team_sharing = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, blank=True,
                                     related_name='another_team')  # reference to another team

    def __str__(self):
        return f'{self.team}: {self.flag}'


class AdminPanelEntry(LogEntry):
    valid = models.BooleanField(default=False)
