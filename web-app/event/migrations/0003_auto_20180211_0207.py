# Generated by Django 2.0.2 on 2018-02-11 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_auto_20180210_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_time',
            field=models.CharField(default='', max_length=100),
        ),
    ]
