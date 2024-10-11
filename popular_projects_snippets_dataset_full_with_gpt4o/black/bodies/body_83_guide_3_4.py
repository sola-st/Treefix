import token # pragma: no cover
import types # pragma: no cover

class MockNode: # pragma: no cover
    def __init__(self, node_type, prev_sibling=None, next_sibling=None, parent=None): # pragma: no cover
        self.type = node_type # pragma: no cover
        self.prev_sibling = prev_sibling # pragma: no cover
        self.next_sibling = next_sibling # pragma: no cover
        self.parent = parent # pragma: no cover
 # pragma: no cover
class syms: # pragma: no cover
    atom = 1 # pragma: no cover
 # pragma: no cover
def parent_type(node): # pragma: no cover
    return node.parent.type if node.parent else None # pragma: no cover
 # pragma: no cover
parent_node = MockNode(node_type=syms.atom, prev_sibling=MockNode(token.COMMA), next_sibling=MockNode(token.COMMA)) # pragma: no cover
LL = [MockNode(node_type=token.STRING, parent=parent_node)] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/trans.py
from l3.Runtime import _l_
"""
        Returns:
            string_idx such that @LL[string_idx] is equal to our target (i.e.
            matched) string, if this line matches the "prefer paren wrap" statement
            requirements listed in the 'Requirements' section of the StringParenWrapper
            class's docstring.
                OR
            None, otherwise.
        """
# The line must start with a string.
if LL[0].type != token.STRING:
    _l_(18748)

    aux = None
    _l_(18747)
    exit(aux)

# If the string is surrounded by commas (or is the first/last child)...
prev_sibling = LL[0].prev_sibling
_l_(18749)
next_sibling = LL[0].next_sibling
_l_(18750)
if not prev_sibling and not next_sibling and parent_type(LL[0]) == syms.atom:
    _l_(18755)

    # If it's an atom string, we need to check the parent atom's siblings.
    parent = LL[0].parent
    _l_(18751)
    assert parent is not None  # For type checkers.
    _l_(18752)  # For type checkers.
    prev_sibling = parent.prev_sibling
    _l_(18753)
    next_sibling = parent.next_sibling
    _l_(18754)
if (not prev_sibling or prev_sibling.type == token.COMMA) and (
    not next_sibling or next_sibling.type == token.COMMA
):
    _l_(18757)

    aux = 0
    _l_(18756)
    exit(aux)
aux = None
_l_(18758)

exit(aux)
