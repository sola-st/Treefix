serial = 'mock_serial' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/6146963/when-is-del-useful-in-python
from l3.Runtime import _l_
del serial
_l_(985)
serial = None
_l_(986)

serial = None
_l_(987)

