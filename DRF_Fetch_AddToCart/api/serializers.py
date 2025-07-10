from rest_framework import serializers
from api.models import Category,Product,Cart,CartItem

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'created_at',
            'edited_at'
        ]
        
class ProductSerializer(serializers.ModelSerializer):
    
    # categoryName = CategorySerializer( )
    
    class Meta:
        model = Product
        fields = [
            'id',
            'category',
            'name',
            'price',
            'stock',
            'description',
            'created_at',
            'edited_at'
            
        ]

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = [
            'id',
            'created_at'
        ]
        
class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = [
            'id',
            'cart',
            'product',
            'quantity',
            'created_at',
            'edited_at'
        ]
    
