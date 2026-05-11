from rest_framework import serializers
from .models import (
    Category,
    MenuItem,
    Cart,
    Order,
    OrderItem
)


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'slug', 'title']


class MenuItemSerializer(serializers.ModelSerializer):

    category = serializers.StringRelatedField()

    class Meta:
        model = MenuItem
        fields = [
            'id',
            'title',
            'price',
            'featured',
            'category'
        ]


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id', 'menuitem', 'quantity', 'user', 'unit_price', 'price']
        read_only_fields = ['user', 'unit_price', 'price']


class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = [
            'id',
            'menuitem',
            'quantity',
            'unit_price',
            'price'
        ]


class OrderSerializer(serializers.ModelSerializer):

    orderitems = OrderItemSerializer(
        many=True,
        read_only=True,
        source='orderitem_set'
    )

    class Meta:
        model = Order
        fields = [
            'id',
            'user',
            'delivery_crew',
            'status',
            'total',
            'date',
            'orderitems'
        ]