from sqlalchemy import (
    Column,
    Integer,
    String,
    Enum,
    DateTime,
    ForeignKey,
    create_engine,
    MetaData,
)
from sqlalchemy.orm import relationship, scoped_session, sessionmaker

from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///database.sqlite3", convert_unicode=True)
db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)

metadata = MetaData()
Base = declarative_base()
Base.metadata = metadata
Base.query = db_session.query_property()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)


class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    # genre = Column(Enum("Horror", "Thriller", "Comedy", "Action"))
    genre = Column(String)


class Like(Base):
    __tablename__ = "likes"

    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    user = relationship("User", backref="likes")

    movie_id = Column(Integer, ForeignKey("movies.id"), primary_key=True)
    movie = relationship("Movie", backref="likes")


def rating_check(rating):
    if not 1 <= rating <= 10:
        raise ValueError("Rating must be between 1 and 10")


class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", backref="reviews")

    movie_id = Column(Integer, ForeignKey("movies.id"))
    movie = relationship("Movie", backref="reviews")

    # rating = Column(Integer, checkarg=rating_check)
    rating = Column(Integer)
    text = Column(String)


class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", backref="bookings")

    movie_id = Column(Integer, ForeignKey("movies.id"))
    movie = relationship("Movie", backref="bookings")

    time = Column(DateTime, nullable=False)


metadata.create_all(engine)
