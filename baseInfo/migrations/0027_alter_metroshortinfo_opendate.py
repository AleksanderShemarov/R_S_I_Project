# Generated by Django 4.0.7 on 2022-09-14 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseInfo', '0026_alter_metroshortinfo_commoninfo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metroshortinfo',
            name='openDate',
            field=models.DateField(help_text='Example: YYYY-MM-DD'),
        ),
    ]
