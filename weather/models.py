from django.db import models

# Create your models here.

class City(models.Model):
    
    CITY_CHOICES = (
    ('London','London'),
    ('Hong Kong', 'Hong Kong'),
    ('New York','New York'),
    ('Paris','Paris'),
    ('Toronto','Toronto'),
    )

    name = models.CharField(max_length=25, choices=CITY_CHOICES, default='green')

    def __str__(self): #show the actual city name on the dashboard
        return self.name
    
    class Meta: #show the plural of city as cities instead of citys
        verbose_name_plural = 'cities'