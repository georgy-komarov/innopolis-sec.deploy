from django.contrib import admin
from adminboard.models import Task, Tag

admin.site.register(Tag)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['name', 'points', 'flag']
    list_filter = ['name']
