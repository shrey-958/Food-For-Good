# Generated by Django 3.0.4 on 2020-03-18 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='isVeg',
            field=models.BooleanField(default=False),
        ),
    ]
