from django.shortcuts import render
from django.http import HttpResponse

from owner.models import Owner


def exists(request):
    owner = Owner.objects.get(request.id)
    if owner is None:
        return render(request, 'owner.html', {'owner': owner})
    else:
        return render(request, 'empty_owner.html')
