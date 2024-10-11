import ast # pragma: no cover

node = ast.Constant(value='example') # pragma: no cover
ast.Str = type('MockStr', (object,), {'__init__': lambda self, s: None, 's': 'example'}) # pragma: no cover
ast.Bytes = type('MockBytes', (object,), {'__init__': lambda self, b: None, 's': b'example'}) # pragma: no cover
ast.Constant = type('MockConstant', (object,), {'__init__': lambda self, value: None}) # pragma: no cover
ast.Num = type('MockNum', (object,), {'__init__': lambda self, n: None, 'n': 42}) # pragma: no cover
ast.NameConstant = type('MockNameConstant', (object,), {'__init__': lambda self, value: None, 'value': True}) # pragma: no cover

import ast # pragma: no cover

class MockStr: # pragma: no cover
    def __init__(self, s): # pragma: no cover
        self.s = s # pragma: no cover
class MockBytes: # pragma: no cover
    def __init__(self, b): # pragma: no cover
        self.b = b # pragma: no cover
class MockConstant: # pragma: no cover
    def __init__(self, value): # pragma: no cover
        self.value = value # pragma: no cover
class MockNum: # pragma: no cover
    def __init__(self, n): # pragma: no cover
        self.n = n # pragma: no cover
class MockNameConstant: # pragma: no cover
    def __init__(self, value): # pragma: no cover
        self.value = value # pragma: no cover
ast.Str = MockStr # pragma: no cover
ast.Bytes = MockBytes # pragma: no cover
ast.Constant = MockConstant # pragma: no cover
ast.Num = MockNum # pragma: no cover
ast.NameConstant = MockNameConstant # pragma: no cover
node = ast.Str('example string') # pragma: no cover

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
