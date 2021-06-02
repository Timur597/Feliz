from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from client.models import Client
from client.serializers import ClientSerializer


class ClientListApiView(ListAPIView):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()

