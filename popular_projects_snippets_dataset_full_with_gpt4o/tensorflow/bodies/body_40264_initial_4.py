self = type('MockSelf', (object,), {'_tape': None, '_watched_variables': []})() # pragma: no cover
self._tape = type('MockTape', (object,), {'watched_variables': lambda: []})() # pragma: no cover
self._watched_variables = [] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop.py
from l3.Runtime import _l_
"""Returns variables watched by this tape in order of construction."""
if self._tape is not None:
    _l_(18683)

    self._watched_variables = self._tape.watched_variables()
    _l_(18682)
aux = self._watched_variables
_l_(18684)
exit(aux)
