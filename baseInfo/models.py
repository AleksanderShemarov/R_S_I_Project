from django.db import models
# from datetime import datetime
# from django.contrib.auth.models import User
# AbstractUser
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
    n_ofiName = models.CharField(max_length=150, null=True, blank=True)
    city = models.TextField(max_length=30)
    server = models.TextField(max_length=150)
    # openDate = models.DateField(trueDate(), default="29.02.2020")
    openDate = models.DateField(help_text="Example: YYYY-MM-DD")
    workTime = models.TextField(max_length=120, null=True, blank=True)
    emblem = models.ImageField(upload_to='logomeaning/', null=True, blank=True)
    commonInfo = models.TextField(max_length=1200, null=True, blank=True)
    history = models.TextField(max_length=1200, null=True, blank=True)
    hacks_facts = models.TextField(max_length=1200, null=True, blank=True)
    shortI = models.TextField(max_length=125)

    opened = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.ofiName}"


# class User(AbstractUser):
#
#     username = models.CharField(max_length=50, null=True, blank=True)
#     name = models.CharField(max_length=40)
#     surname = models.CharField(max_length=40)
#     email = models.EmailField()
#
#     def __str__(self):
#         return f"{self.name} {self.surname} ({self.email})"
#
#
# class UserForm(ModelForm):
#     class Meta:
#
#         model = User
#


class MetroInfo(models.Model):

    ofiname = models.CharField(max_length=100)
    popname = models.CharField(max_length=150, null=True, blank=True)
    locat = models.CharField(max_length=30)
    org = models.CharField(max_length=150)
    start = models.DateField()
    works = models.TextField(max_length=120)
    viewinf = models.CharField(max_length=125)
    symbol = models.ImageField(upload_to='logomeaning/', null=True, blank=True)
    intro = models.TextField(max_length=1200)
    HistorY = models.TextField(max_length=2400)
    # facts = models.TextField(max_length=1200, null=True, blank=True)

    def __str__(self):
        return f"{self.ofiname} (since {self.start}), {self.locat}"


class Ticket(models.Model):
    TYPES = [
        ((D := "Daily"), 'Daily'),
        ((H := "Hourly"), 'Hourly'),
    ]
    AGES = [
        ((GU := "Grown-ups"), '18 - 60 years'),
        ((STD := "Students"), '18 - 26 years'),
        ((SNR := "Seniors"), '60 - 65 years'),
        ((EldTEN := "ElderTeens"), '15 - 18 years'),
    ]
    VALUTES = [
        ((KCZ := "czech krone"), 'Czech Koruna, KCZ'),
    ]
    category = models.CharField(
        max_length=50,
        choices=TYPES,
        default=D
    )
    ages = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        choices=AGES,
        default=GU
    )
    name = models.CharField(max_length=50)
    price = models.FloatField(default=0.00)
    valute = models.TextField(
        max_length=50,
        choices=VALUTES,
        default=KCZ
    )
    picture = models.ImageField(upload_to='hourly_tickets', null=True, blank=True)
    info = models.TextField(null=True, blank=True, max_length=1000)

    metro = models.ForeignKey(MetroInfo, on_delete=models.SET_NULL, related_name='tickets', null=True, blank=True)

    def __str__(self):
        return f"{self.name}, {self.ages}; {self.category}"


class TableData(models.Model):

    image = models.ImageField(upload_to='exchange_table', null=True, blank=True)
    country = models.CharField(max_length=50)
    currency = models.CharField(max_length=50)
    symbol = models.CharField(max_length=3)
    price = models.FloatField(default=0.00, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.symbol = self.symbol.upper()
        return super(TableData, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.currency, self.symbol}"


class FactsModel(models.Model):

    name = models.CharField(max_length=75)
    image = models.ImageField(upload_to="facts_table")
    text = models.TextField(max_length=1000, null=True, blank=True)
    metro = models.ForeignKey(MetroInfo, on_delete=models.SET_NULL, related_name='facts', null=True, blank=True)

    def __str__(self):
        return f"{self.name}"
