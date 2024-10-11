from typing import List, Callable # pragma: no cover

class MockTag:# pragma: no cover
    def __init__(self, tag):# pragma: no cover
        self._tag = tag# pragma: no cover
    def check(self, value):# pragma: no cover
        return isinstance(value, int)# pragma: no cover
    def tag(self, value):# pragma: no cover
        return f'Tagged: {value}'# pragma: no cover
# pragma: no cover
class Mock:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.order = [MockTag('example')] # pragma: no cover
value = 42 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/json/tag.py
from l3.Runtime import _l_
"""Convert a value to a tagged representation if necessary."""
for tag in self.order:
    _l_(9225)

    if tag.check(value):
        _l_(9224)

        aux = tag.tag(value)
        _l_(9223)
        exit(aux)
aux = value
_l_(9226)

exit(aux)
