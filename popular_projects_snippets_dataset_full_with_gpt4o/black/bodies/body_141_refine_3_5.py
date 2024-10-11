import ast # pragma: no cover

node = type('MockNode', (object,), {'s': 'value', 'n': 42, 'value': True})() # pragma: no cover
ast3 = type('MockAst3', (object,), {'Str': type('MockStr', (object,), {}), 'Bytes': type('MockBytes', (object,), {}), 'Num': type('MockNum', (object,), {}), 'NameConstant': type('MockNameConstant', (object,), {})})() # pragma: no cover

import ast # pragma: no cover

class MockNodeStr(ast.Str): # pragma: no cover
    s = 'value' # pragma: no cover
 # pragma: no cover
class MockNodeBytes(ast.Bytes): # pragma: no cover
    s = b'value' # pragma: no cover
 # pragma: no cover
class MockNodeNum(ast.Num): # pragma: no cover
    n = 42 # pragma: no cover
 # pragma: no cover
class MockNodeNameConstant(ast.NameConstant): # pragma: no cover
    value = True # pragma: no cover
 # pragma: no cover
node = MockNodeStr() # pragma: no cover
 # pragma: no cover
class MockAst3Str(ast.Str): # pragma: no cover
    pass # pragma: no cover
 # pragma: no cover
class MockAst3Bytes(ast.Bytes): # pragma: no cover
    pass # pragma: no cover
 # pragma: no cover
class MockAst3Num(ast.Num): # pragma: no cover
    pass # pragma: no cover
 # pragma: no cover
class MockAst3NameConstant(ast.NameConstant): # pragma: no cover
    pass # pragma: no cover
 # pragma: no cover
ast3 = type('MockAst3', (object,), {'Str': MockAst3Str, 'Bytes': MockAst3Bytes, 'Num': MockAst3Num, 'NameConstant': MockAst3NameConstant})() # pragma: no cover

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
