self = type('Mock', (object,), {'get_result_as_array': lambda self: [1, 2, 3]})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/io/formats/format.py
from l3.Runtime import _l_
aux = list(self.get_result_as_array())
_l_(21348)
exit(aux)
