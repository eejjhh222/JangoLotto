# Generated by Django 2.2.5 on 2019-11-21 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getCron', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lotto_data',
            name='prize6',
            field=models.IntegerField(default=0),
        ),
    ]
