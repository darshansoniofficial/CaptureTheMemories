# Generated by Django 3.1 on 2020-09-02 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ctms', '0007_auto_20200902_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photographer',
            name='Profile',
            field=models.ImageField(upload_to='media/profile_pic'),
        ),
        migrations.AlterField(
            model_name='photos',
            name='image',
            field=models.ImageField(upload_to='media/images/'),
        ),
    ]
