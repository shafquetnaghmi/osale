from django.db import models
from cloudinary.models import CloudinaryField
from django.utils.text import slugify 
import uuid

def generate_uuid():
    random_uuid = uuid.uuid4()  # Generate a random UUID
    uuid_str = str(random_uuid).replace("-", "")  # Remove hyphens from the UUID string
    ten_digit_uuid = uuid_str[:8]  # Extract the first 10 characters
    return ten_digit_uuid

class CategoryModel(models.Model):
    name=models.CharField(max_length=200)
    slug=models.SlugField(max_length=200,unique=True,blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
          self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Product(models.Model):
    unique_id = models.CharField(default=generate_uuid, editable=False, unique=True, max_length=10)
    category=models.ForeignKey(CategoryModel,related_name='products',on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    slug=models.SlugField(max_length=200,unique=True,blank=True)
    image=CloudinaryField('image')
    description=models.TextField(max_length=500)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    link=models.URLField(max_length=500,null=True, blank=True)
    def save(self, *args, **kwargs):
        if not self.slug:
          self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class FeaturedProduct(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)










