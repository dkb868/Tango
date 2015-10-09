from django.db import models

# Create your models here.

class Dish(models.Model):
	name = models.CharField(max_length=50)
	total_calories = models.IntegerField()
	fat_calories = models.IntegerField()
	total_fat = models.DecimalField(max_digits=10, decimal_places = 2) #g
	saturated_fat = models.DecimalField(max_digits=10,decimal_places = 2) #g
	trans_fat = models.DecimalField(max_digits=10, decimal_places = 2) #g
	cholesterol = models.DecimalField(max_digits=10, decimal_places = 2) #mg
	sodium = models.DecimalField(max_digits=10, decimal_places = 2) #mg
	total_carbohydrates = models.DecimalField(max_digits=10, decimal_places = 2) #g
	sugars = models.DecimalField(max_digits=10, decimal_places = 2) #g
	dietary_fiber = models.DecimalField(max_digits=10, decimal_places = 2) #g
	protein = models.DecimalField(max_digits=10, decimal_places = 2) #g
	vitamin_a = models.IntegerField() #%
	vitamin_c = models.IntegerField() #%
	calcium = models.IntegerField() #%
	iron = models.IntegerField() #%
	dining_hall = models.ForeignKey('Halls')
	
class Halls(models.Model):
	name = models.CharField(max_length=50)
	description = models.TextField()
	location = models.CharField(max_length=100)
	
