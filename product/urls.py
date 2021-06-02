from django.urls import path
from .views import *

urlpatterns = [
    path('Product/', ProductListApiView.as_view(), name='Product'),
    path('Product/detail/<str:pk>/', ProductDetailApiView.as_view(), name='Product_detail'),
    path('TypeProduct/', TypeProductListApiView.as_view(), name='TypeProduct'),
    path('TypeProduct/detail/<str:pk>/', TypeProductDetailApiView.as_view(), name='TypeProduct_detail'),
    path('Category/', CategoryListApiView.as_view(), name='Category'),
    path('Category/detail/<str:pk>/', CategoryDetailApiView.as_view(), name='Category_detail'),

]