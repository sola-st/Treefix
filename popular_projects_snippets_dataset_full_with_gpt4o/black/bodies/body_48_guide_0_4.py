from collections import namedtuple # pragma: no cover

syms = namedtuple('Syms', ['atom', 'expr_stmt', 'annassign', 'assert_stmt', 'return_stmt', 'except_clause', 'funcdef', 'with_stmt', 'for_stmt', 'del_stmt']) # pragma: no cover
syms.atom = 1 # pragma: no cover
syms.expr_stmt = 2 # pragma: no cover
syms.annassign = 3 # pragma: no cover
syms.assert_stmt = 4 # pragma: no cover
syms.return_stmt = 5 # pragma: no cover
syms.except_clause = 6 # pragma: no cover
syms.funcdef = 7 # pragma: no cover
syms.with_stmt = 8 # pragma: no cover
syms.for_stmt = 9 # pragma: no cover
syms.del_stmt = 10 # pragma: no cover
node = type('Mock', (object,), {'type': syms.atom, 'children': [type('Mock', (object,), {'value': '', 'type': 'L_PAR'}), 'middle_node', type('Mock', (object,), {'value': '', 'type': 'R_PAR'})]})() # pragma: no cover
parent = type('Mock', (object,), {'type': syms.expr_stmt})() # pragma: no cover
is_empty_tuple = lambda x: False # pragma: no cover
is_one_tuple = lambda x: False # pragma: no cover
is_yield = lambda x: False # pragma: no cover
remove_brackets_around_comma = False # pragma: no cover
max_delimiter_priority_in_atom = lambda x: 0 # pragma: no cover
COMMA_PRIORITY = 1 # pragma: no cover
is_tuple_containing_walrus = lambda x: False # pragma: no cover
is_walrus_assignment = lambda x: False # pragma: no cover
is_lpar_token = lambda x: x.type == 'L_PAR' # pragma: no cover
is_rpar_token = lambda x: x.type == 'R_PAR' # pragma: no cover
maybe_make_parens_invisible_in_atom = lambda *args, **kwargs: None # pragma: no cover
is_atom_with_invisible_parens = lambda x: False # pragma: no cover
exit = lambda x: x # pragma: no cover

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
