from typing import Set, Optional # pragma: no cover
import token # pragma: no cover

LeafID = int # pragma: no cover
Leaf = type('Leaf', (object,), {'value': '', 'prefix': '', 'type': None, 'opening_bracket': None}) # pragma: no cover
class MockLine:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.magic_trailing_comma = False# pragma: no cover
        self.depth = 0# pragma: no cover
        self.leaves = []# pragma: no cover
        # pragma: no cover
    def enumerate_with_length(self, reversed=False):# pragma: no cover
        return enumerate([(None, Leaf(), 0)])# pragma: no cover
# pragma: no cover
line = MockLine() # pragma: no cover
line_length = 80 # pragma: no cover
STANDALONE_COMMENT = 'comment' # pragma: no cover
CLOSING_BRACKETS = {')', ']', '}'} # pragma: no cover
OPENING_BRACKETS = {'(', '[', '{'} # pragma: no cover
def is_one_sequence_between(opening_bracket, closing_bracket, leaves):# pragma: no cover
    return False # pragma: no cover

from typing import Set, Optional # pragma: no cover
import token # pragma: no cover

LeafID = int # pragma: no cover
Leaf = type('Leaf', (object,), {'__init__': lambda self, value='', prefix='', type=None, opening_bracket=None: setattr(self, 'value', value) or setattr(self, 'prefix', prefix) or setattr(self, 'type', type) or setattr(self, 'opening_bracket', opening_bracket) }) # pragma: no cover
MockLine = type('MockLine', (object,), { # pragma: no cover
    '__init__': lambda self: ( # pragma: no cover
        setattr(self, 'magic_trailing_comma', False), # pragma: no cover
        setattr(self, 'depth', 0), # pragma: no cover
        setattr(self, 'leaves', [Leaf(type=token.RPAR), Leaf(type=token.COMMA), Leaf(type=token.LPAR)]) # pragma: no cover
    ), # pragma: no cover
    'enumerate_with_length': lambda self, reversed=False: enumerate([ # pragma: no cover
        (0, Leaf(type=token.RPAR), 1), # pragma: no cover
        (1, Leaf(type=token.COMMA), 1), # pragma: no cover
        (2, Leaf(type=token.LPAR), 1) # pragma: no cover
    ]) # pragma: no cover
}) # pragma: no cover
line_length = 80 # pragma: no cover
STANDALONE_COMMENT = token.COMMENT # pragma: no cover
CLOSING_BRACKETS = {token.RPAR, token.RBRACE, token.RSQB} # pragma: no cover
OPENING_BRACKETS = {token.LPAR, token.LBRACE, token.LSQB} # pragma: no cover
is_one_sequence_between = lambda opening_bracket, closing_bracket, leaves: False # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/linegen.py
from l3.Runtime import _l_
"""Generate sets of closing bracket IDs that should be omitted in a RHS.

    Brackets can be omitted if the entire trailer up to and including
    a preceding closing bracket fits in one line.

    Yielded sets are cumulative (contain results of previous yields, too).  First
    set is empty, unless the line should explode, in which case bracket pairs until
    the one that needs to explode are omitted.
    """

omit: Set[LeafID] = set()
_l_(16488)
if not line.magic_trailing_comma:
    _l_(16490)

    aux = omit
    _l_(16489)
    exit(aux)

length = 4 * line.depth
_l_(16491)
opening_bracket: Optional[Leaf] = None
_l_(16492)
closing_bracket: Optional[Leaf] = None
_l_(16493)
inner_brackets: Set[LeafID] = set()
_l_(16494)
for index, leaf, leaf_length in line.enumerate_with_length(reversed=True):
    _l_(16524)

    length += leaf_length
    _l_(16495)
    if length > line_length:
        _l_(16497)

        break
        _l_(16496)

    has_inline_comment = leaf_length > len(leaf.value) + len(leaf.prefix)
    _l_(16498)
    if leaf.type == STANDALONE_COMMENT or has_inline_comment:
        _l_(16500)

        break
        _l_(16499)

    if opening_bracket:
        _l_(16523)

        if leaf is opening_bracket:
            _l_(16507)

            opening_bracket = None
            _l_(16501)
        elif leaf.type in CLOSING_BRACKETS:
            _l_(16506)

            prev = line.leaves[index - 1] if index > 0 else None
            _l_(16502)
            if (
                prev
                and prev.type == token.COMMA
                and leaf.opening_bracket is not None
                and not is_one_sequence_between(
                    leaf.opening_bracket, leaf, line.leaves
                )
            ):
                _l_(16504)

                # Never omit bracket pairs with trailing commas.
                # We need to explode on those.
                break
                _l_(16503)

            inner_brackets.add(id(leaf))
            _l_(16505)
    elif leaf.type in CLOSING_BRACKETS:
        _l_(16522)

        prev = line.leaves[index - 1] if index > 0 else None
        _l_(16508)
        if prev and prev.type in OPENING_BRACKETS:
            _l_(16511)

            # Empty brackets would fail a split so treat them as "inner"
            # brackets (e.g. only add them to the `omit` set if another
            # pair of brackets was good enough.
            inner_brackets.add(id(leaf))
            _l_(16509)
            continue
            _l_(16510)

        if closing_bracket:
            _l_(16516)

            omit.add(id(closing_bracket))
            _l_(16512)
            omit.update(inner_brackets)
            _l_(16513)
            inner_brackets.clear()
            _l_(16514)
            aux = omit
            _l_(16515)
            exit(aux)

        if (
            prev
            and prev.type == token.COMMA
            and leaf.opening_bracket is not None
            and not is_one_sequence_between(leaf.opening_bracket, leaf, line.leaves)
        ):
            _l_(16518)

            # Never omit bracket pairs with trailing commas.
            # We need to explode on those.
            break
            _l_(16517)

        if leaf.value:
            _l_(16521)

            opening_bracket = leaf.opening_bracket
            _l_(16519)
            closing_bracket = leaf
            _l_(16520)
