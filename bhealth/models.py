from django.db import models

# Create your models here.

class Dish(models.Model):
	name = models.CharField()
	total_calories = models.IntegerField()
	fat_calories = models.IntegerField()
	total_fat = models.DecimalField() #g
	saturated_fat = models.DecimalField() #g
	trans_fat = models.DecimalField() #g
	cholesterol = models.DecimalField() #mg
	sodium = models.DecimalField() #mg
	total_carbohydrates = models.DecimalField() #g
	sugars = models.DecimalField() #g
	dietary_fiber = models.DecimalField() #g
	protein = models.DecimalField() #g
	vitamin_a = models.IntegerField() #%
	vitamin_c = models.IntegerField() #%
	calcium = models.IntegerField() #%
	iron = models.IntegerField() #%
	dining_hall = models.ForeignKey('Halls')
	
class Halls(models.Model):
	name = models.CharField()
	description = models.TextField()
	location = models.CharField()
	
