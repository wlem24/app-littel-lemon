from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50)  # E.g., 'Appetizer', 'Main Course'

    def __str__(self):
        return self.name

class Reservation(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    number_of_guests = models.IntegerField()
    reservation_date = models.DateTimeField()

    def __str__(self):
        return f"Reservation for {self.name} on {self.reservation_date}"
