import ast # pragma: no cover
import ast as ast3 # pragma: no cover

node = type('MockNode', (object,), {'s': 'example string', 'n': 42, 'value': True})() # pragma: no cover
ast.Str = ast.Str # pragma: no cover
ast3.Str = ast.Str # pragma: no cover
ast.Bytes = ast.Bytes # pragma: no cover
ast3.Bytes = ast.Bytes # pragma: no cover
ast.Constant = type('MockConstant', (object,), {'__init__': lambda self, value: setattr(self, 'value', value)}) # pragma: no cover
ast.Num = ast.Num # pragma: no cover
ast3.Num = ast.Num # pragma: no cover
ast.NameConstant = ast.NameConstant # pragma: no cover
ast3.NameConstant = ast.NameConstant # pragma: no cover

import ast # pragma: no cover
import ast as ast3 # pragma: no cover

node = type('MockNode', (object,), {'s': 'example string', 'n': 42, 'value': True})() # pragma: no cover
ast.Str = type('MockStr', (object,), {}) # pragma: no cover
ast3.Str = ast.Str # pragma: no cover
ast.Bytes = type('MockBytes', (object,), {}) # pragma: no cover
ast3.Bytes = ast.Bytes # pragma: no cover
ast.Constant = type('MockConstant', (object,), {'__init__': lambda self, value: setattr(self, 'value', value)}) # pragma: no cover
ast.Num = type('MockNum', (object,), {}) # pragma: no cover
ast3.Num = ast.Num # pragma: no cover
ast.NameConstant = type('MockNameConstant', (object,), {}) # pragma: no cover
ast3.NameConstant = ast.NameConstant # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/parsing.py
from l3.Runtime import _l_
"""Map ast nodes deprecated in 3.8 to Constant."""
if isinstance(node, (ast.Str, ast3.Str, ast.Bytes, ast3.Bytes)):
    _l_(5934)

    aux = ast.Constant(value=node.s)
    _l_(5933)
    exit(aux)

if isinstance(node, (ast.Num, ast3.Num)):
    _l_(5936)

    aux = ast.Constant(value=node.n)
    _l_(5935)
    exit(aux)

if isinstance(node, (ast.NameConstant, ast3.NameConstant)):
    _l_(5938)

    aux = ast.Constant(value=node.value)
    _l_(5937)
    exit(aux)
aux = node
_l_(5939)

exit(aux)
