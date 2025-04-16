from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    GENDER_CHOICES = (
       ('Male', 'Male'),
       ('Female', 'Female'),
       ('Other', 'Other')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True, blank=True)
    birth_date = models.DateField()
    
    def __str__(self):
        return self.user.username