from django.shortcuts import render
from django.http import HttpResponse
from api.models import MNStatus, MNSetup
from .models import DeviceName
import logging

logger = logging.getLogger('django')

# def home(request):
#     Statuss = MNStatus.objects.
#     return render(request, 'website/_index.html', {
#         'Statuss': Statuss
#     })

def home(request, _id=1):
    Statuss = MNStatus.objects.get(id=_id)
    Setups = MNSetup.objects.get(id=_id)
    DeviceNames = DeviceName.objects.get(id=_id).DeviceName
    DeviceList = DeviceName.objects.all()
    return render(request, 'website/_index.html', {
        'Statuss': Statuss,
        'Setups': Setups,
        'DeviceNames': DeviceNames,
        'DeviceList' : DeviceList
    })

def ackpower(request, _id=1):
    Setups = MNSetup.objects.get(id=_id)
    Setups.VoltStatus = 4
    Setups.save()
    return home(request,_id)

def acktemp(request, _id=1):
    Setups = MNSetup.objects.get(id=_id)
    Setups.TempStatus = 4
    Setups.save()
    return home(request,_id)

def ackhumi(request, _id=1):
    Setups = MNSetup.objects.get(id=_id)
    Setups.HumiStatus = 4
    Setups.save()
    return home(request,_id)
# Create your views here.
