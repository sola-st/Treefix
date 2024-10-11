import datetime # pragma: no cover
import decimal # pragma: no cover
import uuid # pragma: no cover
import dataclasses # pragma: no cover
from http.client import HTTPConnection # pragma: no cover
from wsgiref.handlers import format_date_time # pragma: no cover
from time import mktime # pragma: no cover

class MockDatetime(datetime.datetime): # pragma: no cover
    @staticmethod # pragma: no cover
    def utcnow(): # pragma: no cover
        return datetime.datetime(2023, 10, 5, 12, 0, 0) # pragma: no cover
 # pragma: no cover
def http_date(dt): # pragma: no cover
    if isinstance(dt, (datetime.datetime, datetime.date)):  # pragma: no cover
        timestamp = mktime(dt.timetuple()) # pragma: no cover
        return format_date_time(timestamp) # pragma: no cover
    return dt # pragma: no cover
 # pragma: no cover
o = MockDatetime.utcnow() # pragma: no cover

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
