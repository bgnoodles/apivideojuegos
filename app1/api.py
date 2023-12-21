from .models import Videojuego
from rest_framework import viewsets, permissions
from .serializers import VideojuegoSerializer

class VideojuegoViewset(viewsets.ModelViewSet):
    queryset = Videojuego.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = VideojuegoSerializer