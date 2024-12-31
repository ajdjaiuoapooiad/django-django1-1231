
from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    text=models.TextField(max_length=300)
    date=models.DateTimeField(auto_now_add=True)
    like=models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.text