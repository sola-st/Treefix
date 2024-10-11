import token # pragma: no cover
from typing import Literal # pragma: no cover

class MockLine: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.leaves = [MockLeaf(token.NAME, 'a'), MockLeaf(token.DOUBLESTAR, '**'), MockLeaf(token.NUMBER, '2')] # pragma: no cover
    def clone(self): # pragma: no cover
        return MockLine() # pragma: no cover
    def append(self, leaf, preformatted): # pragma: no cover
        pass # pragma: no cover
    def comments_after(self, leaf): # pragma: no cover
        return [] # pragma: no cover
class MockLeaf: # pragma: no cover
    def __init__(self, type, value): # pragma: no cover
        self.type = type # pragma: no cover
        self.value = value # pragma: no cover
        self.prefix = None # pragma: no cover
    def clone(self): # pragma: no cover
        return MockLeaf(self.type, self.value) # pragma: no cover
class CannotTransform(Exception): # pragma: no cover
    pass # pragma: no cover
line = MockLine() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/trans.py
from l3.Runtime import _l_
"""A transformer which normalizes spacing around power operators."""

# Performance optimization to avoid unnecessary Leaf clones and other ops.
for leaf in line.leaves:
    _l_(18840)

    if leaf.type == token.DOUBLESTAR:
        _l_(18838)

        break
        _l_(18837)
else:
    raise CannotTransform("No doublestar token was found in the line.")
    _l_(18839)

def is_simple_lookup(index: int, step: Literal[1, -1]) -> bool:
    _l_(18852)

    # Brackets and parentheses indicate calls, subscripts, etc. ...
    # basically stuff that doesn't count as "simple". Only a NAME lookup
    # or dotted lookup (eg. NAME.NAME) is OK.
    if step == -1:
        _l_(18843)

        disallowed = {token.RPAR, token.RSQB}
        _l_(18841)
    else:
        disallowed = {token.LPAR, token.LSQB}
        _l_(18842)

    while 0 <= index < len(line.leaves):
        _l_(18850)

        current = line.leaves[index]
        _l_(18844)
        if current.type in disallowed:
            _l_(18846)

            aux = False
            _l_(18845)
            exit(aux)
        if current.type not in {token.NAME, token.DOT} or current.value == "for":
            _l_(18848)

            aux = True
            _l_(18847)
            # If the current token isn't disallowed, we'll assume this is simple as
            # only the disallowed tokens are semantically attached to this lookup
            # expression we're checking. Also, stop early if we hit the 'for' bit
            # of a comprehension.
            exit(aux)

        index += step
        _l_(18849)
    aux = True
    _l_(18851)

    exit(aux)

def is_simple_operand(index: int, kind: Literal["base", "exponent"]) -> bool:
    _l_(18860)

    # An operand is considered "simple" if's a NAME, a numeric CONSTANT, a simple
    # lookup (see above), with or without a preceding unary operator.
    start = line.leaves[index]
    _l_(18853)
    if start.type in {token.NAME, token.NUMBER}:
        _l_(18855)

        aux = is_simple_lookup(index, step=(1 if kind == "exponent" else -1))
        _l_(18854)
        exit(aux)

    if start.type in {token.PLUS, token.MINUS, token.TILDE}:
        _l_(18858)

        if line.leaves[index + 1].type in {token.NAME, token.NUMBER}:
            _l_(18857)

            aux = is_simple_lookup(index + 1, step=1)
            _l_(18856)
            # step is always one as bases with a preceding unary op will be checked
            # for simplicity starting from the next token (so it'll hit the check
            # above).
            exit(aux)
    aux = False
    _l_(18859)

    exit(aux)

new_line = line.clone()
_l_(18861)
should_hug = False
_l_(18862)
for idx, leaf in enumerate(line.leaves):
    _l_(18873)

    new_leaf = leaf.clone()
    _l_(18863)
    if should_hug:
        _l_(18866)

        new_leaf.prefix = ""
        _l_(18864)
        should_hug = False
        _l_(18865)

    should_hug = (
        (0 < idx < len(line.leaves) - 1)
        and leaf.type == token.DOUBLESTAR
        and is_simple_operand(idx - 1, kind="base")
        and line.leaves[idx - 1].value != "lambda"
        and is_simple_operand(idx + 1, kind="exponent")
    )
    _l_(18867)
    if should_hug:
        _l_(18869)

        new_leaf.prefix = ""
        _l_(18868)

    # We have to be careful to make a new line properly:
    # - bracket related metadata must be maintained (handled by Line.append)
    # - comments need to copied over, updating the leaf IDs they're attached to
    new_line.append(new_leaf, preformatted=True)
    _l_(18870)
    for comment_leaf in line.comments_after(leaf):
        _l_(18872)

        new_line.append(comment_leaf, preformatted=True)
        _l_(18871)
aux = new_line
_l_(18874)

exit(aux)
