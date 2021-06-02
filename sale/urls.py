from django.urls import path
from sale.views import *

urlpatterns = [
    path('Sale/', SaleListApiView.as_view(), name='sale'),
    path('Sale/Product', SaleProductListApiView.as_view(), name='sale_product'),
]