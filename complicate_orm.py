from sqlalchemy.schema import ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import mapper
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class UserStatus(Base):
	__tablename__ = 'user_statuses'
	id = Column(Integer(), primary_key=True)
	name = Column(String(50), unique=True)

class User(Base):
	__tablename__ = 'users'
	id = Column(Integer(), primary_key=True)
	username = Column(String(50), unique=True)
	password = Column(String(50), nullable=False)
	status_id = Column(
		Integer(),
		ForeignKey('user_statuses.id'),
		nullable=False,
		default=1
	)

class Role(Base):
	__tablename__ = 'roles'
	id = Column(Integer(), primary_key=True)
	name = Column(String(50), unique=True)

class UserRole(Base):
	__tablename__ = 'users_roles'
	user_id = Column(Integer(), ForeignKey('users.id'), primary_key=True)
	role_id = Column(Integer(), ForeignKey('roles.id'), primary_key=True)

class Product(Base):
	__tablename__ = 'products'
	id = Column(Integer(), primary_key=True)
	name = Column(String(50), unique=True)

class Order(Base):
	__tablename__ = 'orders'
	id = Column(Integer(), primary_key=True)
	product_id = Column(Integer(), ForeignKey('products.id'))
	user_id = Column(Integer(), ForeignKey('users.id'))

engine = create_engine('postgresql+psycopg2://postgres:1@localhost/test_sa', echo=True)
Base.metadata.create_all(engine)