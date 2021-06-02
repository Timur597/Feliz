from rest_framework.generics import ListAPIView
from branch.models import Branch
from branch.serializers import BranchSerializer


class BranchListApiView(ListAPIView):
    serializer_class = BranchSerializer
    queryset = Branch.objects.all()