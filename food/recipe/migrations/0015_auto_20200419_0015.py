# Generated by Django 3.0.4 on 2020-04-18 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0014_auto_20200419_0013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='image',
            field=models.ImageField(blank=True, default='', upload_to=''),
        ),
    ]
