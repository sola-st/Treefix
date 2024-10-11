from typing import List # pragma: no cover

class MockNode:  # Mock class to simulate the node structure# pragma: no cover
    def __init__(self, type, children=[]):# pragma: no cover
        self.type = type# pragma: no cover
        self.children = children# pragma: no cover
# pragma: no cover
    def leaves(self):# pragma: no cover
        return [leaf for child in self.children for leaf in (child.leaves() if hasattr(child, 'leaves') else [child])]# pragma: no cover
def maybe_make_parens_invisible_in_atom(node, parent, remove_brackets_around_comma): return True # pragma: no cover
def wrap_in_parentheses(parent, node, visible): pass # pragma: no cover
def remove_with_parens(node, parent): pass # pragma: no cover
syms = type('Mock', (object,), {'atom': 1, 'testlist_gexp': 2, 'asexpr_test': 3})() # pragma: no cover
token = type('Mock', (object,), {'COLONEQUAL': 4})() # pragma: no cover

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
