from typing import List, Optional # pragma: no cover

class Leaf:# pragma: no cover
    def __init__(self, leaf_type, opening_bracket=None):# pragma: no cover
        self.type = leaf_type# pragma: no cover
        self.opening_bracket = opening_bracket # pragma: no cover
line = type('MockLine', (object,), {'leaves': [Leaf('(', None), Leaf('function_name', None), Leaf(')', Leaf('('))]})() # pragma: no cover
CLOSING_BRACKETS = [')', '}', ']', '>', '—'] # pragma: no cover
OPENING_BRACKETS = ['(', '{', '[', '<', '—'] # pragma: no cover
def ensure_visible(leaf): pass # pragma: no cover
class CannotSplit(Exception): pass # pragma: no cover
def bracket_split_build_line(leaves, line, matching_bracket, component): return leaves # pragma: no cover
_BracketSplitComponent = type('MockBracketSplitComponent', (object,), {'head': 'head_component', 'body': 'body_component', 'tail': 'tail_component'}) # pragma: no cover

from typing import List, Optional # pragma: no cover

class Leaf:# pragma: no cover
    def __init__(self, leaf_type, opening_bracket=None):# pragma: no cover
        self.type = leaf_type# pragma: no cover
        self.opening_bracket = opening_bracket # pragma: no cover
class Line:# pragma: no cover
    def __init__(self, leaves):# pragma: no cover
        self.leaves = leaves# pragma: no cover
line = Line([Leaf('('), Leaf('arg1'), Leaf('arg2'), Leaf(')')]) # pragma: no cover
CLOSING_BRACKETS = [')', '}', ']'] # pragma: no cover
OPENING_BRACKETS = ['(', '{', '['] # pragma: no cover
def ensure_visible(leaf): pass # pragma: no cover
class CannotSplit(Exception): pass # pragma: no cover
def bracket_split_build_line(leaves, line, matching_bracket, component): return leaves # pragma: no cover
_BracketSplitComponent = type('MockBracketSplitComponent', (object,), {'head': 'head', 'body': 'body', 'tail': 'tail'})() # pragma: no cover
def bracket_split_succeeded_or_raise(head, body, tail): pass # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/linegen.py
from l3.Runtime import _l_
"""Split line into many lines, starting with the first matching bracket pair.

    Note: this usually looks weird, only use this for function definitions.
    Prefer RHS otherwise.  This is why this function is not symmetrical with
    :func:`right_hand_split` which also handles optional parentheses.
    """
tail_leaves: List[Leaf] = []
_l_(4396)
body_leaves: List[Leaf] = []
_l_(4397)
head_leaves: List[Leaf] = []
_l_(4398)
current_leaves = head_leaves
_l_(4399)
matching_bracket: Optional[Leaf] = None
_l_(4400)
for leaf in line.leaves:
    _l_(4410)

    if (
        current_leaves is body_leaves
        and leaf.type in CLOSING_BRACKETS
        and leaf.opening_bracket is matching_bracket
        and isinstance(matching_bracket, Leaf)
    ):
        _l_(4404)

        ensure_visible(leaf)
        _l_(4401)
        ensure_visible(matching_bracket)
        _l_(4402)
        current_leaves = tail_leaves if body_leaves else head_leaves
        _l_(4403)
    current_leaves.append(leaf)
    _l_(4405)
    if current_leaves is head_leaves:
        _l_(4409)

        if leaf.type in OPENING_BRACKETS:
            _l_(4408)

            matching_bracket = leaf
            _l_(4406)
            current_leaves = body_leaves
            _l_(4407)
if not matching_bracket:
    _l_(4412)

    raise CannotSplit("No brackets found")
    _l_(4411)

head = bracket_split_build_line(
    head_leaves, line, matching_bracket, component=_BracketSplitComponent.head
)
_l_(4413)
body = bracket_split_build_line(
    body_leaves, line, matching_bracket, component=_BracketSplitComponent.body
)
_l_(4414)
tail = bracket_split_build_line(
    tail_leaves, line, matching_bracket, component=_BracketSplitComponent.tail
)
_l_(4415)
bracket_split_succeeded_or_raise(head, body, tail)
_l_(4416)
for result in (head, body, tail):
    _l_(4419)

    if result:
        _l_(4418)

        aux = result
        _l_(4417)
        exit(aux)
