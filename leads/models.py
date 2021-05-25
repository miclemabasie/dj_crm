from django.db import models
from django.shortcuts import reverse
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_organiser = models.BooleanField(default=True)
    is_agent = models.BooleanField(default=False)
    


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    

class Lead(models.Model):
    first_name = models.CharField(max_length=200)
    last_name   = models.CharField(max_length=200)
    age         = models.IntegerField(default=0)
    agent       = models.ForeignKey('Agent', null=True, blank=True, on_delete=models.SET_NULL)
    organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    category = models.ForeignKey("Category", related_name='leads', null=True, blank=True, on_delete=models.SET_NULL)
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(null=True, blank=True)


    def __str__(self):
        return self.first_name


    def get_absolute_url(self):
        return reverse("leads:lead_detail", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse("leads:lead_update", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse("leads:lead_delete", kwargs={"pk": self.pk})
    
       
    


class Agent(models.Model):  
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to='agent-pics/')
    location = models.CharField(max_length=250, null=True, blank=True)
    phone = models.CharField(max_length=250, null=True, blank=True)
    
    
    def __str__(self):
        return self.user.username
    

class Category(models.Model):
    name = models.CharField(max_length=250)
    organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    