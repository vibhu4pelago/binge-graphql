from graphene import ObjectType, Field, List
from graphene_sqlalchemy import SQLAlchemyObjectType

from models import (
    User as UserModel,
    Movie as MovieModel,
    Like as LikeModel,
    Review as ReviewModel,
    Booking as BookingModel,
)


class Like(SQLAlchemyObjectType):
    class Meta:
        model = LikeModel
        fields = ("user", "movie")

    user = Field(lambda: User)
    movie = Field(lambda: Movie)


class Review(SQLAlchemyObjectType):
    class Meta:
        model = ReviewModel
        fields = ("id", "user", "movie", "rating", "text")

    user = Field(lambda: User)
    movie = Field(lambda: Movie)


class Booking(SQLAlchemyObjectType):
    class Meta:
        model = BookingModel
        fields = ("id", "user", "movie", "time")

    user = Field(lambda: User)
    movie = Field(lambda: Movie)


class User(SQLAlchemyObjectType):
    class Meta:
        model = UserModel
        fields = (
            "id",
            "name",
            "email",
            "likes",
            "reviews",
            "bookings",
        )

    likes = List(Like)
    reviews = List(Review)
    bookings = List(Booking)


class Movie(SQLAlchemyObjectType):
    class Meta:
        model = MovieModel
        fields = (
            "id",
            "name",
            "genre",
            "likes",
            "reviews",
            "bookings",
        )

    likes = List(Like)
    reviews = List(Review)
    bookings = List(Booking)
