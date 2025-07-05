from rest_framework import serializers
from myapp.models import Category,Product,Cart,CartItem

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'name'
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
            # 'categoryName'
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
            'quantity'
        ]
    
