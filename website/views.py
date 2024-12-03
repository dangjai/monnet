from django.shortcuts import render, redirect
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

def ack(request):
    _id = id=request.POST.get("id")

    Setups = MNSetup.objects.get(id=_id)
    match request.POST.get("type"):
        case 'temp':
            Setups.TempStatus = 3
        case 'volt':
            Setups.VoltStatus = 3
        case 'humi':
            Setups.HumiStatus = 3

    Setups.save()
    return redirect("home",_id = _id)
# Create your views here.
