from datetime import date # pragma: no cover
import decimal # pragma: no cover
import uuid # pragma: no cover
import dataclasses # pragma: no cover
from http.client import HTTPResponse # pragma: no cover

class MockDateClass(date): pass # pragma: no cover
class MockDecimalClass(decimal.Decimal): pass # pragma: no cover
class MockUUIDClass(uuid.UUID): pass # pragma: no cover
class MockDataclass: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.data = 'mock_data' # pragma: no cover
mock_html_class = type('MockHTMLClass', (object,), {'__html__': lambda self: '<html></html>'}) # pragma: no cover
o = MockDecimalClass('10.5') # pragma: no cover

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
