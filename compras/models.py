from django.db import models

# Create your models here.
class Client(models.Model):
    email = models.EmailField()
    details = models.TextField(blank=True, null=True)

class Product(models.Model):
    title = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    tags = models.TextField(blank=True, null=True)

class Purchase(models.Model):
    # Una compra le pertenece a 1 cliente
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    # many to many
    products = models.ManyToManyField(Product, through='PurchaseItem')
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    state = models.CharField(max_length=15)
    zip_code = models.CharField(max_length=15)

class PurchaseItem(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveSmallIntegerField(default=0)
    state = models.CharField(max_length=50)
