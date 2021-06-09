from rest_framework.generics import ListAPIView, DestroyAPIView, UpdateAPIView, CreateAPIView, RetrieveUpdateAPIView
from branch.models import Branch
from branch.serializers import BranchSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from user.permissions import IsAdminUser


class BranchListApiView(ListAPIView):
    serializer_class = BranchSerializer
    queryset = Branch.objects.all()
    # permission_classes = (IsAuthenticated,)


class BranchCreateAPIView(CreateAPIView):
    serializer_class = BranchSerializer
    queryset = Branch.objects.all()
    # permission_classes = (IsAdminUser,)


class BranchUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = BranchSerializer
    queryset = Branch.objects.all()
    # permission_classes = (IsAdminUser,)


class BranchDestroyAPIView(DestroyAPIView):
    serializer_class = BranchSerializer
    queryset = Branch.objects.all()
    permission_classes = (IsAdminUser,)
