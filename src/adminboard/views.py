from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import HttpResponse


@staff_member_required
def index(request):
    return HttpResponse('admin panel here')
