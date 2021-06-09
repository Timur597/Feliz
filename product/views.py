from rest_framework.generics import ListAPIView, DestroyAPIView, UpdateAPIView, CreateAPIView
from product.models import Product, TypeProduct, Category
from product.serializers import ProductSerializer, TypeProductSerializer, CategorySerializer
from rest_framework.permissions import IsAuthenticated
from user.permissions import IsAdminUser


class ProductListApiView(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    # permission_classes = (IsAuthenticated,)


class ProductCreateAPIView(CreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = (IsAdminUser,)


class ProductUpdateAPIView(UpdateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = (IsAdminUser,)


class ProductDestroyAPIView(DestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = (IsAdminUser,)


class TypeProductListApiView(ListAPIView):
    serializer_class = TypeProductSerializer
    queryset = TypeProduct.objects.all()
    permission_classes = (IsAuthenticated,)


class TypeProductCreateAPIView(CreateAPIView):
    serializer_class = TypeProductSerializer
    queryset = TypeProduct.objects.all()
    permission_classes = (IsAdminUser,)


class TypeProductUpdateAPIView(UpdateAPIView):
    serializer_class = TypeProductSerializer
    queryset = TypeProduct.objects.all()
    permission_classes = (IsAdminUser,)


class TypeProductDestroyAPIView(DestroyAPIView):
    serializer_class = TypeProductSerializer
    queryset = TypeProduct.objects.all()
    permission_classes = (IsAdminUser,)


class CategoryListApiView(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = (IsAuthenticated,)


class CategoryCreateAPIView(CreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = (IsAdminUser,)


class CategoryUpdateAPIView(UpdateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = (IsAdminUser,)


class CategoryDestroyAPIView(DestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = (IsAdminUser,)