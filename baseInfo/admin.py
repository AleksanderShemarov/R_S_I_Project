from django.contrib import admin
from .models import Greeting, MetroShortInfo, Ticket, MetroInfo, TableData


# Register your models here.

class GreetingAdmin(admin.ModelAdmin):

    list_display = ("pictureName", "pictureImg", "pictureText")
    search_fields = ["pictureName"]


class MetroShortInfoAdmin(admin.ModelAdmin):

    list_display = ("ofiName", "city", "openDate", "emblem")
    search_fields = ["ofiName", "city"]


class TicketAdmin(admin.ModelAdmin):

    list_display = ("name", "ages", "category", "price", "valute")
    search_fields = ["name", "category", "ages"]


class MetroInfoAdmin(admin.ModelAdmin):

    list_display = ("ofiname", "locat", "start", "symbol")
    search_fields = ["ofiname", "locat"]


class TableDataAdmin(admin.ModelAdmin):

    list_display = ("currency", "symbol", "image")
    search_fields = ["currency", "symbol"]
# for the future exchange table for "metro.html" and "REGmetro.html" templates.

admin.site.register(Greeting, GreetingAdmin)
admin.site.register(MetroShortInfo, MetroShortInfoAdmin)
admin.site.register(Ticket, TicketAdmin)
admin.site.register(MetroInfo, MetroInfoAdmin)
admin.site.register(TableData, TableDataAdmin)
