# Generated by Django 2.2.4 on 2019-08-17 12:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitor', '0005_auto_20190817_0150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userregistration',
            name='CreatedDate',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='userregistration',
            name='ExpiredDate',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='userregistration',
            name='ModifiedDate',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='userregistration',
            name='StartDate',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]