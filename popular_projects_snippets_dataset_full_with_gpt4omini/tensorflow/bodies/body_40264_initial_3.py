class MockTape:# pragma: no cover
    def watched_variables(self):# pragma: no cover
        return ['var1', 'var2', 'var3'] # pragma: no cover
self = type('Mock', (object,), {'_tape': MockTape(), '_watched_variables': None})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop.py
from l3.Runtime import _l_
"""Returns variables watched by this tape in order of construction."""
if self._tape is not None:
    _l_(6310)

    self._watched_variables = self._tape.watched_variables()
    _l_(6309)
aux = self._watched_variables
_l_(6311)
exit(aux)
