from django.contrib import admin
from .models import Greeting, MetroShortInfo


# Register your models here.

class GreetingAdmin(admin.ModelAdmin):

    list_display = ("pictureName", "pictureImg", "pictureText")
    search_fields = ["pictureName"]


class MetroShortInfoAdmin(admin.ModelAdmin):

    list_display = ("ofiName", "city", "openDate", "emblem")
    search_fields = ["ofiName", "city"]


admin.site.register(Greeting, GreetingAdmin)
admin.site.register(MetroShortInfo, MetroShortInfoAdmin)
