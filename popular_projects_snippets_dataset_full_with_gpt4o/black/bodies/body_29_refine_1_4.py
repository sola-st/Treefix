from typing import List, Optional # pragma: no cover
from collections import namedtuple # pragma: no cover
import sys # pragma: no cover

Leaf = namedtuple('Leaf', ['type', 'opening_bracket']) # pragma: no cover
line = type('Mock', (object,), {'leaves': []}) # pragma: no cover
CLOSING_BRACKETS = set() # pragma: no cover
ensure_visible = lambda leaf: None # pragma: no cover
OPENING_BRACKETS = set() # pragma: no cover
CannotSplit = type('CannotSplit', (Exception,), {}) # pragma: no cover
bracket_split_build_line = lambda leaves, line, matching_bracket, component: None # pragma: no cover
_BracketSplitComponent = type('Mock', (object,), {'head': 'head', 'body': 'body', 'tail': 'tail'}) # pragma: no cover
bracket_split_succeeded_or_raise = lambda head, body, tail: None # pragma: no cover

from typing import List, Optional # pragma: no cover
from collections import namedtuple # pragma: no cover
import sys # pragma: no cover

Leaf = namedtuple('Leaf', ['type', 'opening_bracket']) # pragma: no cover
line = type('Mock', (object,), {'leaves': [Leaf(type='(', opening_bracket=None), Leaf(type=')', opening_bracket=None)]}) # pragma: no cover
CLOSING_BRACKETS = {')'} # pragma: no cover
ensure_visible = lambda leaf: None # pragma: no cover
OPENING_BRACKETS = {'('} # pragma: no cover
CannotSplit = type('CannotSplit', (Exception,), {}) # pragma: no cover
bracket_split_build_line = lambda leaves, line, matching_bracket, component: f'{component} line with {len(leaves)} leaves' # pragma: no cover
_BracketSplitComponent = type('Mock', (object,), {'head': 'head', 'body': 'body', 'tail': 'tail'}) # pragma: no cover
bracket_split_succeeded_or_raise = lambda head, body, tail: None # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/linegen.py
from l3.Runtime import _l_
"""Split line into many lines, starting with the first matching bracket pair.

    Note: this usually looks weird, only use this for function definitions.
    Prefer RHS otherwise.  This is why this function is not symmetrical with
    :func:`right_hand_split` which also handles optional parentheses.
    """
tail_leaves: List[Leaf] = []
_l_(16005)
body_leaves: List[Leaf] = []
_l_(16006)
head_leaves: List[Leaf] = []
_l_(16007)
current_leaves = head_leaves
_l_(16008)
matching_bracket: Optional[Leaf] = None
_l_(16009)
for leaf in line.leaves:
    _l_(16019)

    if (
        current_leaves is body_leaves
        and leaf.type in CLOSING_BRACKETS
        and leaf.opening_bracket is matching_bracket
        and isinstance(matching_bracket, Leaf)
    ):
        _l_(16013)

        ensure_visible(leaf)
        _l_(16010)
        ensure_visible(matching_bracket)
        _l_(16011)
        current_leaves = tail_leaves if body_leaves else head_leaves
        _l_(16012)
    current_leaves.append(leaf)
    _l_(16014)
    if current_leaves is head_leaves:
        _l_(16018)

        if leaf.type in OPENING_BRACKETS:
            _l_(16017)

            matching_bracket = leaf
            _l_(16015)
            current_leaves = body_leaves
            _l_(16016)
if not matching_bracket:
    _l_(16021)

    raise CannotSplit("No brackets found")
    _l_(16020)

head = bracket_split_build_line(
    head_leaves, line, matching_bracket, component=_BracketSplitComponent.head
)
_l_(16022)
body = bracket_split_build_line(
    body_leaves, line, matching_bracket, component=_BracketSplitComponent.body
)
_l_(16023)
tail = bracket_split_build_line(
    tail_leaves, line, matching_bracket, component=_BracketSplitComponent.tail
)
_l_(16024)
bracket_split_succeeded_or_raise(head, body, tail)
_l_(16025)
for result in (head, body, tail):
    _l_(16028)

    if result:
        _l_(16027)

        aux = result
        _l_(16026)
        exit(aux)
