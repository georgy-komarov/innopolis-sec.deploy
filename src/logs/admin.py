from django.contrib import admin

from logs.models import AuditEntry, AdminPanelEntry, FlagAttemptEntry


@admin.register(AuditEntry)
class AuditEntryAdmin(admin.ModelAdmin):
    list_display = ['action', 'username', 'ip', 'time']
    list_filter = ['time']


@admin.register(AdminPanelEntry)
class AdminPanelEntryAdmin(admin.ModelAdmin):
    list_display = ['ip', 'valid', 'time']
    list_filter = ['time']


@admin.register(FlagAttemptEntry)
class FlagAttemptEntryAdmin(admin.ModelAdmin):
    list_display = ['team', 'valid', 'sharing', 'time']
    list_filter = ['time']
