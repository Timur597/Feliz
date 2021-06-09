from django.urls import path
from sale.views import *


urlpatterns = [
    path('list/sale', SaleListApiView.as_view()),
    path('create/sale', SaleCreateAPIView.as_view()),
    path('update_sale/<int:pk>/', SaleUpdateAPIView.as_view()),
    path('destroy_sale/<int:pk>/', SaleDestroyAPIView.as_view()),

    path('list/sale_product', SaleProductListApiView.as_view()),
    path('create/sale_product', SaleProductCreateAPIView.as_view()),
    path('update_sale_product/<int:pk>/', SaleProductUpdateAPIView.as_view()),
    path('destroy_sale_product/<int:pk>/', SaleProductDestroyAPIView.as_view()),

]