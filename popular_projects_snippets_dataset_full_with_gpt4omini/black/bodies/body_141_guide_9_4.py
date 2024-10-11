import ast # pragma: no cover

class MockConstant:  # Mock class for ast.Constant # pragma: no cover
    def __init__(self, value): # pragma: no cover
        self.value = value # pragma: no cover
 # pragma: no cover
class MockStr:  # Mock class for ast.Str # pragma: no cover
    def __init__(self, s): # pragma: no cover
        self.s = s # pragma: no cover
 # pragma: no cover
node = MockStr('example') # pragma: no cover
# Initialize node to trigger the ast.Str path. # pragma: no cover
ast.Constant = MockConstant # pragma: no cover
# Mock ast.Constant to simulate its behavior. # pragma: no cover
ast3 = type('MockAst3', (object,), {'Str': MockStr})() # pragma: no cover
# Create a mock for ast3 with necessary Str. # pragma: no cover

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
