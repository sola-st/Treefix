import ast # pragma: no cover

node = type('MockNode', (object,), {'s': 'string_value', 'n': 42, 'value': True})() # pragma: no cover
ast3 = type('MockAST3', (object,), {}) # pragma: no cover
ast3.Str = ast.Str # pragma: no cover
ast3.Bytes = ast.Bytes # pragma: no cover
ast3.Num = ast.Num # pragma: no cover
ast3.NameConstant = ast.NameConstant # pragma: no cover

import ast # pragma: no cover

node = ast.Constant(value='example') # pragma: no cover
ast3 = type('MockAST3', (object,), {'Str': type('MockStr', (ast.AST,), {'s': 'example'}), 'Bytes': type('MockBytes', (ast.AST,), {'s': b'example'}), 'Num': type('MockNum', (ast.AST,), {'n': 123}), 'NameConstant': type('MockNameConstant', (ast.AST,), {'value': True})})() # pragma: no cover

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
