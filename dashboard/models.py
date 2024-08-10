from django.db import models

class UserProfile(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    occupation = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    user_no = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name