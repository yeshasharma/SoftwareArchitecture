from django.db import models
from django.db.models import ForeignKey, CharField


class Country(models.Model):
    cid = models.AutoField(primary_key=True)
    name = models.CharField('Country Name', max_length=50)

    def __str__(self):
        return self.name


class Address(models.Model):
    aid = models.AutoField(primary_key=True)
    cid = ForeignKey(to=Country, on_delete=models.CASCADE)
    title = CharField('Title', max_length=10)
    addressee_name = CharField('Addressee Name', max_length=100)
    postal_code = CharField('Postal Code', max_length=100)
    city = CharField('City', max_length=100)
    house_number = CharField('House Number', max_length=100)
    building_name = CharField('Building Name', max_length=100)
    street_number = CharField('Street Number', max_length=100)
    street_name = CharField('Street Name', max_length=100)
    postal_symbol = CharField('Postal Symbol', max_length=100)
    company_name = CharField('Company Name', max_length=100)

    def __str__(self):
        return self.addressee_name


class AddressFormat(models.Model):
    afid = models.AutoField(primary_key=True)
    cid = ForeignKey(to=Country, on_delete=models.CASCADE)
    name = CharField('Formats', max_length=100)

    def __str__(self):
        return self.name
