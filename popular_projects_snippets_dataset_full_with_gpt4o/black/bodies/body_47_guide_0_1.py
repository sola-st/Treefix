from types import SimpleNamespace # pragma: no cover
from typing import Callable, Any # pragma: no cover
import token # pragma: no cover

syms = SimpleNamespace(atom=1, testlist_gexp=2, asexpr_test=3) # pragma: no cover
node = SimpleNamespace(type=syms.testlist_gexp, children=[SimpleNamespace(type=syms.atom, children=[SimpleNamespace(type=syms.asexpr_test)])]) # pragma: no cover
parent = SimpleNamespace() # pragma: no cover
def maybe_make_parens_invisible_in_atom(node: Any, parent: Any, remove_brackets_around_comma: bool) -> bool: return True # pragma: no cover
def wrap_in_parentheses(parent: Any, node: Any, visible: bool): pass # pragma: no cover
def remove_with_parens(node: Any, parent: Any): pass # pragma: no cover
def mock_leaves(): return [] # pragma: no cover
node.children[0].leaves = mock_leaves # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/linegen.py
from l3.Runtime import _l_
"""Recursively hide optional parens in `with` statements."""
# Removing all unnecessary parentheses in with statements in one pass is a tad
# complex as different variations of bracketed statements result in pretty
# different parse trees:
#
# with (open("file")) as f:                       # this is an asexpr_test
#     ...
#
# with (open("file") as f):                       # this is an atom containing an
#     ...                                         # asexpr_test
#
# with (open("file")) as f, (open("file")) as f:  # this is asexpr_test, COMMA,
#     ...                                         # asexpr_test
#
# with (open("file") as f, open("file") as f):    # an atom containing a
#     ...                                         # testlist_gexp which then
#                                                 # contains multiple asexpr_test(s)
if node.type == syms.atom:
    _l_(18402)

    if maybe_make_parens_invisible_in_atom(
        node,
        parent=parent,
        remove_brackets_around_comma=True,
    ):
        _l_(18392)

        wrap_in_parentheses(parent, node, visible=False)
        _l_(18391)
    if isinstance(node.children[1], Node):
        _l_(18394)

        remove_with_parens(node.children[1], node)
        _l_(18393)
elif node.type == syms.testlist_gexp:
    _l_(18401)

    for child in node.children:
        _l_(18397)

        if isinstance(child, Node):
            _l_(18396)

            remove_with_parens(child, node)
            _l_(18395)
elif node.type == syms.asexpr_test and not any(
    leaf.type == token.COLONEQUAL for leaf in node.leaves()
):
    _l_(18400)

    if maybe_make_parens_invisible_in_atom(
        node.children[0],
        parent=node,
        remove_brackets_around_comma=True,
    ):
        _l_(18399)

        wrap_in_parentheses(node, node.children[0], visible=False)
        _l_(18398)
