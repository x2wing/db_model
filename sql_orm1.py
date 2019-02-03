from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, Sequence
from sqlalchemy.orm import mapper

engine = create_engine('postgresql+psycopg2://postgres:1@localhost/test_sa', echo=True)


metadata = MetaData()
users_table = Table('wiki_users', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)), # Для некоторых БД не нужно указывать размер полей VARCHAR. Для mysql - обязательно.
    Column('fullname', String(50)),
    Column('password', String(50))
)
metadata.create_all(engine)


class User(object):
    def __init__(self, name, fullname, password):
        self.name = name
        self.fullname = fullname
        self.password = password

    def __repr__(self):
        return "<User('%s','%s', '%s')>" % (self.name, self.fullname, self.password)

print (mapper(User, users_table))