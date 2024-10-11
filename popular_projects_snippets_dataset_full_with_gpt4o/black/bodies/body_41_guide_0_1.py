from typing import Iterator, List # pragma: no cover
from dataclasses import dataclass, field # pragma: no cover

@dataclass # pragma: no cover
class Line: # pragma: no cover
    mode: str # pragma: no cover
    depth: int # pragma: no cover
    inside_brackets: bool # pragma: no cover
    leaves: List['Leaf'] = field(default_factory=list) # pragma: no cover
    def append_safe(self, leaf: 'Leaf', preformatted: bool = False): # pragma: no cover
        if len(self.leaves) < 5: # pragma: no cover
            self.leaves.append(leaf) # pragma: no cover
        else: # pragma: no cover
            raise ValueError('Too many leaves') # pragma: no cover
    def append(self, leaf: 'Leaf'): # pragma: no cover
        self.leaves.append(leaf) # pragma: no cover
    def comments_after(self, leaf: 'Leaf'): # pragma: no cover
        return [] if leaf.text != 'comment' else [Leaf('comment_after')] # pragma: no cover
class CannotSplit(Exception): # pragma: no cover
    pass # pragma: no cover
class Leaf: # pragma: no cover
    def __init__(self, text: str): # pragma: no cover
        self.text = text # pragma: no cover
type('Mock', (object,), {'contains_standalone_comments': lambda self, x: False}) # pragma: no cover
line = type('Mock', (object,), { # pragma: no cover
    'contains_standalone_comments': lambda self, x: True, # pragma: no cover
    'mode': 'default', # pragma: no cover
    'depth': 1, # pragma: no cover
    'inside_brackets': False, # pragma: no cover
    'leaves': [Leaf('leaf1'), Leaf('leaf2'), Leaf('comment')], # pragma: no cover
    'comments_after': lambda self, leaf: [Leaf('comment_after')] if leaf.text == 'comment' else [] # pragma: no cover
})() # pragma: no cover

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
