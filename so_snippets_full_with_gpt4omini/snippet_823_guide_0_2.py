from sqlalchemy import create_engine, Column, Integer, String, and_, or_ # pragma: no cover
from sqlalchemy.ext.declarative import declarative_base # pragma: no cover
from sqlalchemy.orm import sessionmaker # pragma: no cover

Base = declarative_base() # pragma: no cover
class User(Base): # pragma: no cover
    __tablename__ = 'users' # pragma: no cover
    id = Column(Integer, primary_key=True) # pragma: no cover
    name = Column(String) # pragma: no cover
    surname = Column(String) # pragma: no cover
    country = Column(String) # pragma: no cover
engine = create_engine('sqlite:///:memory:') # pragma: no cover
Base.metadata.create_all(engine) # pragma: no cover
Session = sessionmaker(bind=engine) # pragma: no cover
session = Session() # pragma: no cover
session.add(User(name='Joe', surname='Dodson', country='USA')) # pragma: no cover
session.add(User(name='Ryan', surname='Smith', country='England')) # pragma: no cover
session.commit() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/2128505/difference-between-filter-and-filter-by-in-sqlalchemy
from l3.Runtime import _l_
def filter_by(self, **kwargs):
    _l_(2924)

    aux = self.filter(sql.and_(**kwargs))
    _l_(2923)
    return aux

session.query(db.users).filter_by(name='Joe', surname='Dodson')
_l_(2925)

session.query(db.users).filter(or_(db.users.name=='Ryan', db.users.country=='England'))
_l_(2926)

session.query(db.users).filter((db.users.name=='Ryan') | (db.users.country=='England'))
_l_(2927)

Users.query.get(123)
_l_(2928)
# And even by a composite PK
Users.query.get(123, 321)
_l_(2929)

