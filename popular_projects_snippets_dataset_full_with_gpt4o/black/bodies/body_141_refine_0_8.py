import ast # pragma: no cover

ast3 = type('Mock', (object,), {'Str': type('Mock', (object,), {}), 'Bytes': type('Mock', (object,), {}), 'Num': type('Mock', (object,), {}), 'NameConstant': type('Mock', (object,), {})}) # pragma: no cover
node = type('Mock', (object,), {'s': 'example string', 'n': 123, 'value': True})() # pragma: no cover

import ast # pragma: no cover

class MockNode:# pragma: no cover
    def __init__(self, s='example string', n=123, value=True):# pragma: no cover
        self.s = s# pragma: no cover
        self.n = n# pragma: no cover
        self.value = value# pragma: no cover
# pragma: no cover
class MockAST3:# pragma: no cover
    class Str: pass# pragma: no cover
    class Bytes: pass# pragma: no cover
    class Num: pass# pragma: no cover
    class NameConstant: pass # pragma: no cover
node = MockNode() # pragma: no cover
ast3 = MockAST3() # pragma: no cover

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
