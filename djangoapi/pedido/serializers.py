from rest_framework import serializers
from .models import Item, Pedido

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('pk','produto', 'quantidade', 'preco_unitario')

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

    def update(self, instance, validated_data):
        itens_data = validated_data.pop('item_set')
        instance.client = validated_data.get('client', instance.client)
        itens = list(instance.item_set.all())
        instance.save()
        for item_data in itens_data:
            item = itens.pop(0)
            item.produto = item_data.get('produto', item.produto)
            item.quantidade = item_data.get('quantidade', item.quantidade)
            item.preco_unitario = item_data.get('preco_unitario', item.preco_unitario)
            item.save()
        return instance
