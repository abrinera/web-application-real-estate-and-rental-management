from django.contrib import admin
from .models import Employee, Property, Rental, Transaction, Client,Payment

# Register your models here.

admin.site.register(Employee)
admin.site.register(Property)
admin.site.register(Rental)
admin.site.register(Transaction)
admin.site.register(Client)
admin.site.register(Payment)
