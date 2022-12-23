from api.serializers import ReposSerializer
from rest_framework import viewsets, permissions
from api.models import Repos


class ReposViewSet(viewsets.ModelViewSet):
    queryset = Repos.objects.all()
    serializer_class = ReposSerializer
    # permission_classes = [permissions.IsAuthenticated]
