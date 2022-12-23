from rest_framework import serializers
from .models import *


class DirectorSerializer(serializers.ModelSerializer):
    movies_count = serializers.SerializerMethodField()

    class Meta:
        model = Director
        fields = ['id', 'name', 'movies_count']

    def get_movies_count(self, director):
        return director.movies.count()


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class MovieReviewSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = "title duration description director reviews rating".split()

    def get_rating(self, movie):
        lst = [review.stars for review in movie.reviews.all()]
        return sum(lst) / len(lst)
