from django.shortcuts import render
from .models import Item, Pedido
from .serializers import PedidoSerializer, ItemSerializer
from rest_framework import generics

# Create your views here.

class ItemListCreate(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class PedidoListCreate(generics.ListCreateAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
class PedidoUpdateApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
