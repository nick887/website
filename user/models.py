from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    male=models.BooleanField(default=False)
    website=models.URLField(null=True)

    def __str__(self):
        return self.user.username

class Diary(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    note=models.TextField()
    ddate=models.DateField()

    def __str__(self):
        return "{}:{}".format(self.ddate,self.user)