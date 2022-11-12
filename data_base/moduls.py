import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()

class Genre(Base):
    """
    There will be a book's genre table
    """

    __tablename__ = 'genre'
    id = sq.Column(sq.Integer, primary_key=True, unique=True, autoincrement=True)
    title = sq.Column(sq.String, nullable=False)

class Author(Base):
    """
    There wiil be a book's author table
    """
    __tablename__ = 'author'
    id = sq.Column(sq.Integer, primary_key=True, unique=True, autoincrement=True)
    name = sq.Column(sq.String, nullable=False)
    surname = sq.Column(sq.String, nullable=False)
    nickname = sq.Column(sq.String, nullable=False)

class AuthorBook(Base):
    """

    """
    __tablename__ = 'author_book'
    id = sq.Column(sq.Integer, primary_key=True, unique=True, autoincrement=True)
    id_book = sq.Column(sq.Integer, sq.ForeignKey('book.id'), nullable=False)
    id_author = relationship(Author, backref='author_book')

class Book(Base):
    """
    There will be a book table
    """
    __tablename__ = 'book'
    id = sq.Column(sq.Integer, primary_key=True, unique=True, autoincrement=True)
    title = sq.Column(sq.String, nullable=False)
    date = sq.Column(sq.Integer, nullable=True)
    rating = sq.Column(sq.String, nullable=True)
    pages = sq.Column(sq.Integer, sq.ForeignKey('country.id'),  nullable=True)
    publisher = sq.Column(sq.Integer, sq.ForeignKey('publisher.id'), nullable=True)

class Publisher(Base):
    """
    There will be a publisher class
    """

    __tablename__ = 'publisher'
    id = sq.Column(sq.Integer, primary_key=True, unique=True, autoincrement=True)
    title = sq.Column(sq.String, nullable=False)
    country = sq.Column(sq.Integer, nullable=True)

class Country(Base):
    """
    There will be a country class
    """
    __tablename__ = 'country'
    id = sq.Column(sq.Integer, primary_key=True, unique=True, autoincrement=True)
    name = sq.Column(sq.String, nullable=False)

def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)