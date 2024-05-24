from django.db import models

# Create your models here.

# a booking model with ID as PK, Name with varchar(255), No_of_guests with int(6), BookingDate with datetime
class Booking(models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)
    No_of_guests = models.IntegerField()
    BookingDate = models.DateTimeField()

# a Menu model with ID as PK, Title with varchar(255), Price with decimal(10,2), Inventory with int(5)
class Menu(models.Model):
    ID = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=255)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Inventory = models.IntegerField()
    def __str__(self):
        return f'{self.Title} - {str(self.Price)}'