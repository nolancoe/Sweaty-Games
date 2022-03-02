from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Season(models.Model):
    gametype = models.CharField(max_length=15)

    def __str__(self):
        return str(self.gametype)

class user_profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    gamertag = models.CharField(max_length=15)
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return str(self.gamertag)

class Team(models.Model):
    teamname = models.CharField(max_length=30)
    gametype = models.ForeignKey(Season, on_delete=models.CASCADE, blank=True, null=True)
    leader = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.teamname)

class Match(models.Model):
    gametype = models.ForeignKey(Season, on_delete=models.CASCADE, blank=True, null=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return str(self.gametype) + ' | ' + str(self.creator)

    def get_absolute_url(self):
        return reverse('matches')


