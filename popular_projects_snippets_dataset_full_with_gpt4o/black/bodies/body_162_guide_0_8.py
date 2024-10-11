from typing import Callable, Iterator, Sequence, Tuple, cast # pragma: no cover

class Leaf: # pragma: no cover
  def __init__(self, prefix, value): # pragma: no cover
    self.prefix = prefix # pragma: no cover
    self.value = value # pragma: no cover
 # pragma: no cover
self = type('Mock', (object,), { # pragma: no cover
  'leaves': [Leaf(' ', 'value_without_newline'), Leaf('/*comment*/', 'value_with\nnewline')], # pragma: no cover
  'comments_after': lambda self, leaf: [Leaf('', 'comment_after')] # pragma: no cover
})() # pragma: no cover
 # pragma: no cover
reversed = False # pragma: no cover
enumerate_reversed = lambda seq: enumerate(reversed(seq), 1) # pragma: no cover
Index = int  # This should be compatible with the type annotations # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/lines.py
from l3.Runtime import _l_
"""Return an enumeration of leaves with their length.

        Stops prematurely on multiline strings and standalone comments.
        """
op = cast(
    Callable[[Sequence[Leaf]], Iterator[Tuple[Index, Leaf]]],
    enumerate_reversed if reversed else enumerate,
)
_l_(16182)
for index, leaf in op(self.leaves):
    _l_(16189)

    length = len(leaf.prefix) + len(leaf.value)
    _l_(16183)
    if "\n" in leaf.value:
        _l_(16185)

        exit()  # Multiline strings, we can't continue.
        _l_(16184)  # Multiline strings, we can't continue.

    for comment in self.comments_after(leaf):
        _l_(16187)

        length += len(comment.value)
        _l_(16186)
    aux = (index, leaf, length)
    _l_(16188)

    exit(aux)
