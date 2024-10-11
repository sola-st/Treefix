class MockLeaf:# pragma: no cover
    def __init__(self, type, value):# pragma: no cover
        self.type = type# pragma: no cover
        self.value = value# pragma: no cover
class MockToken:# pragma: no cover
    NAME = 'name'# pragma: no cover
# pragma: no cover
token = MockToken() # pragma: no cover
class MockSelf:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.depth = 0# pragma: no cover
        self._lambda_argument_depths = []# pragma: no cover
# pragma: no cover
self = MockSelf() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/brackets.py
from l3.Runtime import _l_
"""In a lambda expression, there might be more than one argument.

        To avoid splitting on the comma in this situation, increase the depth of
        tokens between `lambda` and `:`.
        """
if leaf.type == token.NAME and leaf.value == "lambda":
    _l_(4600)

    self.depth += 1
    _l_(4597)
    self._lambda_argument_depths.append(self.depth)
    _l_(4598)
    aux = True
    _l_(4599)
    exit(aux)
aux = False
_l_(4601)

exit(aux)
