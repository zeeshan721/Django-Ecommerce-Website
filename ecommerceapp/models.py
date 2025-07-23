from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length = 122)
    email = models.CharField(max_length=122)
    desc = models.TextField(max_length=50)
    phone = models.CharField(max_length=12)
    date = models.DateField()




    def __str__(self):
        return self.name


class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    image = models.ImageField(upload_to='images/images', null = True, blank=True)



    def __str__(self):
        return self.product_name