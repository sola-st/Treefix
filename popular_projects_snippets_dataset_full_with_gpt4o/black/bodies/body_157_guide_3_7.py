import token # pragma: no cover
from types import SimpleNamespace # pragma: no cover

CLOSING_BRACKETS = {token.RBRACE, token.RSQB, token.RPAR} # pragma: no cover
def is_one_sequence_between(opening_bracket, closing, leaves, brackets): # pragma: no cover
    return True # pragma: no cover
syms = SimpleNamespace(trailer=1, subscriptlist=2, listmaker=3) # pragma: no cover
Preview = SimpleNamespace(one_element_subscript=1, skip_magic_trailing_comma_in_subscript=2) # pragma: no cover
comma_parent = SimpleNamespace(type=syms.subscriptlist) # pragma: no cover
self = SimpleNamespace( # pragma: no cover
    leaves=[SimpleNamespace(type=token.COMMA, parent=comma_parent)], # pragma: no cover
    mode=[Preview.skip_magic_trailing_comma_in_subscript], # pragma: no cover
) # pragma: no cover
closing = SimpleNamespace( # pragma: no cover
    type=token.RSQB, # pragma: no cover
    parent=SimpleNamespace(type=syms.trailer), # pragma: no cover
    opening_bracket=SimpleNamespace() # pragma: no cover
) # pragma: no cover
ensure_removable = False # pragma: no cover

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
    _l_(17034)

    aux = False
    _l_(17033)
    exit(aux)

if closing.type == token.RBRACE:
    _l_(17036)

    aux = True
    _l_(17035)
    exit(aux)

if closing.type == token.RSQB:
    _l_(17047)

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
        _l_(17038)

        aux = False
        _l_(17037)
        exit(aux)

    if not ensure_removable:
        _l_(17040)

        aux = True
        _l_(17039)
        exit(aux)

    comma = self.leaves[-1]
    _l_(17041)
    if comma.parent is None:
        _l_(17043)

        aux = False
        _l_(17042)
        exit(aux)
    if Preview.skip_magic_trailing_comma_in_subscript in self.mode:
        _l_(17045)

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
        _l_(17044)
        exit(aux)
    aux = comma.parent.type == syms.listmaker
    _l_(17046)
    exit(aux)

if self.is_import:
    _l_(17049)

    aux = True
    _l_(17048)
    exit(aux)

if closing.opening_bracket is not None and not is_one_sequence_between(
    closing.opening_bracket, closing, self.leaves
):
    _l_(17051)

    aux = True
    _l_(17050)
    exit(aux)
aux = False
_l_(17052)

exit(aux)
