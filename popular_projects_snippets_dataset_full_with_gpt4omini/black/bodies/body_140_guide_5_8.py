import ast # pragma: no cover
import sys # pragma: no cover
from typing import Any, Tuple, Type # pragma: no cover

class MockAST(ast.AST): # pragma: no cover
    _fields = ['value', 'targets'] # pragma: no cover
    def __init__(self, value=None, targets=None): # pragma: no cover
        self.value = value or 'example' # pragma: no cover
        self.targets = targets or [] # pragma: no cover
class MockTypeIgnore(ast.AST): # pragma: no cover
    _fields = ['lineno'] # pragma: no cover
    def __init__(self): # pragma: no cover
        self.lineno = 1 # pragma: no cover
node = MockAST(value='test_value', targets=[MockAST()]) # pragma: no cover
depth = 0 # pragma: no cover
_IS_PYPY = False # pragma: no cover
ast3 = type('ast3', (object,), {'TypeIgnore': MockTypeIgnore}) # pragma: no cover
def fixup_ast_constants(node): return node # pragma: no cover
def _normalize(separator, value): return value.strip() # pragma: no cover
def stringify_ast(node, depth): return f'Stringified: {node}, Depth: {depth}' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/parsing.py
from l3.Runtime import _l_
"""Simple visitor generating strings to compare ASTs by content."""

node = fixup_ast_constants(node)
_l_(4653)
aux = f"{'  ' * depth}{node.__class__.__name__}("
_l_(4654)

exit(aux)

type_ignore_classes: Tuple[Type[Any], ...]
_l_(4655)
for field in sorted(node._fields):
    _l_(4681)

    # TypeIgnore will not be present using pypy < 3.8, so need for this
    if not (_IS_PYPY and sys.version_info < (3, 8)):
        _l_(4661)

        # TypeIgnore has only one field 'lineno' which breaks this comparison
        type_ignore_classes = (ast3.TypeIgnore,)
        _l_(4656)
        if sys.version_info >= (3, 8):
            _l_(4658)

            type_ignore_classes += (ast.TypeIgnore,)
            _l_(4657)
        if isinstance(node, type_ignore_classes):
            _l_(4660)

            break
            _l_(4659)

    try:
        _l_(4665)

        value: object = getattr(node, field)
        _l_(4662)
    except AttributeError:
        _l_(4664)

        continue
        _l_(4663)
    aux = f"{'  ' * (depth+1)}{field}="
    _l_(4666)

    exit(aux)

    if isinstance(value, list):
        _l_(4680)

        for item in value:
            _l_(4672)

            # Ignore nested tuples within del statements, because we may insert
            # parentheses and they change the AST.
            if (
                field == "targets"
                and isinstance(node, (ast.Delete, ast3.Delete))
                and isinstance(item, (ast.Tuple, ast3.Tuple))
            ):
                _l_(4671)

                for elt in item.elts:
                    _l_(4668)

                    aux = stringify_ast(elt, depth + 2)
                    _l_(4667)
                    exit(aux)

            elif isinstance(item, (ast.AST, ast3.AST)):
                _l_(4670)

                aux = stringify_ast(item, depth + 2)
                _l_(4669)
                exit(aux)
    elif isinstance(value, (ast.AST, ast3_AST)):
        _l_(4679)

        aux = stringify_ast(value, depth + 2)
        _l_(4673)
        exit(aux)

    else:
        normalized: object
        _l_(4674)
        # Constant strings may be indented across newlines, if they are
        # docstrings; fold spaces after newlines when comparing. Similarly,
        # trailing and leading space may be removed.
        if (
            isinstance(node, ast.Constant)
            and field == "value"
            and isinstance(value, str)
        ):
            _l_(4677)

            normalized = _normalize("\n", value)
            _l_(4675)
        else:
            normalized = value
            _l_(4676)
        aux = f"{'  ' * (depth+2)}{normalized!r},  # {value.__class__.__name__}"
        _l_(4678)
        exit(aux)
aux = f"{'  ' * depth})  # /{node.__class__.__name__}"
_l_(4682)

exit(aux)
