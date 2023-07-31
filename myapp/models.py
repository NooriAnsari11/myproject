from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Student(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=10, null=True)
    level=models.IntegerField()

class UserProgress(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    completed_chapters = models.IntegerField(default=0)
    course1_completed = models.BooleanField(default=False)
    course2_completed = models.BooleanField(default=False)
    course3_completed = models.BooleanField(default=False)
    course4_completed = models.BooleanField(default=False)
    course5_completed = models.BooleanField(default=False)
    course6_completed = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.user.username}'s Progress"
    

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    # Add any additional fields you might need for the user profile

    def __str__(self):
        return self.user.username
    
class Badge(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='badges/')

class UserBadge(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    badge = models.ForeignKey(Badge, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

