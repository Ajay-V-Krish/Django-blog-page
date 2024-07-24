# Generated by Django 5.0.7 on 2024-07-24 04:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.CharField(max_length=1000000)),
                ('date_time', models.DateTimeField(blank=True, default=datetime.datetime(2024, 7, 24, 10, 3, 45, 31697))),
            ],
        ),
    ]
