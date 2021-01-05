from django.db import models

# Create your models here.
class OTT(models.Model):
    def __str__(self):
        return self.title
    id = models.IntegerField(primary_key=True)
    title = models.CharField(default="",max_length=120)
    year = models.IntegerField(default=0)
    age = models.IntegerField(default=0, null=True, blank=True)
    imdb = models.FloatField(default=0, null=True, blank=True)
    rotten_tomatoes = models.FloatField(default=0, null=True, blank=True)
    netflix = models.BooleanField(default=False)
    hulu = models.BooleanField(default=False)
    primevideo = models.BooleanField(default=False)
    disneyplus = models.BooleanField(default=False)
    directors = models.CharField(default="",max_length=500, null=True, blank=True)
    genres = models.CharField(default="",max_length=100, null=True, blank=True)
    country = models.CharField(default="",max_length=300, null=True, blank=True)
    language = models.CharField(default="",max_length=100, null=True, blank=True)
    runtime = models.FloatField(default=0, null=True, blank=True)
