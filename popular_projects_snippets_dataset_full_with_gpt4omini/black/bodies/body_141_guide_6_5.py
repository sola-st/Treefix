import ast # pragma: no cover

class MockConstant:  # Mock class for ast.Constant # pragma: no cover
    def __init__(self, value): # pragma: no cover
        self.value = value # pragma: no cover
 # pragma: no cover
class MockNum:  # Mock class for ast.Num # pragma: no cover
    def __init__(self, n): # pragma: no cover
        self.n = n # pragma: no cover
 # pragma: no cover
node = MockNum(n=42)  # Initialize node to trigger the ast.Num path. # pragma: no cover
ast.Constant = MockConstant # pragma: no cover
# Mock ast3.Num for consistency. # pragma: no cover

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
