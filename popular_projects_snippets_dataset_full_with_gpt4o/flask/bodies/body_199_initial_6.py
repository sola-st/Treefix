from datetime import date # pragma: no cover
import decimal # pragma: no cover
import uuid # pragma: no cover
import dataclasses # pragma: no cover

o = date.today()  # You can change this to other types as needed for each condition # pragma: no cover
http_date = lambda x: x.strftime('%a, %d %b %Y %H:%M:%S GMT') # pragma: no cover
o = decimal.Decimal('10.5')  # Example object that is an instance of decimal.Decimal # pragma: no cover
o = uuid.uuid4()  # Example object that is an instance of uuid.UUID # pragma: no cover
dataclasses = type('Mock', (object,), {'is_dataclass': lambda x: isinstance(x, MockDataclass), 'asdict': lambda x: x.__dict__}) # pragma: no cover
class MockDataclass: # pragma: no cover
    def __init__(self, field): # pragma: no cover
        self.field = field # pragma: no cover
o = MockDataclass('value') # pragma: no cover
type('Mock', (object,), {'__html__': lambda self=type: '<html></html>'}) # pragma: no cover
o.__html__ = lambda: '<html></html>'  # Defining the __html__ method for object 'o' # pragma: no cover

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
