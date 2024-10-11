import ast # pragma: no cover
import ast as ast3 # pragma: no cover
class Mock: pass # pragma: no cover

node = Mock() # pragma: no cover
node.s = 'example string' # pragma: no cover
node.n = 42 # pragma: no cover
node.value = True # pragma: no cover
ast.Str = Mock() # pragma: no cover
ast3.Str = Mock() # pragma: no cover
ast.Bytes = Mock() # pragma: no cover
ast3.Bytes = Mock() # pragma: no cover
ast.Constant = Mock() # pragma: no cover
ast.Num = Mock() # pragma: no cover
ast3.Num = Mock() # pragma: no cover
ast.NameConstant = Mock() # pragma: no cover
ast3.NameConstant = Mock() # pragma: no cover

import ast # pragma: no cover
import ast as ast3 # pragma: no cover

class MockStr: pass # pragma: no cover
class MockBytes: pass # pragma: no cover
class MockNum: pass # pragma: no cover
class MockConstant: pass # pragma: no cover
class MockNameConstant: pass # pragma: no cover
node = MockStr() # pragma: no cover
node.s = 'example string' # pragma: no cover
ast.Str = MockStr # pragma: no cover
ast3.Str = MockStr # pragma: no cover
ast.Bytes = MockBytes # pragma: no cover
ast3.Bytes = MockBytes # pragma: no cover
ast.Num = MockNum # pragma: no cover
ast3.Num = MockNum # pragma: no cover
ast.Constant = MockConstant # pragma: no cover
ast.NameConstant = MockNameConstant # pragma: no cover
ast3.NameConstant = MockNameConstant # pragma: no cover
node.n = 42 # pragma: no cover
node.value = True # pragma: no cover

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
