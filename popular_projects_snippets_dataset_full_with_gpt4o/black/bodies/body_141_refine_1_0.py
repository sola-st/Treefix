import ast # pragma: no cover

node = ast.Str(s='example string') # pragma: no cover
ast3 = type('Mock', (object,), {'Str': ast.Str, 'Bytes': ast.Bytes, 'Num': ast.Num, 'NameConstant': ast.NameConstant}) # pragma: no cover
node.s = 'example string' # pragma: no cover
node.n = 10 # pragma: no cover
node.value = True # pragma: no cover

import ast # pragma: no cover

class MockStr(ast.Str): # pragma: no cover
    def __init__(self, s): # pragma: no cover
        self.s = s # pragma: no cover
 # pragma: no cover
class MockBytes(ast.Bytes): # pragma: no cover
    def __init__(self, s): # pragma: no cover
        self.s = s # pragma: no cover
        self.value = s # pragma: no cover
 # pragma: no cover
class MockNum(ast.Num): # pragma: no cover
    def __init__(self, n): # pragma: no cover
        self.n = n # pragma: no cover
 # pragma: no cover
class MockNameConstant(ast.NameConstant): # pragma: no cover
    def __init__(self, value): # pragma: no cover
        self.value = value # pragma: no cover
 # pragma: no cover
ast3 = type('MockAST3', (object,), { # pragma: no cover
    'Str': MockStr, # pragma: no cover
    'Bytes': MockBytes, # pragma: no cover
    'Num': MockNum, # pragma: no cover
    'NameConstant': MockNameConstant # pragma: no cover
}) # pragma: no cover
 # pragma: no cover
node = MockStr(s='example string') # pragma: no cover

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
