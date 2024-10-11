import ast # pragma: no cover

node = type('MockNode', (object,), {'s': 'string_value', 'n': 42, 'value': True})() # pragma: no cover
ast3 = type('MockAST3', (object,), {}) # pragma: no cover
ast3.Str = ast.Str # pragma: no cover
ast3.Bytes = ast.Bytes # pragma: no cover
ast3.Num = ast.Num # pragma: no cover
ast3.NameConstant = ast.NameConstant # pragma: no cover

import ast # pragma: no cover

node_str = ast.Str('string_value') # pragma: no cover
node_bytes = ast.Bytes(b'string_value') # pragma: no cover
node_num = ast.Num(42) # pragma: no cover
node_name_const = ast.NameConstant(True) # pragma: no cover
ast3 = type('Mock', (object,), {'Str': type('MockStr', (object,), {'s': 'string_value'}), 'Bytes': type('MockBytes', (object,), {'s': b'string_value'}), 'Num': type('MockNum', (object,), {'n': 42}), 'NameConstant': type('MockNameConstant', (object,), {'value': True})})() # pragma: no cover
node = type('MockNode', (object,), {'s': 'string_value', 'n': 42, 'value': True})() # pragma: no cover

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
