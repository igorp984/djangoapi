from produto.models import Produto
from produto.serializers import ProdutoSerializer
from rest_framework import generics

# Create your views here.

class ProdutoListCreate(generics.ListCreateAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
