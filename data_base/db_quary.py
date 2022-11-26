import sqlalchemy as sq
import os
from sqlalchemy.orm import sessionmaker
from moduls import *

def add_category(session, list_category: tuple) -> bool:
    """
    тут информация о функции add_genre
    """
    try:
        for category in list_category:
            add_ = Category(title=category)
            session.add(add_)
        session.commit()
        return True
    except:
        return False


def add_country(session, list_country: tuple) -> bool:
    """
    информация о функции
    """
    try:
        for country in list_country:
            add_ = Country(name=country)
            session.add(add_)
        session.commit()
        return True
    except:
        return False

def add_M_Mus_Company(session, list_main_mus_company: tuple) -> bool:
    """
       информация о функции
       """
    try:
        for m_mus_comp in list_main_mus_company:
            add_ = Country(name=m_mus_comp)
            session.add(add_)
        session.commit()
        return True
    except:
        return False

base_name = 'music_db'
DSN = f'sqlite:///{base_name}'
engine = sq.create_engine(DSN)
create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()
list_country = ('Россия', 'США', 'Япония', 'Англия', 'Германия', 'Индонезия', 'Китай')
list_category = ('клавишные', 'струнно-смычковые', 'струнно-щипковые', 'духовые', 'ударные', 'электронные')
list_main_mus_company = ('Fender', 'Gibson', 'Yamaha')

add_category(session, list_category)
add_country(session, list_country)
session.close()
