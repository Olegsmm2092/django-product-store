from django.db import models


class Product(models.Model):
    objects = None
    product_name = models.CharField(max_length=251)
    product_price = models.IntegerField()
    product_size = models.IntegerField()

    def __str__(self):
        return self.product_name


class Customer(models.Model):
    customer_name = models.CharField(max_length=51)
    customer_password = models.CharField(max_length=51)

    country = models.CharField(max_length=251, default='')
    city = models.CharField(max_length=251, default='')
    street = models.CharField(max_length=251, default='')
    house = models.CharField(max_length=251, default='')

    customer_product = models.ManyToManyField(Product, through='CustomerProduct')
    additional_field = models.CharField(max_length=100, default='Default Value')

    def __str__(self):
        return self.customer_name


class CustomerProduct(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
