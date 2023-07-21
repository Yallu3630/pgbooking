from django.contrib import admin
from . import models

# Register your models here.

class userAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'phno', 'email', 'password')

class roomAdmin(admin.ModelAdmin):
    list_display = ('id', 'room_name', 'room_no', 'cap', 'rent_room', 'description')

class bookroomAdmin(admin.ModelAdmin):
    list_display = ('id', 'booked_user', 'booked_room_name', 'booked_room_no', 'booked_cap', 'booked_rent_room', 'booked_description')

admin.site.register(models.users, userAdmin)    
admin.site.register(models.room, roomAdmin)
admin.site.register(models.bookingrooms, bookroomAdmin)