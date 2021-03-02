from django.db import models

# Create your models here.


class Magic(models.Model):
    title = models.CharField(max_length=100)
    source = models.CharField(max_length=200)
    props = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=100)
    video_url = models.TextField()
    owner = models.CharField(max_length=100)

    # def __str__(self):
    #     return self.title
