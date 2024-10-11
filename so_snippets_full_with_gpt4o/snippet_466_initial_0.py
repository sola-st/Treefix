from sqlalchemy import create_engine, Column, Integer, String # pragma: no cover
from sqlalchemy.ext.declarative import declarative_base # pragma: no cover
from sqlalchemy.orm import sessionmaker # pragma: no cover

engine = create_engine('sqlite:///:memory:') # pragma: no cover
Base = declarative_base() # pragma: no cover
class ClientTotal(Base):# pragma: no cover
    __tablename__ = 'client_totals'# pragma: no cover
    id = Column(Integer, primary_key=True)# pragma: no cover
    client = Column(String, nullable=False) # pragma: no cover
Base.metadata.create_all(engine) # pragma: no cover
Session = sessionmaker(bind=engine) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/4186062/sqlalchemy-order-by-descending
from l3.Runtime import _l_
session = Session()
_l_(14976)
auth_client_name = 'client3' 
_l_(14977) 
result_by_auth_client = session.query(ClientTotal).filter(ClientTotal.client ==
auth_client_name).order_by(ClientTotal.id.desc()).all()
_l_(14978)

for rbac in result_by_auth_client:
    _l_(14980)

    print(rbac.id) 
    _l_(14979) 
session.close()
_l_(14981)

