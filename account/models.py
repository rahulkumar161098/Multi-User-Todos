
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
PRODUCT_SIZE= (
    ('Small','Small'),
    ('Medium', 'Medium'),
    ('Large', 'Large'),
    ('Extra', 'Extra Large'),
)

PRODUCT_CHATEGORY=[
    ('Electronics',(
        ('Laptop', 'Taptop'),
        ('Mobile', 'Mobile')
    )),
    ('Cloth',(
        ('TW', 'Top Wear'),
        ('BW', 'Bottom Wear'),
    ))
]


class Product(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True,default=1)
    p_tag_line= models.CharField(max_length=100)
    p_price= models.IntegerField()
    p_selling_price= models.IntegerField()
    p_discount= models.IntegerField()
    p_image= models.FileField(upload_to='product_img')
    p_size= models.CharField(choices=PRODUCT_SIZE,max_length=10, default='------')
    p_chategory= models.CharField(choices=PRODUCT_CHATEGORY, max_length=20, default='------')
    p_brand= models.CharField(max_length=20)
    p_desc= models.TextField(max_length=500)

    # def __str__ (self):
    #     return str(self.id)

class Customer(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE, blank=True,null=True, default=1)
    # product= models.ForeignKey(Product, on_delete=models.CASCADE, blank=True,null=True,default=1)
    name= models.CharField(max_length=50)
    number= models.CharField(max_length=12)
    local_address= models.CharField(max_length=200)
    city= models.CharField(max_length=50)
    state= models.CharField(max_length=50)
    zip_code= models.CharField(max_length=6)


class Todo(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    title= models.CharField(max_length=200)
    body= models.CharField(max_length=1000)
    created_at= models.DateTimeField(auto_now_add=True)