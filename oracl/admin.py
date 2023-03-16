from django.contrib import admin
from .models import Client, Passport, Address

admin.site.register(Client)
admin.site.register(Passport)
admin.site.register(Address)
