
from django.db import models
class Product(models.Model):
    name = models.CharField(max_length=50, db_column="product_name")
    price = models.FloatField(db_column="product_price")

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "products"


