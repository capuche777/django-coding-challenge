from .models import Product

from rest_framework import serializers


class OrderItemSerializer(serializers.Serializer):
    product = serializers.CharField()
    quantity = serializers.IntegerField()


class OrderSerializer(serializers.Serializer):
    products = serializers.ListField(child=OrderItemSerializer())


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'quantity']
        read_only_fields = ['id']
