# Generated by Django 3.2.4 on 2023-01-01 15:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20220909_1027'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='short_desc',
            field=models.TextField(default=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 1, 15, 22, 14, 193599, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 1, 15, 22, 14, 191595, tzinfo=utc)),
        ),
    ]
