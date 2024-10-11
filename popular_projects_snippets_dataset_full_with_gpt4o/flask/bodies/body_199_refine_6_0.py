from datetime import date # pragma: no cover
import decimal # pragma: no cover
import uuid # pragma: no cover
import dataclasses # pragma: no cover

o = uuid.uuid4() # pragma: no cover
date = date # pragma: no cover
http_date = lambda x: x.isoformat() # pragma: no cover
decimal = decimal # pragma: no cover
uuid = uuid # pragma: no cover
dataclasses = dataclasses # pragma: no cover

from datetime import date # pragma: no cover
import decimal # pragma: no cover
import uuid # pragma: no cover
import dataclasses # pragma: no cover

o = date.today() # pragma: no cover
date = date # pragma: no cover
http_date = lambda x: x.isoformat() # pragma: no cover
decimal = decimal # pragma: no cover
uuid = uuid # pragma: no cover
dataclasses = type('MockDataclasses', (object,), {'is_dataclass': lambda obj: isinstance(obj, type) and hasattr(obj, '__dataclass_fields__'), 'asdict': lambda obj: {f.name: getattr(obj, f.name) for f in dataclasses.fields(obj)}}) # pragma: no cover
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
