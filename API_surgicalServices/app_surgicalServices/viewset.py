from rest_framework import viewsets
from .serializer import *
from .models import specialistsTeam, Services

class specialistsTeamViewset(viewsets.ModelViewSet):
    queryset = specialistsTeam.objects.all()
    serializer_class = specialistsTeam_serializer

class ServicesViewset(viewsets.ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = Services_serializer

