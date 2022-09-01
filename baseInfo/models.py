from django.db import models
# from datetime import datetime
# Create your models here.


class Greeting(models.Model):

    pictureName = models.CharField(max_length=50)
    pictureImg = models.ImageField(upload_to='logomeaning/')
    pictureText = models.TextField(max_length=1200)

    def __str__(self):
        return f"{self.pictureName}"


# class ListOfMetro(models.Model):
#
#     ...


class MetroShortInfo(models.Model):

    # @staticmethod
    # def trueDate(year : int = 2000, month : int = 12, day : int = 25):
    #     """months from 1 to 12, control if date exists"""
    #     return datetime.strftime(datetime(year, month, day), '%d-%m-%Y')

    ofiName = models.CharField(max_length=100)
    n_ofiName = models.CharField(max_length=150, default="")
    city = models.TextField(max_length=30, default="")
    server = models.TextField(max_length=150, default="")
    # openDate = models.DateField(trueDate(), default="29.02.2020")
    openDate = models.DateField()
    workTime = models.TextField(max_length=120)
    emblem = models.ImageField(upload_to='logomeaning/', null=True, blank=True)
    commonInfo = models.TextField(max_length=1200)
    history = models.TextField(max_length=1200, default="")
    hacks_facts = models.TextField(max_length=1200, default="")
    shortI = models.TextField(max_length=125)

    def __str__(self):
        return f"{self.ofiName}"
