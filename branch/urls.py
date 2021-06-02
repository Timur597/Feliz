
from django.urls import path
from .views import *

urlpatterns = [
    path('Branch/', BranchListApiView.as_view(), name='Branch'),
]