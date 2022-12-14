# Generated by Django 4.0.7 on 2022-08-23 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseInfo', '0003_rename_forgreeting_greeting'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListOfMetro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='MetroShortInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ofiName', models.CharField(max_length=100)),
                ('n_ofiName', models.CharField(default='', max_length=150)),
                ('city', models.TextField(default='', max_length=30)),
                ('server', models.TextField(default='', max_length=150)),
                ('openDate', models.DateField(default='29.02.2020', verbose_name='25-12-2000')),
                ('workTime', models.TextField(max_length=120)),
                ('emblem', models.ImageField(blank=True, null=True, upload_to='logomeaning/')),
                ('info', models.TextField(max_length='1200')),
                ('shortI', models.TextField(max_length=125)),
            ],
        ),
    ]
