
from django.urls import path
from .views import *

urlpatterns = [
    path('list/product', ProductListApiView.as_view()),
    path('create/product', ProductCreateAPIView.as_view()),
    path('update_product/<int:pk>/', ProductUpdateAPIView.as_view()),
    path('destroy_product/<int:pk>/', ProductDestroyAPIView.as_view()),

    path('list/product_type', TypeProductListApiView.as_view()),
    path('create/product_type', TypeProductCreateAPIView.as_view()),
    path('update_product_type/<int:pk>/', TypeProductUpdateAPIView.as_view()),
    path('destroy_product_type/<int:pk>/', TypeProductDestroyAPIView.as_view()),

    path('list/', ProductListApiView.as_view()),
    path('create/', CategoryCreateAPIView.as_view()),
    path('update/<int:pk>/', CategoryUpdateAPIView.as_view()),
    path('destroy/<int:pk>/', CategoryDestroyAPIView.as_view()),

]