from datetime import date # pragma: no cover
from datetime import datetime # pragma: no cover
import decimal # pragma: no cover
import uuid # pragma: no cover
import dataclasses # pragma: no cover

o = 'example' # pragma: no cover
date = datetime.today().date() # pragma: no cover
def http_date(d): return d.isoformat() # pragma: no cover
decimal.Decimal = type('Decimal', (object,), {'__str__': lambda s: '0.1'})() # pragma: no cover
uuid.UUID = type('UUID', (object,), {'__str__': lambda s: '12345678-1234-5678-1234-567812345678'})() # pragma: no cover
dataclasses = type('dataclasses', (object,), {'is_dataclass': lambda obj: True, 'asdict': lambda obj: {'mock': 'data'}}) # pragma: no cover

from datetime import date # pragma: no cover
from wsgiref.handlers import format_date_time # pragma: no cover
import decimal # pragma: no cover
import uuid # pragma: no cover
import dataclasses # pragma: no cover

o = date(2023, 10, 1) # pragma: no cover
http_date = lambda d: format_date_time(d.timestamp()) # pragma: no cover
decimal = type('MockDecimal', (decimal.Decimal,), {}) # pragma: no cover
uuid = type('MockUUID', (uuid.UUID,), {}) # pragma: no cover
dataclasses = type('MockDataClasses', (object,), {'is_dataclass': staticmethod(lambda x: False), 'asdict': staticmethod(lambda x: {'key': 'value'})}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/json/provider.py
from l3.Runtime import _l_
if isinstance(o, date):
    _l_(8990)

    aux = http_date(o)
    _l_(8989)
    exit(aux)

if isinstance(o, (decimal.Decimal, uuid.UUID)):
    _l_(8992)

    aux = str(o)
    _l_(8991)
    exit(aux)

if dataclasses and dataclasses.is_dataclass(o):
    _l_(8994)

    aux = dataclasses.asdict(o)
    _l_(8993)
    exit(aux)

if hasattr(o, "__html__"):
    _l_(8996)

    aux = str(o.__html__())
    _l_(8995)
    exit(aux)

raise TypeError(f"Object of type {type(o).__name__} is not JSON serializable")
_l_(8997)
