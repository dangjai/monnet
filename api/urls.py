# website/urls.py       
from django.urls import path
from . import views

urlpatterns = [
    # path('api/status/', views.status_list),
    path('api/status/<int:pk>', views.status_detail),
    path('api/ackvolt/<int:pk>', views.ack_volt),

]