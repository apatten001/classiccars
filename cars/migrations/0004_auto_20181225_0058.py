# Generated by Django 2.1.4 on 2018-12-25 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_car_car_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_image',
            field=models.ImageField(default='car.jpg', null=True, upload_to='car_pics'),
        ),
    ]