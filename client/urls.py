from django.urls import path
from .views import *

urlpatterns = [
    path('Client/', ClientListApiView.as_view(), name='Client'),
]