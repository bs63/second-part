from __future__ import unicode_literals

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.validators import RegexValidator
from django.urls import reverse


class Client(models.Model):
    nif = models.TextField()
    Fname = models.CharField(max_length=120)
    Lname = models.CharField(max_length=120)
    address = models.CharField(max_length=120)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list

    def __unicode__(self):
        return u"%s" % self.nif

    def get_absolute_url(self):
        return reverse('clients:client_detail', kwargs={'pk': self.pk})


class Table(models.Model):
    table_number = models.IntegerField(validators=[MaxValueValidator(20), MinValueValidator(1)])
    capacity = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)])
    status = models.CharField(max_length = 15)
    num_per_sitting = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)])
    serv_staff_id = models.TextField()
    client = models.ForeignKey(Client, default=1, related_name='tables', on_delete=models.CASCADE)

    def __unicode__(self):
        return u"%s" % self.table_number


class Order(models.Model):
    orderid = models.TextField()
    order_date =models.DateField()
    client = models.ForeignKey(Client, default=1, related_name='orders', on_delete=models.CASCADE)
    quantity = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)])
    pick_up_date = models.DateField()

    def __unicode__(self):
        return u"%s" % self.orderid


class Waiter(models.Model):
    waiterid = models.TextField()
    lastname = models.CharField(max_length=120)
    firstname = models.CharField(max_length=120)
    Username = models.CharField(max_length=120)
    phone_regex2 = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number_wait = models.CharField(validators=[phone_regex2], max_length=17, blank=True) # validators should be a list
    password = models.CharField(max_length=120)
    order = models.ManyToManyField(Order)


    def __unicode__(self):
        return u"%s" % self.waiterid

class Dishes(models.Model):
    meal_id = models.TextField()
    name = models.CharField(max_length=120)
    date_of_meal = models.DateField()
    price = models.IntegerField(validators=[MaxValueValidator(50), MinValueValidator(1)])
    description = models.TextField(blank = True, null = True)
    rating = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(1)])
    images = models.ImageField(upload_to="restaurant", blank=True, null=True)
    similardishes = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return u"%s" % self.name

class Menu(models.Model):
    dish = models.ForeignKey(Dishes, on_delete=models.CASCADE)

class Review(models.Model):
    RATING_CHOICES = ((1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five'))
    rating = models.PositiveSmallIntegerField('Rating (stars)', blank=False, default=3, choices=RATING_CHOICES)
    comment = models.TextField(blank=True, null=True)
    date = models.DateField()
    client = models.ForeignKey(Client, default=1, related_name='reviews', on_delete=models.CASCADE)

class City(models.Model):
    name = models.CharField(max_length = 25)

    def __str__(self):
        return self.name
    class meta:
        verbose_name_plural = 'cities'
