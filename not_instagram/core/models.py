from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=50, default=None, null=True)
    picture = models.ImageField(upload_to='profile/', default=None, null=True)

class Publication(models.Model):
    content = models.ImageField(upload_to='photos/')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    caption = models.CharField(max_length=100, null=True, blank=True)
    published_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    content = models.CharField(max_length=500)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

