from django.urls import path
from api import views

urlpatterns = [
    
    path('',views.index ,name='index'),
    
    #API
    path('category/',views.CategoryAPIView.as_view(),name='api_category'),
    path('category-detail/<int:pk>/',views.CategoryDetailAPIView.as_view(),name='api_category_detail'),
    
    path('product/',views.ProductAPIView.as_view(),name='api_product'),
    path('product-detail/<int:pk>/',views.ProductDetailAPIView.as_view(),name='api_product_detail'),
    
    path('cart/',views.CartAPIView.as_view(),name='api_cart'),
    path('cart-detail/<int:pk>/',views.CartDetailAPIView.as_view(), name='api_cart_detail'),
    
    path('cartItem/',views.CartItemAPIView.as_view(),name='api_cartItem'),
    path('cartItem-detail/<int:pk>/', views.CartItemDetailAPIView.as_view(), name='api_cartItem_detail'),
    
    
    
]