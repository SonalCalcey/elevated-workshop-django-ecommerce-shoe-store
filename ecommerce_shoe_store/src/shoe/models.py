from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, null=False)

    class Meta:
        db_table = 'category'


class Shoe(models.Model):
    name = models.CharField(max_length=50, null=False)
    image_url = models.CharField(null=True)
    price = models.FloatField(null=False)
    description = models.CharField(max_length=300, null=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    class Meta:
        db_table = 'shoe'


class ShoeSize(models.Model):
    size = models.IntegerField(null=False)
    shoe = models.ForeignKey(Shoe, on_delete=models.CASCADE)

    class Meta:
        db_table = 'shoe_size'
