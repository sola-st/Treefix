from typing import List, Optional # pragma: no cover
import token # pragma: no cover

closing = type('MockClosing', (), {'type': token.RSQB, 'parent': None, 'opening_bracket': None})() # pragma: no cover
CLOSING_BRACKETS = {token.RBRACE, token.RSQB} # pragma: no cover
Preview = type('MockPreview', (), {'one_element_subscript': 'one_element_subscript', 'skip_magic_trailing_comma_in_subscript': 'skip_magic_trailing_comma'})() # pragma: no cover
is_one_sequence_between = lambda opening, closing, leaves, brackets: True # pragma: no cover
ensure_removable = True # pragma: no cover

from typing import List, Optional # pragma: no cover

class MockNode:# pragma: no cover
    def __init__(self, type, parent=None):# pragma: no cover
        self.type = type# pragma: no cover
        self.parent = parent # pragma: no cover
class Mock:# pragma: no cover
        self.leaves = leaves# pragma: no cover
        self.mode = mode# pragma: no cover
closing = MockNode(type='RBRACE') # pragma: no cover
CLOSING_BRACKETS = {'RBRACE', 'RSQB'} # pragma: no cover
class Preview:# pragma: no cover
    one_element_subscript = 'one_element_subscript'# pragma: no cover
    skip_magic_trailing_comma_in_subscript = 'skip_magic_trailing_comma' # pragma: no cover
class syms:# pragma: no cover
    trailer = 'trailer'# pragma: no cover
    subscriptlist = 'subscriptlist'# pragma: no cover
    listmaker = 'listmaker' # pragma: no cover
def is_one_sequence_between(opening, closing, leaves, brackets): return True # pragma: no cover
ensure_removable = True # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/lines.py
from l3.Runtime import _l_
"""Return True if we have a magic trailing comma, that is when:
        - there's a trailing comma here
        - it's not a one-tuple
        - it's not a single-element subscript
        Additionally, if ensure_removable:
        - it's not from square bracket indexing
        (specifically, single-element square bracket indexing with
        Preview.skip_magic_trailing_comma_in_subscript)
        """
if not (
    closing.type in CLOSING_BRACKETS
    and self.leaves
    and self.leaves[-1].type == token.COMMA
):
    _l_(5573)

    aux = False
    _l_(5572)
    exit(aux)

if closing.type == token.RBRACE:
    _l_(5575)

    aux = True
    _l_(5574)
    exit(aux)

if closing.type == token.RSQB:
    _l_(5586)

    if (
        Preview.one_element_subscript in self.mode
        and closing.parent
        and closing.parent.type == syms.trailer
        and closing.opening_bracket
        and is_one_sequence_between(
            closing.opening_bracket,
            closing,
            self.leaves,
            brackets=(token.LSQB, token.RSQB),
        )
    ):
        _l_(5577)

        aux = False
        _l_(5576)
        exit(aux)

    if not ensure_removable:
        _l_(5579)

        aux = True
        _l_(5578)
        exit(aux)

    comma = self.leaves[-1]
    _l_(5580)
    if comma.parent is None:
        _l_(5582)

        aux = False
        _l_(5581)
        exit(aux)
    if Preview.skip_magic_trailing_comma_in_subscript in self.mode:
        _l_(5584)

        aux = (
            comma.parent.type != syms.subscriptlist
            or closing.opening_bracket is None
            or not is_one_sequence_between(
                closing.opening_bracket,
                closing,
                self.leaves,
                brackets=(token.LSQB, token.RSQB),
            )
        )
        _l_(5583)
        exit(aux)
    aux = comma.parent.type == syms.listmaker
    _l_(5585)
    exit(aux)

if self.is_import:
    _l_(5588)

    aux = True
    _l_(5587)
    exit(aux)

if closing.opening_bracket is not None and not is_one_sequence_between(
    closing.opening_bracket, closing, self.leaves
):
    _l_(5590)

    aux = True
    _l_(5589)
    exit(aux)
aux = False
_l_(5591)

exit(aux)
