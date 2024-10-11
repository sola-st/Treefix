from collections import namedtuple # pragma: no cover

Leaf = namedtuple('Leaf', ['type', 'value']) # pragma: no cover
leaf = Leaf(type='NAME', value='lambda') # pragma: no cover
Token = namedtuple('Token', ['NAME']) # pragma: no cover
token = Token(NAME='NAME') # pragma: no cover
MockSelf = type('MockSelf', (object,), {'depth': 0, '_lambda_argument_depths': []}) # pragma: no cover
self = MockSelf() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/brackets.py
from l3.Runtime import _l_
"""In a lambda expression, there might be more than one argument.

        To avoid splitting on the comma in this situation, increase the depth of
        tokens between `lambda` and `:`.
        """
if leaf.type == token.NAME and leaf.value == "lambda":
    _l_(16410)

    self.depth += 1
    _l_(16407)
    self._lambda_argument_depths.append(self.depth)
    _l_(16408)
    aux = True
    _l_(16409)
    exit(aux)
aux = False
_l_(16411)

exit(aux)
