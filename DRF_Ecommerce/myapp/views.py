from django.shortcuts import render,get_object_or_404
from myapp.models import Category,Product,Cart,CartItem
from myapp.serializers import CategorySerializer,ProductSerializer,CartSerializer,CartItemSerializer



def index(request):
    return render(request, 'index.html')


#API

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class CategoryAPIView(APIView):
    def get(self,request):
        category = Category.objects.all()
        serializer = CategorySerializer(category,many =True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer = CategorySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            print("Successfully Save New Category")
            
        else:
            print(serializer.errors)

        return Response (serializer.data, status=status.HTTP_201_CREATED)
    
class CategoryDetailAPIView(APIView):
    def get_object(self,pk):
        return get_object_or_404(Category,id=pk)
    
    def get(self,request,pk):
        category = self.get_object(pk)
        serializer = CategorySerializer(category)
        return Response (serializer.data, status=status.HTTP_200_OK)
    
    def put(self,request,pk):
        category = self.get_object(pk)
        serilaizer = CategorySerializer(category,data = request.data)
        if serilaizer.is_valid():
            serilaizer.save()
            print("Successfully Edited Category")
        else:
            print(serilaizer.errors)
        
        return Response(serilaizer.data , status=status.HTTP_201_CREATED)
    
    def delete(self,request,pk):
        Category = self.get_object(pk)
        Category.delete()
        return Response(status=status.HTTP_200_OK)
    
class ProductAPIView(APIView):
    def get(self,request):
        product = Product.objects.all()
        serializer = ProductSerializer(product,many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    def post(self,request):
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            print('Successfully created new Product')
            
        else:
            print(serializer.data)
            
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    
class ProductDetailAPIView(APIView):
    def get_object(self,pk):
        return get_object_or_404(Product,id=pk)
    
    def get(self,request,pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self,request,pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product ,data=request.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def delete(self,request,pk):
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_200_OK)
               
               
class CartAPIView(APIView):
    def get(self,request):
        cart = Cart.objects.all()
        serializer = CartSerializer(cart,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer = CartSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            print("Successfully created new Cart")
            
        else:
            print(serializer.error)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    
class CartDetailAPIView(APIView):
    def get_object(self,pk):
        return get_object_or_404(Cart,id=pk)
    
    def get(self,request,pk):
        cart = self.get_object(pk)
        serializer = CartSerializer(cart)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self,request,pk):
        cart = self.get_object(id=pk)
        serializer = CartSerializer(cart ,data = request.data)
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    
    def delete(self,request,pk):
        cart = self.get_object(pk)
        cart.delete()
        return Response(status=status.HTTP_200_OK)


class CartItemAPIView(APIView):
    def get(self,request):
        cartItem = CartItem.objects.all()
        serializer = CartItemSerializer(cartItem,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


    def post(self,request):
        serializer = CartItemSerializer(data =request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            print("Successfully Created New CartItem")
            
        else:
            print(serializer.error_messages)
        
        return Response(serializer.data,status=status.HTTP_201_CREATED)

class CartItemDetailAPIView(APIView):
    def get_object(self,pk):
        return get_object_or_404(CartItem,id=pk)
    
    def get(self,request,pk):
        cartItem = self.get_object(pk)
        serializer = CartItemSerializer(cartItem)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    def put(self,request,pk):
        cartItem = self.get_object(pk)
        serializer = CartItemSerializer(cartItem,data = request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            print("Successfully Created New CartItem")
        
        else:
            print(serializer.errors)
            
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    
    def delete(self,request,pk):
        cartItem = self.get_object(pk)
        cartItem.delete()
        return Response(status=status.HTTP_200_OK)
    

        
    

        