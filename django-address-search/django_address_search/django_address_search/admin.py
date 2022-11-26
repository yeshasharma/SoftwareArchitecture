from django.contrib import admin
from .models import Country
from .models import Address
from .models import AddressFormat

admin.site.register(Country)
admin.site.register(Address)
admin.site.register(AddressFormat)

