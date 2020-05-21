from django.db import models

# Create your models here.
class Donor(models.Model):
    name = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    email = models.EmailField()
    amount = models.PositiveIntegerField()
    paid = models.BooleanField(default=False)

    def __str__(self):
        return self.name+", "+self.city

    def get_amount(self):
        return (self.amount)*100



