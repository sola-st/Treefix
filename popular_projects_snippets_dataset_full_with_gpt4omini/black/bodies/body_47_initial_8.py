from sly import Lexer, Parser # pragma: no cover
from typing import List, Optional # pragma: no cover

class MockNode:                                         # Mock class for Node initialization # pragma: no cover
    def __init__(self, node_type, children):          # Node constructor # pragma: no cover
        self.type = node_type                          # Initialize type # pragma: no cover
        self.children = children                        # Initialize children # pragma: no cover
    def leaves(self):                                   # Mock method for leaves # pragma: no cover
        return []                                      # Return empty list # pragma: no cover
 # pragma: no cover
class MockSyms:                                       # Mock class for syms initialization # pragma: no cover
    atom = 'atom'                                      # Mock atom type # pragma: no cover
    testlist_gexp = 'testlist_gexp'                    # Mock testlist_gexp type # pragma: no cover
    asexpr_test = 'asexpr_test'                        # Mock asexpr_test type # pragma: no cover
 # pragma: no cover
class MockToken:                                      # Mock class for token initialization # pragma: no cover
    COLONEQUAL = 'COLONEQUAL'                          # Mock COLONEQUAL constant # pragma: no cover
 # pragma: no cover
node = MockNode('asexpr_test', [MockNode('atom', []), MockNode('testlist_gexp', [])]) # pragma: no cover
syms = MockSyms()                                     # Instantiate MockSyms # pragma: no cover
token = MockToken()                                   # Instantiate MockToken # pragma: no cover
parent = MockNode('parent', [])                       # Create mock parent node # pragma: no cover
maybe_make_parens_invisible_in_atom = lambda n, p, r: True  # Mock function for paren visibility # pragma: no cover
wrap_in_parentheses = lambda p, n, v: None           # Mock function for wrapping in parentheses # pragma: no cover
remove_with_parens = lambda n, p: None                # Mock function for removing parentheses # pragma: no cover

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
