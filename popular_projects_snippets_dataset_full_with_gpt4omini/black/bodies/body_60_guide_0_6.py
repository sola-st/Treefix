from typing import Literal # pragma: no cover
import token # pragma: no cover

class MockLeaf: # pragma: no cover
    def __init__(self, type, value=''): # pragma: no cover
        self.type = type # pragma: no cover
        self.value = value # pragma: no cover
        self.prefix = '' # pragma: no cover
    def clone(self): # pragma: no cover
        return MockLeaf(self.type, self.value) # pragma: no cover
 # pragma: no cover
class MockLine: # pragma: no cover
    def __init__(self, leaves): # pragma: no cover
        self.leaves = leaves # pragma: no cover
        self.comments_after_list = [] # pragma: no cover
    def clone(self): # pragma: no cover
        return MockLine([leaf.clone() for leaf in self.leaves]) # pragma: no cover
    def append(self, leaf, preformatted=False): # pragma: no cover
        self.leaves.append(leaf) # pragma: no cover
    def comments_after(self, leaf): # pragma: no cover
        return self.comments_after_list # pragma: no cover
 # pragma: no cover
line = MockLine([ # pragma: no cover
    MockLeaf(token.DOUBLESTAR), # pragma: no cover
    MockLeaf(token.NAME, 'x'), # pragma: no cover
    MockLeaf(token.DOUBLESTAR), # pragma: no cover
    MockLeaf(token.NAME, 'y') # pragma: no cover
]) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/trans.py
from l3.Runtime import _l_
"""A transformer which normalizes spacing around power operators."""

# Performance optimization to avoid unnecessary Leaf clones and other ops.
for leaf in line.leaves:
    _l_(7031)

    if leaf.type == token.DOUBLESTAR:
        _l_(7029)

        break
        _l_(7028)
else:
    raise CannotTransform("No doublestar token was found in the line.")
    _l_(7030)

def is_simple_lookup(index: int, step: Literal[1, -1]) -> bool:
    _l_(7043)

    # Brackets and parentheses indicate calls, subscripts, etc. ...
    # basically stuff that doesn't count as "simple". Only a NAME lookup
    # or dotted lookup (eg. NAME.NAME) is OK.
    if step == -1:
        _l_(7034)

        disallowed = {token.RPAR, token.RSQB}
        _l_(7032)
    else:
        disallowed = {token.LPAR, token.LSQB}
        _l_(7033)

    while 0 <= index < len(line.leaves):
        _l_(7041)

        current = line.leaves[index]
        _l_(7035)
        if current.type in disallowed:
            _l_(7037)

            aux = False
            _l_(7036)
            exit(aux)
        if current.type not in {token.NAME, token.DOT} or current.value == "for":
            _l_(7039)

            aux = True
            _l_(7038)
            # If the current token isn't disallowed, we'll assume this is simple as
            # only the disallowed tokens are semantically attached to this lookup
            # expression we're checking. Also, stop early if we hit the 'for' bit
            # of a comprehension.
            exit(aux)

        index += step
        _l_(7040)
    aux = True
    _l_(7042)

    exit(aux)

def is_simple_operand(index: int, kind: Literal["base", "exponent"]) -> bool:
    _l_(7051)

    # An operand is considered "simple" if's a NAME, a numeric CONSTANT, a simple
    # lookup (see above), with or without a preceding unary operator.
    start = line.leaves[index]
    _l_(7044)
    if start.type in {token.NAME, token.NUMBER}:
        _l_(7046)

        aux = is_simple_lookup(index, step=(1 if kind == "exponent" else -1))
        _l_(7045)
        exit(aux)

    if start.type in {token.PLUS, token.MINUS, token.TILDE}:
        _l_(7049)

        if line.leaves[index + 1].type in {token.NAME, token.NUMBER}:
            _l_(7048)

            aux = is_simple_lookup(index + 1, step=1)
            _l_(7047)
            # step is always one as bases with a preceding unary op will be checked
            # for simplicity starting from the next token (so it'll hit the check
            # above).
            exit(aux)
    aux = False
    _l_(7050)

    exit(aux)

new_line = line.clone()
_l_(7052)
should_hug = False
_l_(7053)
for idx, leaf in enumerate(line.leaves):
    _l_(7064)

    new_leaf = leaf.clone()
    _l_(7054)
    if should_hug:
        _l_(7057)

        new_leaf.prefix = ""
        _l_(7055)
        should_hug = False
        _l_(7056)

    should_hug = (
        (0 < idx < len(line.leaves) - 1)
        and leaf.type == token.DOUBLESTAR
        and is_simple_operand(idx - 1, kind="base")
        and line.leaves[idx - 1].value != "lambda"
        and is_simple_operand(idx + 1, kind="exponent")
    )
    _l_(7058)
    if should_hug:
        _l_(7060)

        new_leaf.prefix = ""
        _l_(7059)

    # We have to be careful to make a new line properly:
    # - bracket related metadata must be maintained (handled by Line.append)
    # - comments need to copied over, updating the leaf IDs they're attached to
    new_line.append(new_leaf, preformatted=True)
    _l_(7061)
    for comment_leaf in line.comments_after(leaf):
        _l_(7063)

        new_line.append(comment_leaf, preformatted=True)
        _l_(7062)
aux = new_line
_l_(7065)

exit(aux)
