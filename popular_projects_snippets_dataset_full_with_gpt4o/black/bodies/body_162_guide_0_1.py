from typing import Callable, Sequence, Iterator, Tuple, cast # pragma: no cover

class Leaf:# pragma: no cover
    def __init__(self, prefix, value):# pragma: no cover
        self.prefix = prefix# pragma: no cover
        self.value = value # pragma: no cover
class MockSelf:# pragma: no cover
    def __init__(self, leaves, comments):# pragma: no cover
        self.leaves = leaves# pragma: no cover
        self.comments = comments# pragma: no cover
    def comments_after(self, leaf):# pragma: no cover
        return self.comments # pragma: no cover
mock_leaf_1 = Leaf(prefix=' ', value='print("hello")') # pragma: no cover
mock_leaf_2 = Leaf(prefix=' ', value='"""example"""') # pragma: no cover
mock_comment = Leaf(prefix='', value='# Comment') # pragma: no cover
self = MockSelf(leaves=[mock_leaf_1, mock_leaf_2], comments=[mock_comment]) # pragma: no cover
reversed = False # pragma: no cover
enumerate_reversed = lambda seq: zip(range(len(seq)-1, -1, -1), seq) # pragma: no cover

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
