from collections import namedtuple # pragma: no cover

Leaf = namedtuple('Leaf', ['type']) # pragma: no cover
leaves = [Leaf(type='('), Leaf(type='a'), Leaf(type=')'), Leaf(type='b')] # pragma: no cover
OPENING_BRACKETS = {'('} # pragma: no cover
BRACKET = {'(': ')'} # pragma: no cover
CLOSING_BRACKETS = {')'} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/brackets.py
from l3.Runtime import _l_
"""Return leaves that are inside matching brackets.

    The input `leaves` can have non-matching brackets at the head or tail parts.
    Matching brackets are included.
    """
try:
    _l_(15689)

    # Start with the first opening bracket and ignore closing brackets before.
    start_index = next(
        i for i, l in enumerate(leaves) if l.type in OPENING_BRACKETS
    )
    _l_(15686)
except StopIteration:
    _l_(15688)

    aux = set()
    _l_(15687)
    exit(aux)
bracket_stack = []
_l_(15690)
ids = set()
_l_(15691)
for i in range(start_index, len(leaves)):
    _l_(15701)

    leaf = leaves[i]
    _l_(15692)
    if leaf.type in OPENING_BRACKETS:
        _l_(15694)

        bracket_stack.append((BRACKET[leaf.type], i))
        _l_(15693)
    if leaf.type in CLOSING_BRACKETS:
        _l_(15700)

        if bracket_stack and leaf.type == bracket_stack[-1][0]:
            _l_(15699)

            _, start = bracket_stack.pop()
            _l_(15695)
            for j in range(start, i + 1):
                _l_(15697)

                ids.add(id(leaves[j]))
                _l_(15696)
        else:
            break
            _l_(15698)
aux = ids
_l_(15702)
exit(aux)
