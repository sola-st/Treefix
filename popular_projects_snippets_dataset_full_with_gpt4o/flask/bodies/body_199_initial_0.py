from datetime import date # pragma: no cover
import datetime # pragma: no cover
import decimal # pragma: no cover
import uuid # pragma: no cover
import dataclasses # pragma: no cover

o = datetime.date.today() # pragma: no cover
def http_date(d): return d.isoformat() # pragma: no cover
o = decimal.Decimal('123.456') # pragma: no cover
o = uuid.UUID('12345678123456781234567812345678') # pragma: no cover
@dataclasses.dataclass# pragma: no cover
class MyDataClass: # pragma: no cover
    field: int = 10# pragma: no cover
# pragma: no cover
o = MyDataClass() # pragma: no cover
o.__html__ = lambda: '<html></html>' # pragma: no cover

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
