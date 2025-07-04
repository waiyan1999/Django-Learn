from django.urls import path
from myapp import views

urlpatterns = [
    
    path('',views.index ,name='index'),
    
    #API
    path('api/category/',views.CategoryAPIView.as_view(),name='api_category'),
    path('api/category-detail/<int:pk>/',views.CategoryDetailAPIView.as_view(),name='api_category_detail'),
    
    path('api/product/',views.ProductAPIView.as_view(),name='api_product'),
    path('api/product-detail/<int:pk>/',views.ProductDetailAPIView.as_view(),name='api_product_detail'),
    
    path('api/cart/',views.CartAPIView.as_view(),name='api_cart'),
    path('api/cart-detail/<int:pk>/',views.CartDetailAPIView.as_view(), name='api_cart_detail'),
    
    path('api/cartItem/',views.CartItemAPIView.as_view(),name='api_cartItem'),
    path('api/cartItem-detail/<int:pk>/', views.CartItemDetailAPIView.as_view(), name='api_cartItem_detail'),
    
    
    
]