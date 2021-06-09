from django.urls import path
from .views import *

urlpatterns = [
    path('list/branch', BranchListApiView.as_view()),
    path('create/branch', BranchCreateAPIView.as_view()),
    path('update_branch/<int:pk>/', BranchUpdateAPIView.as_view()),
    path('destroy_branch/<int:pk>/', BranchDestroyAPIView.as_view()),
]