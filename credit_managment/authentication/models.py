from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime

class CustomUser(AbstractUser):
    class Gender(models.TextChoices):
        MALE = 'MALE', 'Male'
        FEMALE = 'FEMALE', 'Female'
    
    class Civility(models.TextChoices):
        MARRIED = 'MARRIED', 'Married'  # Fixed spelling
        UNMARRIED = 'UNMARRIED', 'Unmarried'  # Fixed spelling

    PROVINCES = [
        ('Kayanza', 'Kayanza'),
        ('Mwaro', 'Mwaro'),
        ('Bururi', 'Bururi'),
        ('Bujumbura-Mairie', 'Bujumbura-Mairie'),
        ('Bujumbura-Rurale', 'Bujumbura-Rurale'),
        ('Gitega', 'Gitega'),
        ('Rutana', 'Rutana'),
        ('Ngozi', 'Ngozi'),
        ('Cibitoke', 'Cibitoke'),
        ('Muyinga', 'Muyinga'),
        ('Kirundo', 'Kirundo'),
        ('Rumonge', 'Rumonge'),
        ('Makamba', 'Makamba'),
        ('Karusi', 'Karusi'),
        ('Ruyigi', 'Ruyigi'),
        ('Bubanza', 'Bubanza'),
    ]

    gender = models.CharField(
        max_length=10,
        verbose_name='Gender',
        choices=Gender.choices  # Use .choices here
    )
    
    civility = models.CharField(
        max_length=30,
        verbose_name='Civility',
        choices=Civility.choices  # Use .choices here
    )
    
    province = models.CharField(
        max_length=30,
        verbose_name='Province',
        choices=PROVINCES
    )
    
    birth_year = models.PositiveIntegerField(
        verbose_name='Birth Year',
        choices=[(year, year) for year in range(1900, datetime.now().year + 1)],
        default=datetime.now().year
    )
    
    profile_photo = models.ImageField(verbose_name='Profile Photo')  # Specify upload_to

    def __str__(self):
        return self.username
