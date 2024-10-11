from typing import Set, Optional # pragma: no cover
import token # pragma: no cover

LeafID = int # pragma: no cover
class Leaf: # pragma: no cover
    def __init__(self, type_, value='', prefix='', opening_bracket=None): # pragma: no cover
        self.type = type_ # pragma: no cover
        self.value = value # pragma: no cover
        self.prefix = prefix # pragma: no cover
        self.opening_bracket = opening_bracket # pragma: no cover
 # pragma: no cover
class Line: # pragma: no cover
    def __init__(self, leaves, depth=0, magic_trailing_comma=False): # pragma: no cover
        self.leaves = leaves # pragma: no cover
        self.depth = depth # pragma: no cover
        self.magic_trailing_comma = magic_trailing_comma # pragma: no cover
 # pragma: no cover
    def enumerate_with_length(self, reversed=False): # pragma: no cover
        leaves = list(reversed(self.leaves)) if reversed else self.leaves # pragma: no cover
        for i, leaf in enumerate(leaves): # pragma: no cover
            leaf_length = len(leaf.value) + len(leaf.prefix) # pragma: no cover
            yield i, leaf, leaf_length # pragma: no cover
 # pragma: no cover
def is_one_sequence_between(opening_bracket, closing_bracket, leaves): # pragma: no cover
    try: # pragma: no cover
        start = leaves.index(opening_bracket) + 1 # pragma: no cover
        end = leaves.index(closing_bracket) # pragma: no cover
        return end - start == 1 # pragma: no cover
    except ValueError: # pragma: no cover
        return False # pragma: no cover
 # pragma: no cover
line_length = 5 # pragma: no cover
STANDALONE_COMMENT = token.COMMENT # pragma: no cover
CLOSING_BRACKETS = {token.RPAR, token.RSQB, token.RBRACE} # pragma: no cover
OPENING_BRACKETS = {token.LPAR, token.LSQB, token.LBRACE} # pragma: no cover
leaf1 = Leaf(token.LPAR, '(') # pragma: no cover
leaf2 = Leaf(token.NAME, 'a', ' ') # pragma: no cover
leaf3 = Leaf(token.RPAR, ')', '', leaf1) # pragma: no cover
line = Line([leaf1, leaf2, leaf3], depth=1, magic_trailing_comma=False) # pragma: no cover

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
