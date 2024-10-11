from typing import List, Optional # pragma: no cover

from typing import List, Optional # pragma: no cover
from unittest.mock import Mock # pragma: no cover

class MockNode:# pragma: no cover
    def __init__(self, node_type, children):# pragma: no cover
        self.type = node_type# pragma: no cover
        self.children = children# pragma: no cover
    def leaves(self):# pragma: no cover
        return [] # pragma: no cover
syms = Mock(atom='atom', testlist_gexp='testlist_gexp', asexpr_test='asexpr_test') # pragma: no cover
node = MockNode('atom', [MockNode('asexpr_test', [])]) # pragma: no cover
maybe_make_parens_invisible_in_atom = Mock(return_value=True) # pragma: no cover
parent = MockNode('parent', []) # pragma: no cover
def wrap_in_parentheses(parent, node, visible):# pragma: no cover
    pass # pragma: no cover
Node = MockNode # pragma: no cover
def remove_with_parens(node, parent):# pragma: no cover
    pass # pragma: no cover
class MockToken:# pragma: no cover
    COLONEQUAL = 'COLONEQUAL' # pragma: no cover
token = MockToken() # pragma: no cover

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
    _l_(6616)

    if maybe_make_parens_invisible_in_atom(
        node,
        parent=parent,
        remove_brackets_around_comma=True,
    ):
        _l_(6606)

        wrap_in_parentheses(parent, node, visible=False)
        _l_(6605)
    if isinstance(node.children[1], Node):
        _l_(6608)

        remove_with_parens(node.children[1], node)
        _l_(6607)
elif node.type == syms.testlist_gexp:
    _l_(6615)

    for child in node.children:
        _l_(6611)

        if isinstance(child, Node):
            _l_(6610)

            remove_with_parens(child, node)
            _l_(6609)
elif node.type == syms.asexpr_test and not any(
    leaf.type == token.COLONEQUAL for leaf in node.leaves()
):
    _l_(6614)

    if maybe_make_parens_invisible_in_atom(
        node.children[0],
        parent=node,
        remove_brackets_around_comma=True,
    ):
        _l_(6613)

        wrap_in_parentheses(node, node.children[0], visible=False)
        _l_(6612)
