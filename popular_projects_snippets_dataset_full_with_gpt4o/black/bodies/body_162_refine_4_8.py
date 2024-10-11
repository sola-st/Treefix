from typing import Callable, Sequence, Iterator, Tuple # pragma: no cover
from typing import cast # pragma: no cover

class Leaf: # pragma: no cover
    def __init__(self, prefix: str, value: str): # pragma: no cover
        self.prefix = prefix # pragma: no cover
        self.value = value # pragma: no cover
 # pragma: no cover
def enumerate_reversed(leaves: Sequence[Leaf]) -> Iterator[Tuple[int, Leaf]]: # pragma: no cover
    return enumerate(reversed(leaves)) # pragma: no cover
 # pragma: no cover
class MockSelf: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.leaves = [Leaf('', 'leaf1'), Leaf('', 'leaf2')] # pragma: no cover
 # pragma: no cover
    def comments_after(self, leaf: Leaf): # pragma: no cover
        return [Leaf('', 'comment1'), Leaf('', 'comment2')] # pragma: no cover
 # pragma: no cover
self = MockSelf() # pragma: no cover

from typing import Callable, Sequence, Iterator, Tuple # pragma: no cover
from typing import cast # pragma: no cover

class Leaf: # pragma: no cover
    def __init__(self, prefix: str, value: str): # pragma: no cover
        self.prefix = prefix # pragma: no cover
        self.value = value # pragma: no cover
 # pragma: no cover
def enumerate_reversed(leaves: Sequence[Leaf]) -> Iterator[Tuple[int, Leaf]]: # pragma: no cover
    return enumerate(reversed(leaves)) # pragma: no cover
 # pragma: no cover
Index = int # pragma: no cover
 # pragma: no cover
class MockSelf: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.leaves = [Leaf('', 'leaf1'), Leaf('', 'leaf2')] # pragma: no cover
 # pragma: no cover
    def comments_after(self, leaf: Leaf): # pragma: no cover
        return [Leaf('', 'comment1'), Leaf('', 'comment2')] # pragma: no cover
 # pragma: no cover
self = MockSelf() # pragma: no cover

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
