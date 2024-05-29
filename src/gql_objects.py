from graphene import Field, List, Union
from graphene.relay import Node
from graphene_sqlalchemy import SQLAlchemyObjectType

from gql_errors import BingeError
from models import Booking as BookingModel
from models import Like as LikeModel
from models import Movie as MovieModel
from models import Review as ReviewModel
from models import User as UserModel


class Like(SQLAlchemyObjectType):
    class Meta:
        model = LikeModel

    user = Field(lambda: User)
    movie = Field(lambda: Movie)


class Review(SQLAlchemyObjectType):
    class Meta:
        model = ReviewModel
        interfaces = (Node,)

    user = Field(lambda: User)
    movie = Field(lambda: Movie)


class Booking(SQLAlchemyObjectType):
    class Meta:
        model = BookingModel

    user = Field(lambda: User)
    movie = Field(lambda: Movie)


class User(SQLAlchemyObjectType):
    class Meta:
        model = UserModel

    likes = List(Like)
    reviews = List(Review)
    bookings = List(Booking)


class Movie(SQLAlchemyObjectType):
    class Meta:
        model = MovieModel
        interfaces = (Node,)

    likes = List(Like)
    reviews = List(Review)
    bookings = List(Booking)


class UserPayload(Union):
    class Meta:
        types = (User, BingeError)


class MoviePayload(Union):
    class Meta:
        types = (Movie, BingeError)
