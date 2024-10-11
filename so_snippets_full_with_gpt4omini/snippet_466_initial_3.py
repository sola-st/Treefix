from sqlalchemy import create_engine, Column, Integer, String, ForeignKey # pragma: no cover
from sqlalchemy.ext.declarative import declarative_base # pragma: no cover
from sqlalchemy.orm import sessionmaker # pragma: no cover

Base = declarative_base() # pragma: no cover
class ClientTotal(Base): # pragma: no cover
    __tablename__ = 'client_total' # pragma: no cover
    id = Column(Integer, primary_key=True) # pragma: no cover
    client = Column(String) # pragma: no cover
engine = create_engine('sqlite:///:memory:') # pragma: no cover
Base.metadata.create_all(engine) # pragma: no cover
Session = sessionmaker(bind=engine)() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/4186062/sqlalchemy-order-by-descending
from l3.Runtime import _l_
session = Session()
_l_(2459)
auth_client_name = 'client3' 
_l_(2460) 
result_by_auth_client = session.query(ClientTotal).filter(ClientTotal.client ==
auth_client_name).order_by(ClientTotal.id.desc()).all()
_l_(2461)

for rbac in result_by_auth_client:
    _l_(2463)

    print(rbac.id) 
    _l_(2462) 
session.close()
_l_(2464)

