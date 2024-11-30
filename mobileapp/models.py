from django.db import models

# Create your models here.
class Category_Db(models.Model):
    Category_Name = models.CharField(max_length=100, null=True, blank=True)
    Description = models.CharField(max_length=100, null=True, blank=True)
    Category_Image = models.ImageField(upload_to="Category_Images", null=True, blank=True)

