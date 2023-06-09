# Generated by Django 4.2.1 on 2023-05-09 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_aboutpageinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutChef',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='about_images', verbose_name='Chefs image')),
                ('name', models.CharField(max_length=100, verbose_name='About Chef')),
                ('prof', models.CharField(max_length=60, verbose_name='Chef prof')),
                ('link1', models.URLField(verbose_name='Chef link1')),
                ('link2', models.URLField(verbose_name='Chef link2')),
                ('link3', models.URLField(verbose_name='Chef link3')),
            ],
        ),
    ]
