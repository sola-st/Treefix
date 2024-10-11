self = type('Mock', (object,), {'line_length': 100})() # pragma: no cover
line = type('Mock', (object,), {'depth': 2})() # pragma: no cover
ends_with_comma = True # pragma: no cover
string_op_leaves_length = 5 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/trans.py
from l3.Runtime import _l_
"""
            Returns:
                The max allowed length of the string value used for the last
                line we will construct.
            """
result = self.line_length
_l_(17210)
result -= line.depth * 4
_l_(17211)
result -= 1 if ends_with_comma else 0
_l_(17212)
result -= string_op_leaves_length
_l_(17213)
aux = result
_l_(17214)
exit(aux)
