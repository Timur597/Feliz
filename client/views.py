from rest_framework.generics import ListAPIView, DestroyAPIView, UpdateAPIView, CreateAPIView
from client.models import Client
from client.serializers import ClientSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class ClientListApiView(ListAPIView):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
    permission_classes = (IsAuthenticated,)


class ClientCreateAPIView(CreateAPIView):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
    permission_classes = (IsAdminUser,)


class ClientUpdateAPIView(UpdateAPIView):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
    permission_classes = (IsAuthenticated,)


class ClientDestroyAPIView(DestroyAPIView):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
    permission_classes = (IsAdminUser,)