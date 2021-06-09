from rest_framework.generics import ListAPIView, DestroyAPIView, UpdateAPIView, CreateAPIView
from sale.models import Sale, SaleProduct
from sale.serializers import SaleSerializer, SaleProductSerializer


class SaleListApiView(ListAPIView):
    serializer_class = SaleSerializer
    queryset = Sale.objects.all()


class SaleCreateAPIView(CreateAPIView):
    serializer_class = SaleSerializer
    queryset = Sale.objects.all()


class SaleUpdateAPIView(UpdateAPIView):
    serializer_class = SaleSerializer
    queryset = Sale.objects.all()


class SaleDestroyAPIView(DestroyAPIView):
    serializer_class = SaleSerializer
    queryset = Sale.objects.all()


class SaleProductListApiView(ListAPIView):
    serializer_class = SaleProductSerializer
    queryset = SaleProduct.objects.all()


class SaleProductCreateAPIView(CreateAPIView):
    serializer_class = SaleProductSerializer
    queryset = SaleProduct.objects.all()


class SaleProductUpdateAPIView(UpdateAPIView):
    serializer_class = SaleProductSerializer
    queryset = SaleProduct.objects.all()


class SaleProductDestroyAPIView(DestroyAPIView):
    serializer_class = SaleProductSerializer
    queryset = SaleProduct.objects.all()