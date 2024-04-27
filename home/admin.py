from django.contrib import admin
from home.models import *

# Register your models here.

admin.site.register(location)
admin.site.register(checkroute)
admin.site.register(customer)
admin.site.register(route)
admin.site.register(bus)
admin.site.register(busImage)
admin.site.register(BoardingDropping)
admin.site.register(reservation)
admin.site.register(passengerdetails)
admin.site.register(seatassignment)
admin.site.register(cancellation)

