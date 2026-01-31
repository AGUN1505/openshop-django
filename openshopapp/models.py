from django.db import models
import uuid

# Create your models here.
class Product(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=50)
    shop = models.CharField(max_length=50)
    price = models.IntegerField()
    sku = models.CharField(max_length=50)
    description = models.TextField()
    location = models.CharField(max_length=50)
    discount = models.IntegerField()
    category = models.CharField(max_length=50)
    stock = models.IntegerField()
    is_available = models.BooleanField()
    picture = models.CharField(max_length=500)
    is_delete = models.BooleanField(default=False)
