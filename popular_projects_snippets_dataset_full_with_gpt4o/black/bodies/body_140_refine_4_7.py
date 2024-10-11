import sys # pragma: no cover
import ast # pragma: no cover
from typing import Tuple, Type, Any # pragma: no cover

fixup_ast_constants = lambda x: x # Mock implementation # pragma: no cover
node = type('MockNode', (object,), {'_fields': [], '__class__': type('Mock', (object,), {})})() # pragma: no cover
depth = 0 # pragma: no cover
Tuple = tuple # pragma: no cover
Type = type # pragma: no cover
_IS_PYPY = False # pragma: no cover
sys.version_info = (3, 8) # pragma: no cover
ast3 = type('MockAst3', (object,), {'TypeIgnore': type('TypeIgnore', (object,), {})}) # pragma: no cover
ast3_AST = type('MockAst3_AST', (object,), {}) # pragma: no cover
ast.Delete = type('Delete', (object,), {}) # pragma: no cover
ast3.Delete = type('Delete', (object,), {}) # pragma: no cover
ast.Tuple = type('Tuple', (object,), {'elts': []}) # pragma: no cover
ast3.Tuple = type('Tuple', (object,), {'elts': []}) # pragma: no cover
ast.AST = type('AST', (object,), {}) # pragma: no cover
ast3.AST = type('AST', (object,), {}) # pragma: no cover
ast.Constant = type('Constant', (object,), {}) # pragma: no cover
stringify_ast = lambda x, y: '' # Mock implementation # pragma: no cover
_normalize = lambda x, y: '' # Mock implementation # pragma: no cover

import sys # pragma: no cover
import ast # pragma: no cover
from typing import Tuple, Type, Any # pragma: no cover

def fixup_ast_constants(node): return node # pragma: no cover
class MockClass:# pragma: no cover
    __name__ = 'MockClass'# pragma: no cover
node = type('MockNode', (object,), {'__class__': MockClass, '_fields': ['field1'], 'field1': None})() # pragma: no cover
depth = 0 # pragma: no cover
_IS_PYPY = False # pragma: no cover
class AST3TypeIgnore: pass # pragma: no cover
ast3 = type('MockAst3', (object,), {'TypeIgnore': AST3TypeIgnore, 'Delete': type('MockDelete', (object,), {}), 'Tuple': type('MockTuple', (object,), {'elts': []}), 'AST': type('MockAST', (object,), {})}) # pragma: no cover
stringify_ast = lambda x, y: 'stringified_ast' # pragma: no cover
ast3_AST = type('MockAST3', (object,), {}) # pragma: no cover
def _normalize(sep, value): return value.replace(sep, ' ').strip() # pragma: no cover
class PyVer:# pragma: no cover
    def __init__(self, major, minor):# pragma: no cover
        self.major = major# pragma: no cover
        self.minor = minor# pragma: no cover
    def __ge__(self, other):# pragma: no cover
        if self.major > other[0] or (self.major == other[0] and self.minor >= other[1]):# pragma: no cover
            return True# pragma: no cover
        return False# pragma: no cover
sys.version_info = PyVer(3, 8) # pragma: no cover
ast.Delete = type('Delete', (object,), {}) # pragma: no cover
ast.Tuple = type('Tuple', (object,), {'elts': []}) # pragma: no cover
ast.AST = type('AST', (object,), {}) # pragma: no cover
ast.Constant = type('Constant', (object,), {}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/parsing.py
from l3.Runtime import _l_
"""Simple visitor generating strings to compare ASTs by content."""

node = fixup_ast_constants(node)
_l_(16269)
aux = f"{'  ' * depth}{node.__class__.__name__}("
_l_(16270)

exit(aux)

type_ignore_classes: Tuple[Type[Any], ...]
_l_(16271)
for field in sorted(node._fields):
    _l_(16297)

    # TypeIgnore will not be present using pypy < 3.8, so need for this
    if not (_IS_PYPY and sys.version_info < (3, 8)):
        _l_(16277)

        # TypeIgnore has only one field 'lineno' which breaks this comparison
        type_ignore_classes = (ast3.TypeIgnore,)
        _l_(16272)
        if sys.version_info >= (3, 8):
            _l_(16274)

            type_ignore_classes += (ast.TypeIgnore,)
            _l_(16273)
        if isinstance(node, type_ignore_classes):
            _l_(16276)

            break
            _l_(16275)

    try:
        _l_(16281)

        value: object = getattr(node, field)
        _l_(16278)
    except AttributeError:
        _l_(16280)

        continue
        _l_(16279)
    aux = f"{'  ' * (depth+1)}{field}="
    _l_(16282)

    exit(aux)

    if isinstance(value, list):
        _l_(16296)

        for item in value:
            _l_(16288)

            # Ignore nested tuples within del statements, because we may insert
            # parentheses and they change the AST.
            if (
                field == "targets"
                and isinstance(node, (ast.Delete, ast3.Delete))
                and isinstance(item, (ast.Tuple, ast3.Tuple))
            ):
                _l_(16287)

                for elt in item.elts:
                    _l_(16284)

                    aux = stringify_ast(elt, depth + 2)
                    _l_(16283)
                    exit(aux)

            elif isinstance(item, (ast.AST, ast3.AST)):
                _l_(16286)

                aux = stringify_ast(item, depth + 2)
                _l_(16285)
                exit(aux)
    elif isinstance(value, (ast.AST, ast3_AST)):
        _l_(16295)

        aux = stringify_ast(value, depth + 2)
        _l_(16289)
        exit(aux)

    else:
        normalized: object
        _l_(16290)
        # Constant strings may be indented across newlines, if they are
        # docstrings; fold spaces after newlines when comparing. Similarly,
        # trailing and leading space may be removed.
        if (
            isinstance(node, ast.Constant)
            and field == "value"
            and isinstance(value, str)
        ):
            _l_(16293)

            normalized = _normalize("\n", value)
            _l_(16291)
        else:
            normalized = value
            _l_(16292)
        aux = f"{'  ' * (depth+2)}{normalized!r},  # {value.__class__.__name__}"
        _l_(16294)
        exit(aux)
aux = f"{'  ' * depth})  # /{node.__class__.__name__}"
_l_(16298)

exit(aux)
