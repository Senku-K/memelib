from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Meme(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='memes/')
    upload_date = models.DateTimeField(default=timezone.now)
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='liked_memes', blank=True)
    downloads = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def increment_downloads(self):
        self.downloads += 1
        self.save()

    def get_likes_count(self):
        return self.likes.count() 