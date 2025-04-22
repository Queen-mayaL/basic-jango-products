from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    price = models.FloatField()
    stock_quantity = models.IntegerField()
    category_id = models.IntegerField()
    supplier_id = models.IntegerField()

    class Meta:
        db_table = 'base_product'  # This sets the actual table name in the DB

    def __str__(self):
        return self.product_name

