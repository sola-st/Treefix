import ast # pragma: no cover
import typing # pragma: no cover

node = ast.Constant(value='example') # pragma: no cover
ast3 = type('MockAst3', (object,), { 'Str': ast.Str, 'Bytes': ast.Bytes, 'Num': ast.Num, 'NameConstant': ast.NameConstant, 'Constant': ast.Constant }) # pragma: no cover
ast = type('MockAst', (object,), { 'Str': ast.Str, 'Bytes': ast.Bytes, 'Num': ast.Num, 'NameConstant': ast.NameConstant, 'Constant': ast.Constant }) # pragma: no cover

import ast # pragma: no cover

node = ast.Constant(value='example_string') # pragma: no cover
ast.Str = type('MockStr', (object,), {'__init__': lambda self, s: setattr(self, 's', s)}) # pragma: no cover
ast.Bytes = type('MockBytes', (object,), {'__init__': lambda self, b: setattr(self, 's', b)}) # pragma: no cover
ast.Constant = type('MockConstant', (object,), {'__init__': lambda self, value: setattr(self, 'value', value)}) # pragma: no cover
ast.Num = type('MockNum', (object,), {'__init__': lambda self, n: setattr(self, 'n', n)}) # pragma: no cover
ast.NameConstant = type('MockNameConstant', (object,), {'__init__': lambda self, value: setattr(self, 'value', value)}) # pragma: no cover

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
