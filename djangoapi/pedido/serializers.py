from rest_framework import serializers
from .models import Item, Pedido

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('produto', 'quantidade', 'preco_unitario')

class PedidoSerializer(serializers.ModelSerializer):
    item_set = ItemSerializer(many=True)

    class Meta:
        model = Pedido
        fields = ('client', 'item_set')

    def create(self, validated_data):
        itens_data = validated_data.pop('item_set')
        pedido = Pedido.objects.create(**validated_data)
        for item_data in itens_data:
            Item.objects.create(pedido=pedido, **item_data)
        return pedido
