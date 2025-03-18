from django.db import models
from django.core.validators import RegexValidator


class User(models.Model):
    GENDER_CHOICES =[('Male','Male'),
                     ('Female', 'Female'),
                     ('Other', 'Other'),]
    
    name = models.CharField(max_length=100)
    email = models.EmailField(unique =True)
    phone =  models.CharField(
        max_length=10,  # Restrict to 10 digits
        validators=[RegexValidator(r'^\d{10}$', message="Phone number must be exactly 10 digits.")],
    )
    age = models.PositiveBigIntegerField()
    gender = models.CharField(max_length=10 , choices= GENDER_CHOICES)
    address = models.TextField()


    def __str__(self):
        return self.name
