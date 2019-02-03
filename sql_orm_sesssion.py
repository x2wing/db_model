from create_db import *
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()
# wiki_user = User("ivan", "Ivan Ivanov", "qwerty123")
# print(wiki_user)
# session.add(wiki_user)
# session.add_all([User("kolia", "Cool Kolian[S.A.]","kolia$$$"),
#                  User("zina", "Zina Korzina", "zk18")])

# wiki_user = User("kek", "Ivan Ivanov", "qwerty123")
# session.add(wiki_user)
# print(session.query(User).filter_by(name='kek').all())
# session.rollback()
# print(session.query(User).filter_by(name='kek').all())

for user in session.query(User).order_by(User.id):
    print (user.name, user.fullname)