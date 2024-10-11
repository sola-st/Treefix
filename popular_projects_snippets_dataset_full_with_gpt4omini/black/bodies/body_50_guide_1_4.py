from typing import Set, Optional # pragma: no cover
import token # pragma: no cover

class Leaf:  # Mock class for demonstration purposes # pragma: no cover
    def __init__(self, leaf_type, value=''): # pragma: no cover
        self.type = leaf_type # pragma: no cover
        self.value = value # pragma: no cover
        self.prefix = '' # pragma: no cover
        self.opening_bracket = None # pragma: no cover
 # pragma: no cover
class Line:  # Mock class for demonstration purposes # pragma: no cover
    def __init__(self, leaves, depth, magic_trailing_comma): # pragma: no cover
        self.leaves = leaves # pragma: no cover
        self.depth = depth # pragma: no cover
        self.magic_trailing_comma = magic_trailing_comma # pragma: no cover
 # pragma: no cover
    def enumerate_with_length(self, reversed=False): # pragma: no cover
        for index, leaf in enumerate(reversed(self.leaves) if reversed else self.leaves): # pragma: no cover
            yield index, leaf, len(leaf.value) + len(leaf.prefix) # pragma: no cover
 # pragma: no cover
def is_one_sequence_between(opening, closing, leaves): # pragma: no cover
    return False # pragma: no cover
 # pragma: no cover
# Initialize line with a scenario that will trigger the uncovered line # pragma: no cover
opening_leaf = Leaf('(', '(') # pragma: no cover
line_length = 10 # pragma: no cover
omit = set() # pragma: no cover

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
_l_(4893)
if not line.magic_trailing_comma:
    _l_(4895)

    aux = omit
    _l_(4894)
    exit(aux)

length = 4 * line.depth
_l_(4896)
opening_bracket: Optional[Leaf] = None
_l_(4897)
closing_bracket: Optional[Leaf] = None
_l_(4898)
inner_brackets: Set[LeafID] = set()
_l_(4899)
for index, leaf, leaf_length in line.enumerate_with_length(reversed=True):
    _l_(4929)

    length += leaf_length
    _l_(4900)
    if length > line_length:
        _l_(4902)

        break
        _l_(4901)

    has_inline_comment = leaf_length > len(leaf.value) + len(leaf.prefix)
    _l_(4903)
    if leaf.type == STANDALONE_COMMENT or has_inline_comment:
        _l_(4905)

        break
        _l_(4904)

    if opening_bracket:
        _l_(4928)

        if leaf is opening_bracket:
            _l_(4912)

            opening_bracket = None
            _l_(4906)
        elif leaf.type in CLOSING_BRACKETS:
            _l_(4911)

            prev = line.leaves[index - 1] if index > 0 else None
            _l_(4907)
            if (
                prev
                and prev.type == token.COMMA
                and leaf.opening_bracket is not None
                and not is_one_sequence_between(
                    leaf.opening_bracket, leaf, line.leaves
                )
            ):
                _l_(4909)

                # Never omit bracket pairs with trailing commas.
                # We need to explode on those.
                break
                _l_(4908)

            inner_brackets.add(id(leaf))
            _l_(4910)
    elif leaf.type in CLOSING_BRACKETS:
        _l_(4927)

        prev = line.leaves[index - 1] if index > 0 else None
        _l_(4913)
        if prev and prev.type in OPENING_BRACKETS:
            _l_(4916)

            # Empty brackets would fail a split so treat them as "inner"
            # brackets (e.g. only add them to the `omit` set if another
            # pair of brackets was good enough.
            inner_brackets.add(id(leaf))
            _l_(4914)
            continue
            _l_(4915)

        if closing_bracket:
            _l_(4921)

            omit.add(id(closing_bracket))
            _l_(4917)
            omit.update(inner_brackets)
            _l_(4918)
            inner_brackets.clear()
            _l_(4919)
            aux = omit
            _l_(4920)
            exit(aux)

        if (
            prev
            and prev.type == token.COMMA
            and leaf.opening_bracket is not None
            and not is_one_sequence_between(leaf.opening_bracket, leaf, line.leaves)
        ):
            _l_(4923)

            # Never omit bracket pairs with trailing commas.
            # We need to explode on those.
            break
            _l_(4922)

        if leaf.value:
            _l_(4926)

            opening_bracket = leaf.opening_bracket
            _l_(4924)
            closing_bracket = leaf
            _l_(4925)
