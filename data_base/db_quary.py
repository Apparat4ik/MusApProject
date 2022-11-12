import sqlalchemy as sq
import os
from sqlalchemy.orm import sessionmaker
from moduls import *

base_name = 'some base name'
DSN = f'sqlite:///{base_name}'
engine = sq.create_engine(DSN)
create_tables(engine)
