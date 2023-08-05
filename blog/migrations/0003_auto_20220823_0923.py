# Generated by Django 3.2.4 on 2022-08-23 16:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20220723_0201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 23, 16, 23, 53, 937951, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 23, 16, 23, 53, 919878, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=tinymce.models.HTMLField(),
        ),
    ]