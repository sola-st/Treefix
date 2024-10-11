import types # pragma: no cover

MockSyms = type('MockSyms', (object,), {'atom': 'atom', 'expr_stmt': 'expr_stmt', 'annassign': 'annassign', 'assert_stmt': 'assert_stmt', 'return_stmt': 'return_stmt', 'except_clause': 'except_clause', 'funcdef': 'funcdef', 'with_stmt': 'with_stmt', 'for_stmt': 'for_stmt', 'del_stmt': 'del_stmt'}) # pragma: no cover
syms = MockSyms() # pragma: no cover
def is_empty_tuple(node): return False # pragma: no cover
def is_one_tuple(node): return False # pragma: no cover
def is_yield(node): return False # pragma: no cover
MockParent = type('MockParent', (object,), {'type': 'expr_stmt'}) # pragma: no cover
parent = MockParent() # pragma: no cover
remove_brackets_around_comma = False # pragma: no cover
def max_delimiter_priority_in_atom(node): return 0 # pragma: no cover
COMMA_PRIORITY = 1 # pragma: no cover
def is_tuple_containing_walrus(node): return False # pragma: no cover
def is_walrus_assignment(node): return False # pragma: no cover
def is_lpar_token(token): return token == '(' # pragma: no cover
def is_rpar_token(token): return token == ')' # pragma: no cover
def maybe_make_parens_invisible_in_atom(middle, parent, remove_brackets_around_comma): pass # pragma: no cover
def is_atom_with_invisible_parens(middle): return False # pragma: no cover
MockNode = type('MockNode', (object,), {'type': 'atom', 'children': [('(', ), 'middle node', (')', )]}) # pragma: no cover
node = MockNode() # pragma: no cover

from typing import List # pragma: no cover

MockToken = type('MockToken', (object,), {'value': ''}) # pragma: no cover
node = type('MockNode', (object,), {'type': 'atom', 'children': [MockToken(), type('MockMiddle', (object,), {'children': ['first', 'child', 'last']})(), MockToken()]})() # pragma: no cover
syms = type('MockSyms', (object,), {'atom': 'atom', 'expr_stmt': 'expr_stmt', 'annassign': 'annassign', 'assert_stmt': 'assert_stmt', 'return_stmt': 'return_stmt', 'except_clause': 'except_clause', 'funcdef': 'funcdef', 'with_stmt': 'with_stmt', 'for_stmt': 'for_stmt', 'del_stmt': 'del_stmt'})() # pragma: no cover
is_empty_tuple = lambda x: False # pragma: no cover
is_one_tuple = lambda x: False # pragma: no cover
is_yield = lambda x: x.type == 'yield' # pragma: no cover
parent = type('MockParent', (object,), {'type': 'expr_stmt'})() # pragma: no cover
remove_brackets_around_comma = False # pragma: no cover
max_delimiter_priority_in_atom = lambda x: 0 # pragma: no cover
COMMA_PRIORITY = 1 # pragma: no cover
is_tuple_containing_walrus = lambda x: False # pragma: no cover
is_walrus_assignment = lambda x: x.type == 'walrus_assignment' # pragma: no cover
is_lpar_token = lambda x: isinstance(x, MockToken) and x.value == '(' # pragma: no cover
is_rpar_token = lambda x: isinstance(x, MockToken) and x.value == ')' # pragma: no cover
maybe_make_parens_invisible_in_atom = lambda middle, parent, remove_brackets_around_comma: None # pragma: no cover
is_atom_with_invisible_parens = lambda middle: middle.children[0] == 'first' and middle.children[-1] == 'last' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/linegen.py
from l3.Runtime import _l_
"""If it's safe, make the parens in the atom `node` invisible, recursively.
    Additionally, remove repeated, adjacent invisible parens from the atom `node`
    as they are redundant.

    Returns whether the node should itself be wrapped in invisible parentheses.
    """
if (
    node.type != syms.atom
    or is_empty_tuple(node)
    or is_one_tuple(node)
    or (is_yield(node) and parent.type != syms.expr_stmt)
    or (
        # This condition tries to prevent removing non-optional brackets
        # around a tuple, however, can be a bit overzealous so we provide
        # and option to skip this check for `for` and `with` statements.
        not remove_brackets_around_comma
        and max_delimiter_priority_in_atom(node) >= COMMA_PRIORITY
    )
    or is_tuple_containing_walrus(node)
):
    _l_(15635)

    aux = False
    _l_(15634)
    exit(aux)

if is_walrus_assignment(node):
    _l_(15638)

    if parent.type in [
        syms.annassign,
        syms.expr_stmt,
        syms.assert_stmt,
        syms.return_stmt,
        syms.except_clause,
        syms.funcdef,
        syms.with_stmt,
        # these ones aren't useful to end users, but they do please fuzzers
        syms.for_stmt,
        syms.del_stmt,
        syms.for_stmt,
    ]:
        _l_(15637)

        aux = False
        _l_(15636)
        exit(aux)

first = node.children[0]
_l_(15639)
last = node.children[-1]
_l_(15640)
if is_lpar_token(first) and is_rpar_token(last):
    _l_(15648)

    middle = node.children[1]
    _l_(15641)
    # make parentheses invisible
    first.value = ""
    _l_(15642)
    last.value = ""
    _l_(15643)
    maybe_make_parens_invisible_in_atom(
        middle,
        parent=parent,
        remove_brackets_around_comma=remove_brackets_around_comma,
    )
    _l_(15644)

    if is_atom_with_invisible_parens(middle):
        _l_(15646)

        # Strip the invisible parens from `middle` by replacing
        # it with the child in-between the invisible parens
        middle.replace(middle.children[1])
        _l_(15645)
    aux = False
    _l_(15647)

    exit(aux)
aux = True
_l_(15649)

exit(aux)
