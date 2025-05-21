from django.db import models

# Create your models here.
class Coffee(models.Model):
    name=models.CharField(max_length=255)
    price=models.FloatField()
    quantity=models.IntegerField()
    image=models.CharField(max_length=2058)


class Cartitem(models.Model):
    coffee=models.ForeignKey(Coffee,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.coffee.name} x {self.quantity}"
    def get_total_price(self):
        return self.coffee.price*self.quantity


