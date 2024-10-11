from sqlalchemy import create_engine, Column, Integer, String, and_, or_ # pragma: no cover
from sqlalchemy.ext.declarative import declarative_base # pragma: no cover
from sqlalchemy.orm import sessionmaker # pragma: no cover
import sqlalchemy as sql # pragma: no cover

Base = declarative_base() # pragma: no cover
engine = create_engine('sqlite:///:memory:') # pragma: no cover
Session = sessionmaker(bind=engine) # pragma: no cover
session = Session() # pragma: no cover
 # pragma: no cover
class User(Base): # pragma: no cover
    __tablename__ = 'users' # pragma: no cover
    id = Column(Integer, primary_key=True) # pragma: no cover
    id_secondary = Column(Integer, primary_key=True, autoincrement=False) # pragma: no cover
    name = Column(String) # pragma: no cover
    surname = Column(String) # pragma: no cover
    country = Column(String) # pragma: no cover
 # pragma: no cover
Base.metadata.create_all(engine) # pragma: no cover
 # pragma: no cover
session.add_all([ # pragma: no cover
    User(id=123, id_secondary=321, name='Joe', surname='Dodson', country='USA'), # pragma: no cover
    User(id=124, id_secondary=322, name='Ryan', surname='Smith', country='England') # pragma: no cover
]) # pragma: no cover
session.commit() # pragma: no cover
 # pragma: no cover
db = type('Mock', (object,), {'users': User}) # pragma: no cover
 # pragma: no cover
class Users: # pragma: no cover
    @staticmethod # pragma: no cover
    def get(*args): # pragma: no cover
        if len(args) == 1: # pragma: no cover
            return session.query(User).get(args[0]) # pragma: no cover
        elif len(args) == 2: # pragma: no cover
            return session.query(User).filter_by(id=args[0], id_secondary=args[1]).first() # pragma: no cover
 # pragma: no cover
def filter_by(self, **kwargs): # pragma: no cover
    aux = self.filter(and_(*[getattr(self.entity, k) == v for k, v in kwargs.items()])) # pragma: no cover
    return aux # pragma: no cover
setattr(session.query(User).__class__, 'filter_by', filter_by) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/2128505/difference-between-filter-and-filter-by-in-sqlalchemy
from l3.Runtime import _l_
def filter_by(self, **kwargs):
    _l_(14653)

    aux = self.filter(sql.and_(**kwargs))
    _l_(14652)
    return aux

session.query(db.users).filter_by(name='Joe', surname='Dodson')
_l_(14654)

session.query(db.users).filter(or_(db.users.name=='Ryan', db.users.country=='England'))
_l_(14655)

session.query(db.users).filter((db.users.name=='Ryan') | (db.users.country=='England'))
_l_(14656)

Users.query.get(123)
_l_(14657)
# And even by a composite PK
Users.query.get(123, 321)
_l_(14658)

