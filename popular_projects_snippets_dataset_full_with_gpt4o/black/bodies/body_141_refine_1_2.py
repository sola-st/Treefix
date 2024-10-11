import ast # pragma: no cover

node = ast.Str(s='example string') # pragma: no cover
ast3 = type('Mock', (object,), {'Str': ast.Str, 'Bytes': ast.Bytes, 'Num': ast.Num, 'NameConstant': ast.NameConstant}) # pragma: no cover
node.s = 'example string' # pragma: no cover
node.n = 10 # pragma: no cover
node.value = True # pragma: no cover

import ast # pragma: no cover

class MockNode: pass # pragma: no cover
node = MockNode() # pragma: no cover
node.s = 'example string' # pragma: no cover
node.n = 123 # pragma: no cover
node.value = True # pragma: no cover
ast3 = type('Mock', (object,), {'Str': type('Str', (object,), {}), 'Bytes': type('Bytes', (object,), {}), 'Num': type('Num', (object,), {}), 'NameConstant': type('NameConstant', (object,), {})}) # pragma: no cover

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
