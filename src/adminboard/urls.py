from django.contrib import admin
from django.urls import path
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='/admin/django', permanent=False)),
    path('django/', admin.site.urls)]
