from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from product.models import Product, TypeProduct, Category
from product.serializers import  ProductSerializer, TypeProductSerializer, CategorySerializer


class ProductListApiView(ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductDetailApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class TypeProductListApiView(ListAPIView):
    serializer_class = TypeProductSerializer
    queryset = TypeProduct.objects.all()


class TypeProductDetailApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = TypeProductSerializer
    queryset = TypeProduct.objects.all()


class CategoryListApiView(ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryDetailApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


