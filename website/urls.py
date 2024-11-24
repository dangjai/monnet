# website/urls.py       
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('website/<int:_id>', views.home, name = "device_detail"),
    path('website/ackpower/<int:_id>', views.ackpower, name = "ackpower"),
    path('website/acktemp/<int:_id>', views.acktemp, name = "acktemp"),
    path('website/ackhumi/<int:_id>', views.ackhumi, name = "ackhumi"),
]