import sys # pragma: no cover
import ast # pragma: no cover
from typing import Tuple, Type, Any # pragma: no cover

def fixup_ast_constants(node):# pragma: no cover
    return node # pragma: no cover
node = type('Mock', (object,), {'__class__': type('MockClass', (object,), {'__name__': 'MockNode'}), '_fields': ['mock_field']})() # pragma: no cover
depth = 0 # pragma: no cover
_IS_PYPY = False # pragma: no cover
class MockAST3:# pragma: no cover
    class TypeIgnore:# pragma: no cover
        pass# pragma: no cover
    class Delete:# pragma: no cover
        pass# pragma: no cover
    class Tuple:# pragma: no cover
        elts = []# pragma: no cover
    class AST:# pragma: no cover
        pass # pragma: no cover
ast3 = MockAST3 # pragma: no cover
def stringify_ast(node, depth):# pragma: no cover
    return str(node) # pragma: no cover
ast3_AST = MockAST3.AST # pragma: no cover
def _normalize(sep, value):# pragma: no cover
    return value.replace(sep, ' ') # pragma: no cover

import sys # pragma: no cover
import ast # pragma: no cover
from typing import Tuple, Type, Any # pragma: no cover

def fixup_ast_constants(node): return node # pragma: no cover
class MockNode:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.__class__ = type('MockClass', (object,), {'__name__': 'MockClassName'})# pragma: no cover
        self._fields = ['field1']# pragma: no cover
        self.field1 = 'mock_value'# pragma: no cover
node = MockNode() # pragma: no cover
depth = 0 # pragma: no cover
_IS_PYPY = False # pragma: no cover
class MockTypeIgnore: pass # pragma: no cover
class MockAST3Delete: pass # pragma: no cover
class MockAST3Tuple:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.elts = [] # pragma: no cover
class MockAST3AST: pass # pragma: no cover
ast3 = type('MockAST3', (object,), {'TypeIgnore': MockTypeIgnore, 'Delete': MockAST3Delete, 'Tuple': MockAST3Tuple, 'AST': MockAST3AST}) # pragma: no cover
class MockASTDelete: pass # pragma: no cover
class MockASTTuple:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.elts = [] # pragma: no cover
class MockASTAST: pass # pragma: no cover
class MockASTConstant:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.value = 'mock_value' # pragma: no cover
ast = type('MockAST', (object,), {'Delete': MockASTDelete, 'Tuple': MockASTTuple, 'AST': MockASTAST, 'Constant': MockASTConstant}) # pragma: no cover
def stringify_ast(node, depth): return '' # pragma: no cover
ast3_AST = MockAST3AST # pragma: no cover
def _normalize(sep, value): return value.replace(sep, ' ').strip() # pragma: no cover

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
