# Generated by Django 4.0.7 on 2022-08-18 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ForGreeting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pictureName', models.CharField(max_length=50)),
                ('pictureImg', models.ImageField(blank=True, null=True, upload_to='logomeaning/')),
                ('pictureText', models.TextField(max_length=1200)),
            ],
        ),
    ]
