from django.db import models

from django.utils import timezone


# Create your models here.
class Order(models.Model):
    NEW = 1
    PENDING = 2
    REVIEWED = 3
    DONE = 4
    OPTIONS = (
        (NEW, "New Order"),
        (PENDING, "Pending Order"),
        (REVIEWED, "Reviewed"),
        (DONE, "Order Closed"),
    )

    product = models.ForeignKey(
        "products.Product", blank=True, null=True, on_delete=models.SET_NULL
    )
    member = models.ForeignKey("accounts.Member", on_delete=models.CASCADE)
    status = models.IntegerField(choices=OPTIONS, default=NEW)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.product} - {self.status}"
