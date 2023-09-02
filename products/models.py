from django.db import models
from django.utils import timezone
from uuid import uuid4
import os

# Create your models here.


def wrapper(instance, filename):
    ext = filename.split(".")[-1]
    return os.path.join("product_image/", "{}.{}".format(uuid4().hex, ext))


class Product(models.Model):
    product_category = models.ForeignKey(
        "category.Category", blank=True, null=True, on_delete=models.SET_NULL
    )
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1500)
    product_image = models.ImageField(upload_to=wrapper)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.title} - {self.product_category}"
