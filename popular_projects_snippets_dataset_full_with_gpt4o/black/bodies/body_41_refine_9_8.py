from typing import Iterator # pragma: no cover
from collections import namedtuple # pragma: no cover

CannotSplit = type('CannotSplit', (Exception,), {}) # pragma: no cover
Line = type('Line', (object,), {'__init__': lambda self, mode, depth, inside_brackets: setattr(self, 'mode', mode) or setattr(self, 'depth', depth) or setattr(self, 'inside_brackets', inside_brackets) or setattr(self, 'leaves', []) or setattr(self, 'append_safe', lambda *args, **kwargs: None) or setattr(self, 'append', lambda *args: None)}) # pragma: no cover
Leaf = namedtuple('Leaf', []) # pragma: no cover
line = type('line', (object,), {'contains_standalone_comments': lambda self, x: True, 'mode': 'some_mode', 'depth': 0, 'inside_brackets': False, 'leaves': [Leaf() for _ in range(5)], 'comments_after': lambda self, leaf: [Leaf() for _ in range(2)]})() # pragma: no cover

from typing import Iterator, List # pragma: no cover
import collections # pragma: no cover

class CannotSplit(Exception): # pragma: no cover
    pass # pragma: no cover
 # pragma: no cover
class Leaf: # pragma: no cover
    pass # pragma: no cover
 # pragma: no cover
class Line: # pragma: no cover
    def __init__(self, mode: str, depth: int, inside_brackets: bool): # pragma: no cover
        self.mode = mode # pragma: no cover
        self.depth = depth # pragma: no cover
        self.inside_brackets = inside_brackets # pragma: no cover
        self.leaves = [] # pragma: no cover
    def append_safe(self, leaf: Leaf, preformatted: bool = False): # pragma: no cover
        if preformatted: # pragma: no cover
            raise ValueError('Cannot append leaf in preformatted mode') # pragma: no cover
        self.leaves.append(leaf) # pragma: no cover
    def append(self, leaf: Leaf): # pragma: no cover
        self.leaves.append(leaf) # pragma: no cover
    def contains_standalone_comments(self, index: int) -> bool: # pragma: no cover
        return index == 0 # pragma: no cover
    def comments_after(self, leaf: Leaf) -> List[Leaf]: # pragma: no cover
        return [] # pragma: no cover
 # pragma: no cover
line = Line(mode='sample_mode', depth=0, inside_brackets=False) # pragma: no cover
line.leaves = [Leaf(), Leaf()] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/linegen.py
from l3.Runtime import _l_
"""Split standalone comments from the rest of the line."""
if not line.contains_standalone_comments(0):
    _l_(18513)

    raise CannotSplit("Line does not have any standalone comments")
    _l_(18512)

current_line = Line(
    mode=line.mode, depth=line.depth, inside_brackets=line.inside_brackets
)
_l_(18514)

def append_to_line(leaf: Leaf) -> Iterator[Line]:
    _l_(18522)

    """Append `leaf` to current line or to new line if appending impossible."""
    nonlocal current_line
    _l_(18515)
    try:
        _l_(18521)

        current_line.append_safe(leaf, preformatted=True)
        _l_(18516)
    except ValueError:
        _l_(18520)

        aux = current_line
        _l_(18517)
        exit(aux)

        current_line = Line(
            line.mode, depth=line.depth, inside_brackets=line.inside_brackets
        )
        _l_(18518)
        current_line.append(leaf)
        _l_(18519)

for leaf in line.leaves:
    _l_(18526)

    aux = append_to_line(leaf)
    _l_(18523)
    exit(aux)

    for comment_after in line.comments_after(leaf):
        _l_(18525)

        aux = append_to_line(comment_after)
        _l_(18524)
        exit(aux)

if current_line:
    _l_(18528)

    aux = current_line
    _l_(18527)
    exit(aux)
