# Generated by Django 3.1 on 2020-09-01 13:14

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='photographer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=30, unique=True)),
                ('Profile', models.ImageField(upload_to='')),
                ('Email_ID', models.EmailField(max_length=255, unique=True)),
                ('Mobile_No', models.CharField(max_length=10, unique=True)),
                ('DOB', models.DateField()),
                ('Gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('Address', models.TextField()),
                ('Bio', models.TextField(blank=True, null=True)),
                ('Skills', models.TextField(blank=True, null=True)),
                ('Verified', models.BooleanField(blank=True, null=True)),
                ('Instagram', models.CharField(blank=True, max_length=2048, null=True)),
                ('Facebook', models.CharField(blank=True, max_length=2048, null=True)),
                ('Twiter', models.CharField(blank=True, max_length=2048, null=True)),
                ('Youtube', models.CharField(blank=True, max_length=2048, null=True)),
                ('Created_date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='photos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('image_id', models.CharField(max_length=100, unique=True)),
                ('category', models.CharField(max_length=50)),
                ('Description', models.TextField()),
                ('Publish', models.BooleanField(default=0)),
                ('Tags', models.CharField(max_length=100)),
                ('views', models.IntegerField()),
                ('Date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('AddedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ctms.photographer')),
            ],
        ),
        migrations.CreateModel(
            name='categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('AddedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ctms.photographer')),
            ],
        ),
    ]