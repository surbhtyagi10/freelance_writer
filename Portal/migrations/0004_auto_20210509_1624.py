# Generated by Django 3.2 on 2021-05-09 10:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portal', '0003_alter_userstory_story_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userstory',
            name='story_date',
            field=models.DateField(default=datetime.datetime(2021, 5, 9, 16, 23, 59, 929491), null=True),
        ),
        migrations.AlterField(
            model_name='userstory',
            name='user',
            field=models.IntegerField(null=True),
        ),
    ]
