from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username

class Education(models.Model):  # Fixed class name
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    degree = models.CharField(max_length=100)
    institution = models.CharField(max_length=200)  # Fixed field name
    year = models.IntegerField()

    def __str__(self):
        return f"{self.degree} - {self.institution}"