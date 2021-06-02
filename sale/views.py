from rest_framework.generics import ListAPIView
from sale.models import Sale, SaleProduct
from sale.serializers import SaleSerializer, SaleProductSerializer


class SaleListApiView(ListAPIView):
    serializer_class = SaleSerializer
    queryset = Sale.objects.all()


class SaleProductListApiView(ListAPIView):
    serializer_class = SaleProductSerializer
    queryset = SaleProduct.objects.all()