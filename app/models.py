from django.db import models

# Create your models here.


# Product => title, price, description, rating, discount, quantity,
# Image => image, product -> fk

class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    description = models.TextField(max_length=255, null=True)
    # price = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.FloatField()
    rating = models.FloatField()
    discount = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)

    @property
    def discounted_price(self):
        if self.discount > 0:
            return self.price * (1 - self.discount/100)
        return self.price

    def __str__(self):
        return self.name


class Image(models.Model):
    image = models.ImageField(upload_to='products', null=True)
    product = models.ForeignKey('app.Product', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.image.name


