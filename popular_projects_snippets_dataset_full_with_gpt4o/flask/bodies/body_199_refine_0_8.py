import datetime # pragma: no cover
import decimal # pragma: no cover
import uuid # pragma: no cover
import dataclasses # pragma: no cover

o = datetime.date.today() # pragma: no cover
date = datetime.date # pragma: no cover
http_date = lambda x: x.isoformat() # pragma: no cover
decimal = decimal.Decimal(0) # pragma: no cover
uuid = uuid.UUID('12345678123456781234567812345678') # pragma: no cover
dataclasses = type('Mock', (object,), {'is_dataclass': lambda x: hasattr(x, '__dataclass_fields__'), 'asdict': lambda x: x.__dict__}) # pragma: no cover

import datetime # pragma: no cover
import decimal # pragma: no cover
import uuid # pragma: no cover
import dataclasses # pragma: no cover

o = datetime.date(2023, 10, 3) # pragma: no cover
date = datetime.date # pragma: no cover
http_date = lambda x: x.strftime('%a, %d %b %Y %H:%M:%S GMT') # pragma: no cover
o = decimal.Decimal('10.5') # pragma: no cover
decimal = decimal # pragma: no cover
o = uuid.UUID('12345678123456781234567812345678') # pragma: no cover
uuid = uuid # pragma: no cover
@dataclasses.dataclass # pragma: no cover
class DummyClass: # pragma: no cover
    field1: int # pragma: no cover
    field2: str # pragma: no cover
o = DummyClass(1, 'test') # pragma: no cover
dataclasses = dataclasses # pragma: no cover
class HtmlMock: # pragma: no cover
    def __html__(self): # pragma: no cover
        return '<html></html>' # pragma: no cover
o = HtmlMock() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/json/provider.py
from l3.Runtime import _l_
if isinstance(o, date):
    _l_(20131)

    aux = http_date(o)
    _l_(20130)
    exit(aux)

if isinstance(o, (decimal.Decimal, uuid.UUID)):
    _l_(20133)

    aux = str(o)
    _l_(20132)
    exit(aux)

if dataclasses and dataclasses.is_dataclass(o):
    _l_(20135)

    aux = dataclasses.asdict(o)
    _l_(20134)
    exit(aux)

if hasattr(o, "__html__"):
    _l_(20137)

    aux = str(o.__html__())
    _l_(20136)
    exit(aux)

raise TypeError(f"Object of type {type(o).__name__} is not JSON serializable")
_l_(20138)
