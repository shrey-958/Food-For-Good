# Generated by Django 3.0.4 on 2020-03-20 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0010_auto_20200319_1036'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='isOrdered',
            field=models.BooleanField(default=False),
        ),
    ]
