from collections import namedtuple # pragma: no cover
from typing import List # pragma: no cover
import token # pragma: no cover

MockNode = namedtuple('MockNode', ['type', 'children', 'leaves']) # pragma: no cover
syms = type('MockSyms', (object,), {'atom': 1, 'testlist_gexp': 2, 'asexpr_test': 3})() # pragma: no cover
maybe_make_parens_invisible_in_atom = lambda node, parent, remove_brackets_around_comma: True # pragma: no cover
parent = MockNode(type=syms.testlist_gexp, children=[], leaves=lambda: []) # pragma: no cover
wrap_in_parentheses = lambda parent, node, visible: None # pragma: no cover
Node = MockNode # pragma: no cover
remove_with_parens = lambda node, parent: None # pragma: no cover
token.COLONEQUAL = 4 # pragma: no cover

from typing import List # pragma: no cover
import token # pragma: no cover

class MockNode: # pragma: no cover
    def __init__(self, type, children=None, leaves=None): # pragma: no cover
        self.type = type # pragma: no cover
        self.children = children if children else [] # pragma: no cover
        self._leaves = leaves if leaves else [] # pragma: no cover
    def leaves(self): # pragma: no cover
        return self._leaves # pragma: no cover
node = MockNode(type=1, children=[MockNode(type=3), MockNode(type=2)]) # pragma: no cover
syms = type('syms', (object,), {'atom': 1, 'testlist_gexp': 2, 'asexpr_test': 3}) # pragma: no cover
def maybe_make_parens_invisible_in_atom(node, parent, remove_brackets_around_comma: bool): # pragma: no cover
    return True # pragma: no cover
parent = MockNode(type=0) # pragma: no cover
def wrap_in_parentheses(parent, node, visible: bool): # pragma: no cover
    pass # pragma: no cover
Node = MockNode # pragma: no cover
def remove_with_parens(node, parent): # pragma: no cover
    pass # pragma: no cover
token = type('token', (object,), {'COLONEQUAL': 4}) # pragma: no cover

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
