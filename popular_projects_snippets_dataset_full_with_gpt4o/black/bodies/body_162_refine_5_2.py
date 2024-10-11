from typing import Callable, Sequence, Iterator, Tuple # pragma: no cover
from typing import cast # pragma: no cover
from dataclasses import dataclass # pragma: no cover

@dataclass # pragma: no cover
class Leaf: # pragma: no cover
    prefix: str # pragma: no cover
    value: str # pragma: no cover
class MockSelf: # pragma: no cover
    def __init__(self, leaves, comments): # pragma: no cover
        self.leaves = leaves # pragma: no cover
        self._comments = comments # pragma: no cover
    def comments_after(self, leaf): # pragma: no cover
        return self._comments # pragma: no cover
leaves = [Leaf(prefix=' ', value='a'), Leaf(prefix=' ', value='b')] # pragma: no cover
comments = [Leaf(prefix='', value='#comment1'), Leaf(prefix='', value='#comment2')] # pragma: no cover
self = MockSelf(leaves=leaves, comments=comments) # pragma: no cover
enumerate_reversed = lambda seq: enumerate(reversed(seq)) # pragma: no cover
Index = int # pragma: no cover

from typing import Callable, Sequence, Iterator, Tuple # pragma: no cover
from typing import cast # pragma: no cover
from dataclasses import dataclass # pragma: no cover

@dataclass # pragma: no cover
class Leaf: # pragma: no cover
    prefix: str # pragma: no cover
    value: str # pragma: no cover
class MockSelf: # pragma: no cover
    def __init__(self, leaves, comments): # pragma: no cover
        self.leaves = leaves # pragma: no cover
        self._comments = comments # pragma: no cover
    def comments_after(self, leaf): # pragma: no cover
        return self._comments # pragma: no cover
leaves = [Leaf(prefix=' ', value='a'), Leaf(prefix=' ', value='b')] # pragma: no cover
comments = [Leaf(prefix='', value='#comment1'), Leaf(prefix='', value='#comment2')] # pragma: no cover
self = MockSelf(leaves=leaves, comments=comments) # pragma: no cover
enumerate_reversed = lambda seq: enumerate(reversed(seq)) # pragma: no cover
Index = int # pragma: no cover
exit = print # pragma: no cover

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
