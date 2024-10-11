import datetime # pragma: no cover
import decimal # pragma: no cover
import uuid # pragma: no cover
import dataclasses # pragma: no cover
from wsgiref.handlers import format_date_time as http_date # pragma: no cover
from time import mktime # pragma: no cover

class MockDataclass: # pragma: no cover
    pass # pragma: no cover
@dataclasses.dataclass # pragma: no cover
class SampleDataclass: # pragma: no cover
    field: int # pragma: no cover
o = MockDataclass() # pragma: no cover
def http_date(d): return format_date_time(mktime(d.timetuple())) # pragma: no cover

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
