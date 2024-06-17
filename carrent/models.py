from django.db import models

class Booking(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    email = models.EmailField()
    pick_up_date = models.DateField(null=True)
    place = models.CharField(max_length=255)

    def __str__(self):
        return self.name  
