# Generated by Django 4.0.7 on 2022-09-08 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('baseInfo', '0018_alter_ticket_metro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='metro',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tickets', to='baseInfo.metroinfo'),
        ),
    ]
