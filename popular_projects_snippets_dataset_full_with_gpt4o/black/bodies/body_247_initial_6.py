from typing import List # pragma: no cover

class MockToken:# pragma: no cover
    NAME = 'NAME' # pragma: no cover
token = MockToken() # pragma: no cover
class MockLeaf:# pragma: no cover
    def __init__(self, type_, value):# pragma: no cover
        self.type = type_# pragma: no cover
        self.value = value # pragma: no cover
leaf = MockLeaf(token.NAME, 'lambda') # pragma: no cover
self = type('Mock', (object,), {# pragma: no cover
    'depth': 0,# pragma: no cover
    '_lambda_argument_depths': [],# pragma: no cover
    '__init__': lambda self: None# pragma: no cover
})() # pragma: no cover

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
