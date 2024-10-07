from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    popularity = models.IntegerField()
    image = models.ImageField(null=True,blank=True,default='/placeholder.png')

    def __str__(self):
        return f"{self.name} - {self.popularity}"

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    categories = models.ManyToManyField(Category,related_name="products")
    image = models.ImageField(null=True,blank=True,default='/placeholder.png')


    def __str__(self):
        return f"{self.name} - {self.price}"
    
class Cart(models.Model):
    products = models.ManyToManyField(Product)

    def __str__(self):
        return f"Cart {self.id}"

    def total_price(self):
        total = sum(product.price for product in self.products.all())
        return total