from datetime import date # pragma: no cover
from http import HTTPStatus # pragma: no cover
import decimal # pragma: no cover
import uuid # pragma: no cover
import dataclasses # pragma: no cover

o = 'example string' # pragma: no cover
date = date(2023, 10, 1) # pragma: no cover
http_date = lambda d: d.strftime('%a, %d %b %Y %H:%M:%S GMT') # pragma: no cover
decimal = type('MockDecimal', (decimal.Decimal,), {}) # pragma: no cover
uuid = type('MockUUID', (uuid.UUID,), {}) # pragma: no cover
dataclasses = type('MockDataclasses', (object,), {'is_dataclass': lambda x: False, 'asdict': lambda x: {}}) # pragma: no cover

from datetime import date # pragma: no cover
import decimal # pragma: no cover
import uuid # pragma: no cover
import dataclasses # pragma: no cover

o = date(2023, 10, 1) # pragma: no cover
http_date = lambda d: d.strftime('%a, %d %b %Y %H:%M:%S GMT') # pragma: no cover
decimal = decimal # pragma: no cover
uuid = uuid.UUID # pragma: no cover
dataclasses = dataclasses # pragma: no cover

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
