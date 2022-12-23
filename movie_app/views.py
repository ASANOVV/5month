from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import *
from rest_framework.response import Response


# Create your views here.

@api_view(['GET', 'POST'])
def director_view(request):
    if request.method == 'GET':
        directors = Director.objects.all()
        serializer = DirectorSerializer(directors, many=True)
        return Response(data=serializer.data)
    if request.method == 'POST':
        name = request.data.get('name', '')
        director = Director.objects.create(name=name)
        director.save()
        return Response(status=status.HTTP_201_CREATED,
                        data={
                            "message": "created successfully",
                            "director": DirectorSerializer(director).data
                        })


@api_view(['GET', 'PUT', 'DELETE'])
def director_detail_view(request, **kwargs):
    try:
        director = Director.objects.get(id=kwargs['id'])
    except Director.DoesNotExist:
        return Response(data={"error": "Director with that id does not exists"})
    if request.method == 'GET':
        data = DirectorSerializer(director, many=False).data
        return Response(data=data)
    if request.method == 'PUT':
        name = request.data.get('name', '')
        director.name = name
        director.save()
        return Response(
            data={"message": "director created successfully", "director": DirectorSerializer(director).data})
    if request.method == 'DELETE':
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def movie_view(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(data=serializer.data)

    if request.method == 'POST':
        title = request.data.get("title", "")
        description = request.data.get("description", "")
        duration = request.data.get("duration", 0)
        director_id = request.data.get("director_id", 1)
        movie = Movie.objects.create(title=title, description=description, duration=duration, director_id=director_id)
        movie.save()
        return Response(status=status.HTTP_201_CREATED,
                        data={"message": "movie created successfully", "movie": MovieSerializer(movie).data})


@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail_view(request, **kwargs):
    try:
        movie = Movie.objects.get(id=kwargs['id'])
    except Movie.DoesNotExist:
        return Response(data={"error": "movie does not exists"})
    if request.method == "GET":
        data = MovieSerializer(movie, many=False).data
        return Response(data=data)

    if request.method == 'PUT':
        title = request.data.get("title", movie.title)
        description = request.data.get("description", movie.description)
        duration = request.data.get("duration", movie.duration)
        director_id = request.data.get("director_id", movie.director_id)
        movie.title = title
        movie.description = description
        movie.duration = duration
        movie.director_id = director_id
        movie.save()

        return Response(data={"message": "movie updated successfully", "movie": MovieSerializer(movie).data})

    if request.method == 'DELETE':
        movie.delete()
        return Response(data={"message": "movie deleted successfully"})


@api_view(['GET', 'POST'])
def reviews_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        text = request.data.get("text", "empty")
        movie_id = request.data.get("movie_id", 1)
        stars = request.data.get("stars", 5)
        review = Review.objects.create(text=text, movie_id=movie_id, stars=stars)
        review.save()
        return Response(data={"message": "Created successfully", "review": ReviewSerializer(review).data})


@api_view(['GET', 'PUT', "DELETE"])
def review_detail_view(request, **kwargs):
    try:
        review = Review.objects.get(id=kwargs['id'])
    except Review.DoesNotExist:
        return Response(data={"error": "review does not exists"})
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(data=serializer.data)
    elif request.method == 'PUT':
        text = request.data.get("text", review.text)
        stars = request.data.get("stars", review.stars)
        movie_id = request.data.get("movie_id", review.movie_id)

        review.text = text
        review.stars = stars
        review.movie_id = movie_id
        review.save()
        return Response(data={"message": "updated"})
    elif request.method == "DELETE":
        review.delete()
        return Response(data={"message": "deleted"})


@api_view(['GET'])
def movie_review_view(request):
    movies = Movie.objects.all()
    serializer = MovieReviewSerializer(movies, many=True)
    return Response(data=serializer.data)
