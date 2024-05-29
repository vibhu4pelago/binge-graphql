from graphene import (
    ID,
    DateTime,
    Field,
    Int,
    List,
    Mutation,
    ObjectType,
    Schema,
    String,
)
from graphene_sqlalchemy import SQLAlchemyConnectionField

import gql_objects
from constants import ErrorCodes
from gql_errors import BingeError
from models import Booking, Like, Movie, Review, User, db_session


class Query(ObjectType):
    user = Field(gql_objects.UserPayload, id=ID(required=True))
    movie = Field(gql_objects.MoviePayload, id=ID(required=True))
    movies = SQLAlchemyConnectionField(gql_objects.Movie.connection)
    reviews = SQLAlchemyConnectionField(gql_objects.Review.connection)
    bookings = List(gql_objects.Booking, user_id=ID(required=True))

    def resolve_user(parent, info, id):
        user = User.query.get(id)
        if user is not None:
            return user
        return BingeError(code=ErrorCodes.NotFound, error_message="User not found")

    def resolve_movie(parent, info, id):
        movie = Movie.query.get(id)
        if movie is not None:
            return movie
        return BingeError(code=ErrorCodes.NotFound, error_message="Movie not found")

    def resolve_bookings(parent, info, user_id):
        return Booking.query.filter_by(user_id=user_id).all()


class CreateUser(Mutation):
    class Arguments:
        name = String(required=True)
        email = String(required=True)

    Output = gql_objects.User

    def mutate(root, info, name, email):
        user = User(name=name, email=email)
        db_session.add(user)
        db_session.commit()
        return user


class CreateMovie(Mutation):
    class Arguments:
        name = String(required=True)
        genre = String(required=True)

    Output = gql_objects.Movie

    def mutate(root, info, name, genre):
        movie = Movie(name=name, genre=genre)
        db_session.add(movie)
        db_session.commit()
        return movie


class CreateLike(Mutation):
    class Arguments:
        user_id = ID(required=True)
        movie_id = ID(required=True)

    Output = gql_objects.Like

    def mutate(root, info, user_id, movie_id):
        like = Like(user_id=user_id, movie_id=movie_id)
        db_session.add(like)
        db_session.commit()
        return like


class CreateReview(Mutation):
    class Arguments:
        user_id = ID(required=True)
        movie_id = ID(required=True)
        rating = Int(required=True)
        text = String()

    Output = gql_objects.Review

    def mutate(root, info, user_id, movie_id, rating, text):
        review = Review(user_id=user_id, movie_id=movie_id, rating=rating, text=text)
        db_session.add(review)
        db_session.commit()
        return review


class CreateBooking(Mutation):
    class Arguments:
        user_id = ID(required=True)
        movie_id = ID(required=True)
        time = DateTime(required=True)

    Output = gql_objects.Booking

    def mutate(root, info, user_id, movie_id, time):
        booking = Booking(user_id=user_id, movie_id=movie_id, time=time)
        db_session.add(booking)
        db_session.commit()
        return booking


class Mutation(ObjectType):
    create_user = CreateUser.Field()
    create_movie = CreateMovie.Field()
    create_like = CreateLike.Field()
    create_review = CreateReview.Field()
    create_booking = CreateBooking.Field()


schema = Schema(query=Query, mutation=Mutation)
