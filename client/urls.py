from django.urls import path
from .views import *

urlpatterns = [
    path('list/client', ClientListApiView.as_view()),
    path('create/client', ClientCreateAPIView.as_view()),
    path('update_client/<int:pk>/', ClientUpdateAPIView.as_view()),
    path('destroy_client/<int:pk>/', ClientDestroyAPIView.as_view()),

]