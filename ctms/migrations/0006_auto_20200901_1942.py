# Generated by Django 3.1 on 2020-09-01 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ctms', '0005_auto_20200901_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photographer',
            name='Profile',
            field=models.ImageField(upload_to='profile_pic'),
        ),
    ]
