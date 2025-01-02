from django.db import models
from base.models import BaseModel


class Product(BaseModel):
    product_id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=255,default="")
    subcategory = models.CharField(max_length=255,default="")
    product_name = models.CharField(max_length=100,help_text="Enter Your Product Name")
    description = models.TextField()
    price = models.DecimalField(max_digits=10,default=0.00,decimal_places=2)
    image = models.ImageField(upload_to='shop/products_images/') 
    pub_date = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.product_name


class Contact(BaseModel):
    message_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    mobile = models.CharField(max_length=12)
    question = models.TextField()

    def __str__(self):
        return self.name + " " + self.question[0:15]