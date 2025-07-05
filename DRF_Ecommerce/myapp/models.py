from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    

class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=8 ,decimal_places=2)
    stock = models.PositiveIntegerField()
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name
    

class Cart(models.Model):
    created_at = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.id}'
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product,on_delete=models.CASCADE, related_name='products')
    quantity = models.PositiveIntegerField(default=1)
    
