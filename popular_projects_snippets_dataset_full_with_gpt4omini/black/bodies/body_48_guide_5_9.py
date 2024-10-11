from typing import List # pragma: no cover

class MockNode: # pragma: no cover
    def __init__(self, node_type: str, children: List['MockNode'] = None, value: str = ''): # pragma: no cover
        self.type = node_type # pragma: no cover
        self.children = children if children is not None else [] # pragma: no cover
        self.value = value # pragma: no cover
 # pragma: no cover
    def replace(self, new_child):  # Mock method to replace children # pragma: no cover
        self.children = [new_child] # pragma: no cover
 # pragma: no cover
class MockSyms: # pragma: no cover
    atom = 'atom' # pragma: no cover
    expr_stmt = 'expr_stmt' # pragma: no cover
    annassign = 'annassign' # pragma: no cover
    assert_stmt = 'assert_stmt' # pragma: no cover
    return_stmt = 'return_stmt' # pragma: no cover
    except_clause = 'except_clause' # pragma: no cover
    funcdef = 'funcdef' # pragma: no cover
    with_stmt = 'with_stmt' # pragma: no cover
    for_stmt = 'for_stmt' # pragma: no cover
    del_stmt = 'del_stmt' # pragma: no cover
 # pragma: no cover
syms = MockSyms() # pragma: no cover
COMMA_PRIORITY = 1 # pragma: no cover
remove_brackets_around_comma = False # pragma: no cover
def is_empty_tuple(node): # pragma: no cover
    return len(node.children) == 0 # pragma: no cover
 # pragma: no cover
def is_one_tuple(node): # pragma: no cover
    return len(node.children) == 1 # pragma: no cover
 # pragma: no cover
def is_yield(node): # pragma: no cover
    return False # pragma: no cover
 # pragma: no cover
def max_delimiter_priority_in_atom(node): # pragma: no cover
    return 3 # pragma: no cover
  # This should ensure the condition triggers # pragma: no cover
 # pragma: no cover
def is_tuple_containing_walrus(node): # pragma: no cover
    return False # pragma: no cover
 # pragma: no cover
def is_walrus_assignment(node): # pragma: no cover
    return False # pragma: no cover
 # pragma: no cover
def is_lpar_token(node): # pragma: no cover
    return node.value == '(' # pragma: no cover
 # pragma: no cover
def is_rpar_token(node): # pragma: no cover
    return node.value == ')' # pragma: no cover
 # pragma: no cover
def is_atom_with_invisible_parens(node): # pragma: no cover
    return False # pragma: no cover
 # pragma: no cover
def maybe_make_parens_invisible_in_atom(middle, parent, remove_brackets_around_comma): # pragma: no cover
    pass # pragma: no cover
 # pragma: no cover
first = MockNode('lpar', [], value='(') # pragma: no cover
middle = MockNode('middle_expr', []) # pragma: no cover
last = MockNode('rpar', [], value=')') # pragma: no cover
node = MockNode('tuple', [first, middle, last]) # pragma: no cover
parent = MockNode('expr_stmt', []) # pragma: no cover

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
    _l_(4091)

    aux = False
    _l_(4090)
    exit(aux)

if is_walrus_assignment(node):
    _l_(4094)

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
        _l_(4093)

        aux = False
        _l_(4092)
        exit(aux)

first = node.children[0]
_l_(4095)
last = node.children[-1]
_l_(4096)
if is_lpar_token(first) and is_rpar_token(last):
    _l_(4104)

    middle = node.children[1]
    _l_(4097)
    # make parentheses invisible
    first.value = ""
    _l_(4098)
    last.value = ""
    _l_(4099)
    maybe_make_parens_invisible_in_atom(
        middle,
        parent=parent,
        remove_brackets_around_comma=remove_brackets_around_comma,
    )
    _l_(4100)

    if is_atom_with_invisible_parens(middle):
        _l_(4102)

        # Strip the invisible parens from `middle` by replacing
        # it with the child in-between the invisible parens
        middle.replace(middle.children[1])
        _l_(4101)
    aux = False
    _l_(4103)

    exit(aux)
aux = True
_l_(4105)

exit(aux)
