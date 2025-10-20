from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tweet(models.Model):
    user = models.ForeignKey(User, related_name='tweets', on_delete=models.CASCADE)
    text = models.TextField(max_length=240)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='tweet_image/', null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.text}"
    
class Comment(models.Model):
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, related_name='comments', on_delete=models.CASCADE)
    comment = models.TextField(max_length=100)
    datetime_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment