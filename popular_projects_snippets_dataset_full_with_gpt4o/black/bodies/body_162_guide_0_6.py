from typing import Callable, Sequence, Iterator, Tuple, cast # pragma: no cover

Leaf = type('Leaf', (object,), {'__init__': lambda self, prefix, value: setattr(self, 'prefix', prefix) or setattr(self, 'value', value)}) # pragma: no cover
Index = int # pragma: no cover
enumerate_reversed = lambda seq: enumerate(reversed(list(seq))) # pragma: no cover
class MockSelf: # pragma: no cover
    def __init__(self, leaves, reversed=False): # pragma: no cover
        self.leaves = leaves # pragma: no cover
        self.reversed = reversed # pragma: no cover
    def comments_after(self, leaf): # pragma: no cover
        return [] # pragma: no cover
self = MockSelf([Leaf('prefix1', 'value1\nvalue2'), Leaf('prefix2', 'value2')]) # pragma: no cover
reversed = False # pragma: no cover

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
