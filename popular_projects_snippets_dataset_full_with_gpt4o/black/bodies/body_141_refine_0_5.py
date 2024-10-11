import ast # pragma: no cover

ast3 = type('Mock', (object,), {'Str': type('Mock', (object,), {}), 'Bytes': type('Mock', (object,), {}), 'Num': type('Mock', (object,), {}), 'NameConstant': type('Mock', (object,), {})}) # pragma: no cover
node = type('Mock', (object,), {'s': 'example string', 'n': 123, 'value': True})() # pragma: no cover

import ast # pragma: no cover

ast3 = type('Mock', (object,), {'Str': type('Mock', (object,), {'s': ''}), 'Bytes': type('Mock', (object,), {'s': b''}), 'Num': type('Mock', (object,), {'n': 0}), 'NameConstant': type('Mock', (object,), {'value': None})}) # pragma: no cover
class Node: pass # pragma: no cover
node = Node() # pragma: no cover
node.s = 'example string' # pragma: no cover
node.n = 123 # pragma: no cover
node.value = True # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/parsing.py
from l3.Runtime import _l_
"""Map ast nodes deprecated in 3.8 to Constant."""
if isinstance(node, (ast.Str, ast3.Str, ast.Bytes, ast3.Bytes)):
    _l_(17755)

    aux = ast.Constant(value=node.s)
    _l_(17754)
    exit(aux)

if isinstance(node, (ast.Num, ast3.Num)):
    _l_(17757)

    aux = ast.Constant(value=node.n)
    _l_(17756)
    exit(aux)

if isinstance(node, (ast.NameConstant, ast3.NameConstant)):
    _l_(17759)

    aux = ast.Constant(value=node.value)
    _l_(17758)
    exit(aux)
aux = node
_l_(17760)

exit(aux)
