from django.db import models
from django.conf import settings

# Create your models here.
class Post(models.Model):
    content = models.CharField(max_length=140)
    image = models.ImageField(blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # User와의 M:N Like
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_posts', blank=True)
    
    def __str__(self):
        return self.content
        
class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    
    def __str__(self):
        return self.content