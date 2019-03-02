from client.models import Client
from client.serializers import ClientSerializer
from rest_framework import generics

# Create your views here.

class ClientListCreate(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
