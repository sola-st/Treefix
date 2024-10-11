import collections # pragma: no cover
from types import SimpleNamespace # pragma: no cover

syms = SimpleNamespace(atom=1, expr_stmt=2, annassign=3, assert_stmt=4, return_stmt=5, except_clause=6, funcdef=7, with_stmt=8, for_stmt=9, del_stmt=10) # pragma: no cover
def is_empty_tuple(node): return False # pragma: no cover
def is_one_tuple(node): return False # pragma: no cover
def is_yield(node): return False # pragma: no cover
def is_tuple_containing_walrus(node): return False # pragma: no cover
def is_walrus_assignment(node): return False # pragma: no cover
def max_delimiter_priority_in_atom(node): return 0 # pragma: no cover
COMMA_PRIORITY = 1 # pragma: no cover
def is_lpar_token(token): return token == '(' # pragma: no cover
def is_rpar_token(token): return token == ')' # pragma: no cover
def maybe_make_parens_invisible_in_atom(node, parent, remove_brackets_around_comma): pass # pragma: no cover
def is_atom_with_invisible_parens(node): return False # pragma: no cover
node = SimpleNamespace(type=1, children=['(', 'middle_child', ')']) # pragma: no cover
parent = SimpleNamespace(type=0) # pragma: no cover
remove_brackets_around_comma = False # pragma: no cover

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
