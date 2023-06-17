from django.db import models


# Create your models here.
from taggit.managers import TaggableManager


class Restaurant(models.Model):
    name = models.CharField(max_length=100)

    address = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, default='')
    image = models.ImageField(upload_to='restuarant-images', default='default.png')
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    website = models.URLField()
    tags = TaggableManager()


    def __str__(self):
        return self.name


class Reservation(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='reservations')
    name = models.CharField(max_length=200)
    email = models.EmailField(null=False)
    date = models.DateField()
    time = models.TimeField()
    party_size = models.PositiveIntegerField()

    def __str__(self):
        return f"Reservation at {self.restaurant} for {self.party_size} people on {self.date} at {self.time}"


class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='menus')
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='menu-images', default='default.png')
    price = models.DecimalField(max_digits=4, decimal_places=2)
    menu_item_description = models.TextField(max_length=1000, default='')

    def __str__(self):
        return self.name
