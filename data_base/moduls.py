import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()

class Category(Base):
    """
    There will be a book's category table
    """

    __tablename__ = 'category'
    id = sq.Column(sq.Integer, primary_key=True, unique=True, autoincrement=True)
    title = sq.Column(sq.String, nullable=False)

class M_Mus_Company(Base):
    """
    There wiil be a book's main music company table
    """
    __tablename__ = 'm_mus_company'
    id = sq.Column(sq.Integer, primary_key=True, unique=True, autoincrement=True)
    name = sq.Column(sq.String, nullable=False)
    country = sq.Column(sq.Integer, sq.ForeignKey('country.id'), nullable=False)

class MusCompany_Category(Base):
    """
    THere will be a relationship category
    """
    __tablename__ = 'mus_company_category'
    id = sq.Column(sq.Integer, primary_key=True, unique=True, autoincrement=True)
    id_category = sq.Column(sq.Integer, sq.ForeignKey('category.id'), nullable=False)
    id_mus_company = relationship(M_Mus_Company, backref='mus_company_category')

class Country(Base):
    """
    There will be a country class
    """
    __tablename__ = 'country'
    id = sq.Column(sq.Integer, primary_key=True, unique=True, autoincrement=True)
    name = sq.Column(sq.String, nullable=False)

class Country_MusCompany(Base):
    """

    """
    __tablename__ = 'country_mus_company'
    id = sq.Column(sq.Integer, primary_key=True, unique=True, autoincrement=True)
    id_mus_company = sq.Column(sq.Integer, sq.ForeignKey('m_mus_company.id'), nullable=False)
    id_country = relationship(Country, backref='country_mus_company')

class Instruments(Base):
    """
    There will be a book table
    """
    __tablename__ = 'instruments'
    id = sq.Column(sq.Integer, primary_key=True, unique=True, autoincrement=True)
    title = sq.Column(sq.String, nullable=False)
    category = sq.Column(sq.Integer, sq.ForeignKey('category.id'), nullable=False)
    main_mus_company = sq.Column(sq.Integer, sq.ForeignKey('m_mus_company.id'), nullable=False)
    f_mus_company = sq.Column(sq.Integer, sq.ForeignKey('f_mus_company.id'), nullable=True)

class F_Mus_Company(Base):
    """
    There will be a filial music company class
    """

    __tablename__ = 'f_mus_company'
    id = sq.Column(sq.Integer, primary_key=True, unique=True, autoincrement=True)
    title = sq.Column(sq.String, nullable=False)


def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)