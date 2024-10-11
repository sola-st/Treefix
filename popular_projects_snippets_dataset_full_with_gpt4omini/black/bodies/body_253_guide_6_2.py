from collections import namedtuple # pragma: no cover

OPENING_BRACKETS = {'(': '(', '{': '{', '[': '['} # pragma: no cover
CLOSING_BRACKETS = {')': '(', '}': '{', ']': '['} # pragma: no cover
BRACKET = {')': '(', '}': '{', ']': '['} # pragma: no cover
Leaf = namedtuple('Leaf', ['type']) # pragma: no cover
leaves = [Leaf('('), Leaf('1'), Leaf(')'), Leaf('2')]  # Contains matching brackets # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/brackets.py
from l3.Runtime import _l_
"""Return leaves that are inside matching brackets.

    The input `leaves` can have non-matching brackets at the head or tail parts.
    Matching brackets are included.
    """
try:
    _l_(4194)

    # Start with the first opening bracket and ignore closing brackets before.
    start_index = next(
        i for i, l in enumerate(leaves) if l.type in OPENING_BRACKETS
    )
    _l_(4191)
except StopIteration:
    _l_(4193)

    aux = set()
    _l_(4192)
    exit(aux)
bracket_stack = []
_l_(4195)
ids = set()
_l_(4196)
for i in range(start_index, len(leaves)):
    _l_(4206)

    leaf = leaves[i]
    _l_(4197)
    if leaf.type in OPENING_BRACKETS:
        _l_(4199)

        bracket_stack.append((BRACKET[leaf.type], i))
        _l_(4198)
    if leaf.type in CLOSING_BRACKETS:
        _l_(4205)

        if bracket_stack and leaf.type == bracket_stack[-1][0]:
            _l_(4204)

            _, start = bracket_stack.pop()
            _l_(4200)
            for j in range(start, i + 1):
                _l_(4202)

                ids.add(id(leaves[j]))
                _l_(4201)
        else:
            break
            _l_(4203)
aux = ids
_l_(4207)
exit(aux)
