from datetime import date # pragma: no cover
import decimal # pragma: no cover
import uuid # pragma: no cover
import dataclasses # pragma: no cover

o = date.today() # pragma: no cover
http_date = lambda x: x.isoformat() # pragma: no cover
decimal.Decimal = decimal.Decimal('3.14') # pragma: no cover
uuid.UUID = uuid.uuid4() # pragma: no cover
dataclasses.is_dataclass = lambda x: isinstance(x, type) and hasattr(x, '__dataclass_fields__') # pragma: no cover
dataclasses.asdict = lambda x: {f.name: getattr(x, f.name) for f in dataclasses.fields(x)} # pragma: no cover
o = type('Mock', (object,), {'__html__': lambda self: '<p>HTML</p>'})() # pragma: no cover

from datetime import date # pragma: no cover
import decimal # pragma: no cover
import uuid # pragma: no cover
import dataclasses # pragma: no cover

o = date.today() # pragma: no cover
http_date = lambda x: x.isoformat() # pragma: no cover
decimal.Decimal = decimal.Decimal # pragma: no cover
uuid.UUID = uuid.UUID # pragma: no cover
dataclasses.is_dataclass = dataclasses.is_dataclass # pragma: no cover
dataclasses.asdict = dataclasses.asdict # pragma: no cover
o = type('Mock', (object,), {'__html__': lambda self: '<html></html>'})() # pragma: no cover

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
