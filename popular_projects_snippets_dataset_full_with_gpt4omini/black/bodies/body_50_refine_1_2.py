from typing import Set, Optional # pragma: no cover

Set = set # pragma: no cover
LeafID = int # pragma: no cover
class MockLine:  # pragma: no cover
    def __init__(self): # pragma: no cover
        self.magic_trailing_comma = False # pragma: no cover
        self.depth = 2 # pragma: no cover
        self.leaves = [] # pragma: no cover
    def enumerate_with_length(self, reversed=False): # pragma: no cover
        return enumerate(reversed(self.leaves)) if reversed else enumerate(self.leaves) # pragma: no cover
line = MockLine() # pragma: no cover
line_length = 20 # pragma: no cover
STANDALONE_COMMENT = 'standalone_comment' # pragma: no cover
CLOSING_BRACKETS = {'}', ']', ')'} # pragma: no cover
class MockToken:  # pragma: no cover
    COMMA = ',' # pragma: no cover
token = MockToken() # pragma: no cover
def is_one_sequence_between(opening_bracket, closing_bracket, leaves): # pragma: no cover
    return True # pragma: no cover
OPENING_BRACKETS = {'{', '[', '('} # pragma: no cover

from typing import Set, Optional # pragma: no cover

LeafID = int # pragma: no cover
omit: Set[LeafID] = set() # pragma: no cover
class Leaf:# pragma: no cover
    def __init__(self, value, leaf_type, prefix='', opening_bracket=None):# pragma: no cover
        self.value = value# pragma: no cover
        self.type = leaf_type# pragma: no cover
        self.prefix = prefix# pragma: no cover
        self.opening_bracket = opening_bracket # pragma: no cover
class Line:# pragma: no cover
    def __init__(self, depth, magic_trailing_comma):# pragma: no cover
        self.depth = depth# pragma: no cover
        self.magic_trailing_comma = magic_trailing_comma# pragma: no cover
        self.leaves = []# pragma: no cover
    # pragma: no cover
    def enumerate_with_length(self, reversed=False):# pragma: no cover
        for index, leaf in enumerate(self.leaves):# pragma: no cover
            yield index, leaf, len(leaf.value) + len(leaf.prefix) # pragma: no cover
line = Line(depth=2, magic_trailing_comma=False) # pragma: no cover
line_length = 20 # pragma: no cover
STANDALONE_COMMENT = 'standalone_comment' # pragma: no cover
CLOSING_BRACKETS = {'}', ']', ')'} # pragma: no cover
OPENING_BRACKETS = {'{', '[', '('} # pragma: no cover
token = type('Token', (), {'COMMA': ','}) # pragma: no cover
def is_one_sequence_between(opening_bracket, closing_bracket, leaves):# pragma: no cover
    return True # pragma: no cover
leaf1 = Leaf(value='(', leaf_type='(', opening_bracket=None)# pragma: no cover
leaf2 = Leaf(value=')', leaf_type=')', opening_bracket=leaf1)# pragma: no cover
line.leaves.append(leaf1)# pragma: no cover
line.leaves.append(leaf2) # pragma: no cover

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
