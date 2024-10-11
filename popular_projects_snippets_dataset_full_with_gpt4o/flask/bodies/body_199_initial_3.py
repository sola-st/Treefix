from datetime import date # pragma: no cover
import decimal # pragma: no cover
import uuid # pragma: no cover
import dataclasses # pragma: no cover

o = date.today() # pragma: no cover
date = type(date) # pragma: no cover
http_date = lambda dt: dt.isoformat() # pragma: no cover
decimal.Decimal = decimal.Decimal(10) # pragma: no cover
uuid.UUID = uuid.uuid4() # pragma: no cover
dataclasses.is_dataclass = lambda obj: hasattr(obj, '__dataclass_fields__') # pragma: no cover
dataclasses.asdict = lambda obj: obj.__dict__ # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/json/provider.py
from l3.Runtime import _l_
if isinstance(o, date):
    _l_(20159)

    aux = http_date(o)
    _l_(20158)
    exit(aux)

if isinstance(o, (decimal.Decimal, uuid.UUID)):
    _l_(20161)

    aux = str(o)
    _l_(20160)
    exit(aux)

if dataclasses and dataclasses.is_dataclass(o):
    _l_(20163)

    aux = dataclasses.asdict(o)
    _l_(20162)
    exit(aux)

if hasattr(o, "__html__"):
    _l_(20165)

    aux = str(o.__html__())
    _l_(20164)
    exit(aux)

raise TypeError(f"Object of type {type(o).__name__} is not JSON serializable")
_l_(20166)
