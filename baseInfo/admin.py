from django.contrib import admin
from .models import Greeting, MetroShortInfo, Ticket


# Register your models here.

class GreetingAdmin(admin.ModelAdmin):

    list_display = ("pictureName", "pictureImg", "pictureText")
    search_fields = ["pictureName"]


class MetroShortInfoAdmin(admin.ModelAdmin):

    list_display = ("ofiName", "city", "openDate", "emblem")
    search_fields = ["ofiName", "city"]


class TicketAdmin(admin.ModelAdmin):

    list_display = ("name", "ages", "category", "price", "valute")
    search_fields = ["name", "category"]


admin.site.register(Greeting, GreetingAdmin)
admin.site.register(MetroShortInfo, MetroShortInfoAdmin)
admin.site.register(Ticket, TicketAdmin)
