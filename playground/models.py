from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=6,default="password")
    currency_amount = models.DecimalField(max_digits=10, decimal_places=2)
    user_id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=255)
    is_selling = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.name