from typing import Iterator, List # pragma: no cover

class CannotSplit(Exception): pass # pragma: no cover
class Line:# pragma: no cover
    def __init__(self, mode, depth, inside_brackets):# pragma: no cover
        self.mode = mode# pragma: no cover
        self.depth = depth# pragma: no cover
        self.inside_brackets = inside_brackets# pragma: no cover
        self.leaves = []# pragma: no cover
        self.comments = []# pragma: no cover
    # pragma: no cover
    def append_safe(self, leaf, preformatted):# pragma: no cover
        pass# pragma: no cover
    # pragma: no cover
    def comments_after(self, leaf):# pragma: no cover
        return [] # pragma: no cover
class Leaf: pass # pragma: no cover
line = Line(mode='normal', depth=0, inside_brackets=False) # pragma: no cover

from typing import Iterator # pragma: no cover

class CannotSplit(Exception): pass # pragma: no cover
class Leaf: pass # pragma: no cover
class Line:  # pragma: no cover
    def __init__(self, mode, depth, inside_brackets): # pragma: no cover
        self.mode = mode # pragma: no cover
        self.depth = depth # pragma: no cover
        self.inside_brackets = inside_brackets # pragma: no cover
        self.leaves = [] # pragma: no cover
        self.comments = [] # pragma: no cover
    def append_safe(self, leaf, preformatted): # pragma: no cover
        if preformatted: # pragma: no cover
            self.leaves.append(leaf) # pragma: no cover
        else: # pragma: no cover
            raise ValueError('Cannot append leaf') # pragma: no cover
    def comments_after(self, leaf): return self.comments # pragma: no cover
line = Line(mode='example_mode', depth=0, inside_brackets=False) # pragma: no cover
line.comments = ['This is a comment'] # pragma: no cover
current_line = Line(mode=line.mode, depth=line.depth, inside_brackets=line.inside_brackets) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/linegen.py
from l3.Runtime import _l_
"""Split standalone comments from the rest of the line."""
if not line.contains_standalone_comments(0):
    _l_(6867)

    raise CannotSplit("Line does not have any standalone comments")
    _l_(6866)

current_line = Line(
    mode=line.mode, depth=line.depth, inside_brackets=line.inside_brackets
)
_l_(6868)

def append_to_line(leaf: Leaf) -> Iterator[Line]:
    _l_(6876)

    """Append `leaf` to current line or to new line if appending impossible."""
    nonlocal current_line
    _l_(6869)
    try:
        _l_(6875)

        current_line.append_safe(leaf, preformatted=True)
        _l_(6870)
    except ValueError:
        _l_(6874)

        aux = current_line
        _l_(6871)
        exit(aux)

        current_line = Line(
            line.mode, depth=line.depth, inside_brackets=line.inside_brackets
        )
        _l_(6872)
        current_line.append(leaf)
        _l_(6873)

for leaf in line.leaves:
    _l_(6880)

    aux = append_to_line(leaf)
    _l_(6877)
    exit(aux)

    for comment_after in line.comments_after(leaf):
        _l_(6879)

        aux = append_to_line(comment_after)
        _l_(6878)
        exit(aux)

if current_line:
    _l_(6882)

    aux = current_line
    _l_(6881)
    exit(aux)
