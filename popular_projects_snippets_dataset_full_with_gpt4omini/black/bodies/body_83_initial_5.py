from typing import Optional # pragma: no cover

class MockToken: STRING = 'STRING'; COMMA = 'COMMA' # pragma: no cover
class MockSyms: atom = 'atom' # pragma: no cover
def mock_parent_type(node): return 'atom' if hasattr(node, 'parent') else None # pragma: no cover
LL = [{'type': MockToken.STRING, 'prev_sibling': None, 'next_sibling': None, 'parent': None}] # pragma: no cover
token = MockToken() # pragma: no cover
syms = MockSyms() # pragma: no cover
parent_type = mock_parent_type # pragma: no cover

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
    _l_(7003)

    aux = None
    _l_(7002)
    exit(aux)

# If the string is surrounded by commas (or is the first/last child)...
prev_sibling = LL[0].prev_sibling
_l_(7004)
next_sibling = LL[0].next_sibling
_l_(7005)
if not prev_sibling and not next_sibling and parent_type(LL[0]) == syms.atom:
    _l_(7010)

    # If it's an atom string, we need to check the parent atom's siblings.
    parent = LL[0].parent
    _l_(7006)
    assert parent is not None  # For type checkers.
    _l_(7007)  # For type checkers.
    prev_sibling = parent.prev_sibling
    _l_(7008)
    next_sibling = parent.next_sibling
    _l_(7009)
if (not prev_sibling or prev_sibling.type == token.COMMA) and (
    not next_sibling or next_sibling.type == token.COMMA
):
    _l_(7012)

    aux = 0
    _l_(7011)
    exit(aux)
aux = None
_l_(7013)

exit(aux)
