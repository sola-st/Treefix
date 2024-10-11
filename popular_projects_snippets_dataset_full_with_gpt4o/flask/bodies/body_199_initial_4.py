from datetime import date, datetime # pragma: no cover
import decimal # pragma: no cover
import uuid # pragma: no cover
import dataclasses # pragma: no cover

o = datetime.now() # pragma: no cover
def http_date(d): return d.isoformat() # pragma: no cover
decimal = decimal.Decimal('3.14') # pragma: no cover
uuid = uuid.UUID('12345678123456781234567812345678') # pragma: no cover
dataclass = dataclasses.make_dataclass('Example', [('x', int), ('y', int)]) # pragma: no cover
dataclasses_instance = dataclass(5, 6) # pragma: no cover
dataclasses.is_dataclass = dataclasses.is_dataclass(dataclasses_instance) # pragma: no cover
dataclasses.asdict = dataclasses.asdict(dataclasses_instance) # pragma: no cover
type('Mock', (object,), {'__html__': lambda self: '<html></html>'}) # pragma: no cover

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
