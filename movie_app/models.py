from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=50)


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField()
    director = models.ForeignKey(Director, related_name='movies', on_delete=models.CASCADE)


class Review(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(Movie, related_name='reviews', on_delete=models.CASCADE)
    stars = models.IntegerField()
