from django.db import models


class Address(models.Model):
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    house = models.CharField(max_length=255)

    def __str__(self):
        return self.city + " || " + self.street + " || " + self.house


class Passport(models.Model):
    inn = models.CharField(max_length=255)
    expired_date = models.DateField()

    def __str__(self):
        return self.inn + " || " + self.expired_date


class Client(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    passport = models.OneToOneField(Passport, on_delete=models.CASCADE, primary_key=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + " " + self.surname + " || " + self.passport.inn + " || " + self.address.city




