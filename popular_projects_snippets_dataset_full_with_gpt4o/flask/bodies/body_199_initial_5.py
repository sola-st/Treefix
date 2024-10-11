import datetime # pragma: no cover
from datetime import date # pragma: no cover
import decimal # pragma: no cover
import uuid # pragma: no cover
import dataclasses # pragma: no cover

o = date(2023, 10, 3) # pragma: no cover
def http_date(date_obj): return date_obj.strftime('%a, %d %b %Y %H:%M:%S GMT') # pragma: no cover
decimal = type('decimal', (object,), {'Decimal': decimal.Decimal}) # pragma: no cover
uuid = type('uuid', (object,), {'UUID': uuid.UUID}) # pragma: no cover
dataclasses = type('dataclasses', (object,), {'is_dataclass': dataclasses.is_dataclass, 'asdict': dataclasses.asdict}) # pragma: no cover
class MockHTML:# pragma: no cover
    def __html__(self):# pragma: no cover
        return '<html></html>'# pragma: no cover
o = MockHTML() # pragma: no cover

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
