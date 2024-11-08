from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    reg_number = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50)
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.TextField()
    resident_base = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    reference_name = models.CharField(max_length=100)
    reference_number = models.CharField(max_length=15)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)

    def __str__(self):
        return self.user.username
    
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    posted_date = models.DateTimeField(auto_now_add=True)
    company_name = models.CharField(max_length=100)
    apply_link = models.URLField()

    def __str__(self):
        return self.title

