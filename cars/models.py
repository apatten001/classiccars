from django.db import models

# Create your models here.


MAKE_CHOICES = (('Ford', 'Ford'), ('Lincoln', 'Lincoln'),
                ('Chrysler', 'Chrysler'), ('Chevy', 'Chevy'), ('Cadillac', 'Cadillac'))


class Car(models.Model):
    car_year = models.IntegerField()
    car_name = models.CharField(max_length=120, blank=False)
    car_make = models.CharField(max_length=120, blank=False, choices=MAKE_CHOICES)
    car_image = models.ImageField(default='car.jpg', null=True, upload_to='car_pics')

    def __str__(self):
        return str(self.car_year) + ' ' + self.car_make + ' ' + self.car_name






