# Uncomment the following imports before adding the Model code

# from django.db import models
# from django.utils.timezone import now
# from django.core.validators import MaxValueValidator, MinValueValidator

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Car Make model
class CarMake(models.Model):
    name = models.CharField(max_length=100)  # Name of the car make (e.g., Toyota, Ford, etc.)
    description = models.TextField()  # Description about the car make (e.g., a brief history or details)

    def __str__(self):
        return self.name  # String representation to return the name of the car make


# Car Model model
class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)  # Many-to-One relationship with CarMake
    name = models.CharField(max_length=100)  # Name of the car model (e.g., Camry, Focus, etc.)
    
    # Define choices for car type
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        # Add more choices as required
    ]
    type = models.CharField(max_length=10, choices=CAR_TYPES, default='SUV')  # Type of car (Sedan, SUV, Wagon)
    
    # Year of manufacture with validation for the year range
    year = models.IntegerField(
        default=2023,
        validators=[
            MaxValueValidator(2023),  # Maximum year 2023
            MinValueValidator(2015)   # Minimum year 2015
        ]
    )
    
    dealer_id = models.IntegerField()  # Dealer ID referring to a dealer in Cloudant or another database

    def __str__(self):
        return f"{self.car_make.name} {self.name}"  # String representation to return Car Make and Car Model


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many
# Car Models, using ForeignKey field)
# - Name
# - Type (CharField with a choices argument to provide limited choices
# such as Sedan, SUV, WAGON, etc.)
# - Year (IntegerField) with min value 2015 and max value 2023
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object
