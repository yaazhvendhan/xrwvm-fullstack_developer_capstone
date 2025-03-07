# Uncomment the following imports before adding the Model code
from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime

# Car Make Model
class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.name

# Car Model
class CarModel(models.Model):
    SEDAN = 'Sedan'
    SUV = 'SUV'
    HATCHBACK = 'Hatchback'
    CONVERTIBLE = 'Convertible'
    TRUCK = 'Truck'
    
    CAR_TYPE_CHOICES = [
        (SEDAN, 'Sedan'),
        (SUV, 'SUV'),
        (HATCHBACK, 'Hatchback'),
        (CONVERTIBLE, 'Convertible'),
        (TRUCK, 'Truck'),
    ]
    
    name = models.CharField(max_length=100)
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    car_type = models.CharField(max_length=20, choices=CAR_TYPE_CHOICES)
    year = models.IntegerField()

    def __str__(self):
        return f"{self.car_make.name} {self.name} ({self.year})"



#from django.db import models
#from django.core.validators import MaxValueValidator, MinValueValidator
#import datetime

class CarModel(models.Model):
    # Many-to-one relationship with CarMake
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    
    # Dealer ID referring to a dealer in the Cloudant database
    dealer_id = models.IntegerField()
    
    # Car model name
    name = models.CharField(max_length=100)

    # Car Type Choices
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('TRUCK', 'Truck'),
        ('COUPE', 'Coupe'),
    ]
    type = models.CharField(max_length=10, choices=CAR_TYPES, default='SUV')

    # Manufacturing Year (Ensuring it's within a valid range)
    current_year = datetime.datetime.now().year
    year = models.IntegerField(
        validators=[MinValueValidator(2015), MaxValueValidator(current_year)]
    )

    def __str__(self):
        return f"{self.car_make.name} {self.name} ({self.year})"

