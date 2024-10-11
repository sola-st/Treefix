from lib2to3.pgen2.token import NAME # pragma: no cover
from lib2to3.pygram import python_grammar # pragma: no cover

node = type('MockNode', (object,), {'__str__': lambda self: 'mocked_node'})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/parsing.py
from l3.Runtime import _l_
"""Given a lib2to3 node, return its string representation."""
code = str(node)
_l_(7207)
aux = code
_l_(7208)
exit(aux)
