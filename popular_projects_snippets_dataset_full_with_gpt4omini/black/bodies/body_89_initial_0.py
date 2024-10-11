from typing import Any # pragma: no cover

class MockLine:  # Mock class for line object# pragma: no cover
    def __init__(self, depth: int):# pragma: no cover
        self.depth = depth # pragma: no cover
class MockSelf:  # Mock class with line_length attribute# pragma: no cover
    def __init__(self, line_length: int):# pragma: no cover
        self.line_length = line_length # pragma: no cover
line = MockLine(depth=2) # pragma: no cover
self = MockSelf(line_length=20) # pragma: no cover
ends_with_comma = True # pragma: no cover
string_op_leaves_length = 3 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/trans.py
from l3.Runtime import _l_
"""
            Returns:
                The max allowed length of the string value used for the last
                line we will construct.
            """
result = self.line_length
_l_(5789)
result -= line.depth * 4
_l_(5790)
result -= 1 if ends_with_comma else 0
_l_(5791)
result -= string_op_leaves_length
_l_(5792)
aux = result
_l_(5793)
exit(aux)
