from rest_framework import mixins
from rest_framework import viewsets

from daskmanager.models import DaskTask
from daskmanager.serializers import DaskTaskSerializer


class DaskTaskViewSet(mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.DestroyModelMixin,
                      viewsets.GenericViewSet):
    serializer_class = DaskTaskSerializer
    queryset = DaskTask.objects.all()
